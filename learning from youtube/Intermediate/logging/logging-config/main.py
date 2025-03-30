import logging
import logging.config

logging.config.fileConfig("logging.conf")

# logging.config.dictConfig("logging.conf")  # for dictionary
# Create a logger
logger = logging.getLogger("simpleExample")

logger.debug('This is a warning message.')

