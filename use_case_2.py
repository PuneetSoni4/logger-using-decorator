#!/usr/bin/python
__author__ = "Puneet Soni <puneet.soni111@gmail.com>"

from exception_decorator import exception
from exception_logger import logger

@exception(logger)
def main():
    logger.info('This is in test 2.')
 
if __name__ == '__main__':
    main()