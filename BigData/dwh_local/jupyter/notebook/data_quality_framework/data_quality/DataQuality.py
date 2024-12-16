import logging
from reader.JSONFileReader import JSONFileReader
from great_expectations.dataset.sparkdf_dataset import SparkDFDataset
from expectation.NotNullExpectation import NotNullExpectation
from expectation.UniqueExpectation import UniqueExpectation
from expectation.ValuesInListExpectation import ValuesInListExpectation

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DataQuality:

    def __init__(self, pyspark_df, config_path):
        self.pyspark_df = pyspark_df
        self.config_path = config_path
        logger.info("DataQuality object initialized with config_path: %s", config_path)

    def rule_mapping(self, dq_rule):
        logger.debug("Mapping rule: %s", dq_rule)
        return {
            "check_if_not_null": "NotNullExpectation",
            "check_if_unique": "UniqueExpectation",
            "check_if_values_in_list": "ValuesInListExpectation"
        }[dq_rule]

    def _get_expectation(self, rule_name):
        logger.debug("Getting expectation class for rule: %s", rule_name)
        class_obj = globals()[self.rule_mapping(rule_name)]
        return class_obj

    def convert_to_ge_df(self):
        logger.info("Converting PySpark DataFrame to Great Expectations DataFrame")
        return SparkDFDataset(self.pyspark_df)

    def read_config(self):
        logger.info("Reading configuration from path: %s", self.config_path)
        json_reader = JSONFileReader(self.config_path)
        config = json_reader.read()
        logger.debug("Configuration read: %s", config)
        return config

    def run_test(self):
        logger.info("Starting data quality tests")
        ge_df = self.convert_to_ge_df()
        config = self.read_config()

        for column in config["columns"]:
            column_name = column["column_name"]
            logger.info("Processing column: %s", column_name)

            if not column.get("dq_rule(s)"):
                logger.warning("No rules defined for column: %s", column_name)
                continue

            for dq_rule in column["dq_rule(s)"]:
                rule_name = dq_rule["rule_name"]
                logger.info("Applying rule: %s on column: %s", rule_name, column_name)

                expectation_obj = globals()[self.rule_mapping(rule_name)]

                expectation_instance = expectation_obj(
                    column_name,
                    dq_rule.get("rule_dimension"),
                    dq_rule.get("add_info")
                )

                logger.debug(
                    "Created expectation instance: %s with details: %s", 
                    expectation_instance, dq_rule
                )

                expectation_instance.test(ge_df)

        dq_results = ge_df.validate()
        logger.info("Data quality tests completed")
        logger.debug("Validation results: %s", dq_results)
        return dq_results
