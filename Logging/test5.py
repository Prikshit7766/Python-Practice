import logging
logging.basicConfig(filename="test5.log", level=logging.DEBUG,format=' %(levelname)s %(asctime)s %(name)s  %(message)s')
try:
    with open("sudh.txt","r"):
        logging.info("i am read a file")
        logging.info("sucessfully it has read the file")
except Exception as e:
    logging.critical("this is a situation for us")
    logging.error(e)
    logging.exception(e)
