import logging

logger  =  logging.getLogger(__name__) # this will create a logger with the name of logger module  which is logging2 in this case
logger.propagate = False  # now it will not propogate to base loger
logger.info("hello how are you")