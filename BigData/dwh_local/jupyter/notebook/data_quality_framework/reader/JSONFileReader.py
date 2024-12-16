import logging
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set to DEBUG for more detailed logs
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class JSONFileReader:
    def __init__(self, filename):
        self.filename = filename
        logger = logging.getLogger(__name__)
        logger.debug(f"Created JSONFileReader for file: {self.filename}")

    def read(self):
        logger = logging.getLogger(__name__)
        try:
            logger.info(f"Reading JSON data from file: {self.filename}")
            with open(self.filename) as f:
                return json.load(f)
        except FileNotFoundError as e:
            logger.error(f"File not found: {self.filename}. Error: {e}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON data from file: {self.filename}. Error: {e}")
            raise