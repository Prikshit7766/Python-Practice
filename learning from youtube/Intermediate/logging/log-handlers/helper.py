import logging

# Create a logger
logger = logging.getLogger(__name__)


# Create a stream handler and set the level to WARNING
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)

# Create a file handler and set the level to ERROR
file_handler = logging.FileHandler('myapp.log')
file_handler.setLevel(logging.ERROR)

# Define a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

# Set the formatter for both handlers
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# Log messages
logger.warning('This is a warning message.')
logger.error('This is an error message.')
