# code for logging
import logging
logging.basicConfig(filename="test.log",level=logging.INFO )
logging.info("this is my first code for logging")
logging.warning("this will try to load the warning ")
logging.error("this is ther error message")
l=[1,2,3,4,5,6.7]
for i in l:
    if i==2:
        logging.info(l)
        logging.warning("this is the warning for user that they have 2 list")

logging.shutdown()