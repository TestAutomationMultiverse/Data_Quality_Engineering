import logging
from expectation.Expectation import Expectation

logger = logging.getLogger(__name__)

class ValuesInListExpectation(Expectation):
    def __init__(self, column, dimension, add_info = {}):
        super().__init__(column, dimension, add_info)
        logger.debug(f"Created ValuesInListExpectation for column '{self.column}' with value_set: {self.add_info.get('value_set', 'N/A')}")

    def test(self, ge_df):
        logger.info(f"Testing ValuesInListExpectation for column '{self.column}'")
        try:
            ge_df.expect_column_values_to_be_in_set(column=self.column, value_set=self.add_info["value_set"], meta = {"dimension": self.dimension})
            logger.info(f"ValuesInListExpectation passed for column '{self.column}'")
        except Exception as e:
            logger.error(f"ValuesInListExpectation failed for column '{self.column}'. Error: {e}")
            raise