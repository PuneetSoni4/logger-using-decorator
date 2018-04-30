#!/usr/bin/python
__author__ = "Puneet Soni <puneet.soni111@gmail.com>"

from exception_decorator import exception
from exception_logger import logger

@exception(logger)
def test_3():
    logger.warn('This is in test 2. WARN ERROR')
    1/0
    try:
        #1/0
        raise Exception('Exception Raised in test_3.')
    except Exception as exception:
        logger.critical(exception.message)

@exception(logger)
def main():
    logger.info('This is in test 2.')
    test_3()
 
if __name__ == '__main__':
    main()