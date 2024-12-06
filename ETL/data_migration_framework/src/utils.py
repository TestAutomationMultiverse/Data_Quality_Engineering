from loguru import logger

logger.add("logs/framework.log", rotation="1 MB")

def log(message):
    logger.info(message)
