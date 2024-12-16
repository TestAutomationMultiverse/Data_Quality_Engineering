import logging
from expectation.Expectation import Expectation

logger = logging.getLogger(__name__)

class NotNullExpectation(Expectation):
    def __init__(self, column, dimension, add_info = {}):
        super().__init__(column, dimension, add_info)
        logger.debug(f"Created NotNullExpectation for column '{self.column}'")

    def test(self, ge_df):
        logger.info(f"Testing NotNullExpectation for column '{self.column}'")
        try:
            ge_df.expect_column_values_to_not_be_null(column=self.column, meta = {"dimension": self.dimension})
            logger.info(f"NotNullExpectation passed for column '{self.column}'")
        except Exception as e:
            logger.error(f"NotNullExpectation failed for column '{self.column}'. Error: {e}")
            raise