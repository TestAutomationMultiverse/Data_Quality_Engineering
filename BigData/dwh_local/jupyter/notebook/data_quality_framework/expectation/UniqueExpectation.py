import logging
from expectation.Expectation import Expectation

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set to DEBUG for more detailed logs
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class UniqueExpectation(Expectation):
    def __init__(self, column, dimension, add_info={}):
        super().__init__(column, dimension, add_info)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("UniqueExpectation initialized with column: '%s', dimension: '%s', and additional info: %s", column, dimension, add_info)

    def test(self, ge_df):
        self.logger.info("Starting test for column: '%s' with dimension: '%s'", self.column, self.dimension)
        try:
            result = ge_df.expect_column_values_to_be_unique(column=self.column, meta={"dimension": self.dimension})
            self.logger.info("Test completed successfully for column: '%s'. Result: %s", self.column, result)
            return result
        except Exception as e:
            self.logger.error("An error occurred while testing column: '%s'. Error: %s", self.column, e, exc_info=True)
            raise
