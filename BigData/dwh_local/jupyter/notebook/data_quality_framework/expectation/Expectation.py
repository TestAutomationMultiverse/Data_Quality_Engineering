import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class Expectation(ABC):
    def __init__(self, column, dimension, add_info = {}):
        self.column = column  # column on which the expectation rule will be applied
        self.dimension = dimension # category of the data quality which can be Completeness, Uniqueness, Validity, Accuracy, and Consistency
        self.add_info = add_info
        logger.debug(f"Created Expectation for column '{self.column}' and dimension '{self.dimension}'")

    @abstractmethod
    def test(self, ge_df):
        logger.info(f"Testing expectation for column '{self.column}' and dimension '{self.dimension}'")
        pass