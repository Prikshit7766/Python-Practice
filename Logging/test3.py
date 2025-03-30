import logging
logging.basicConfig(filename="test4.log",level=logging.WARNING ,format=' %(levelname)s %(asctime)s %(name)s  %(message)s')
def div(a,b):
    logging.info("the number entered by user %s and %s ",a,b)
    try:
         logging.info("we are into function")
         div= a/b
         logging.info("we have completed a division operation")
         return div
    except Exception as e:
         logging.info(e)
         logging.exception(e)
         return e




print(div(3,1))
print(div(3,0))

