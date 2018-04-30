#!/usr/bin/python
__author__ = "Puneet Soni <puneet.soni111@gmail.com>"

import logging
 
def create_logger():
    """
    Creates a logging object and returns it
    """
    logger = logging.getLogger("my_logger_name")
    logger.setLevel(logging.DEBUG)
 
    # create the logging file handler
    file_handler = logging.FileHandler(r"path_to_log_file\sample_output_file.log")
 
    log_format = '%(asctime)s [%(levelname)s] %(funcName)s: %(message)s'
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)
 
    # add handler to logger object
    logger.addHandler(file_handler)
    return logger
 
logger = create_logger()