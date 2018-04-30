#!/usr/bin/python
__author__ = "Puneet Soni <puneet.soni111@gmail.com>"

from exception_decorator import exception
from exception_logger import logger
 
@exception(logger)
def zero_divide():
    1 / 0
 
if __name__ == '__main__':
    zero_divide()