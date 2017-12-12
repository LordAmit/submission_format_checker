#!/usr/bin/python

import logging
import time

def setup_logger(name):

    formatter = logging.Formatter(fmt='%(levelname)s - %(module)s - %(funcName)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger



# def log_this(message):
#     print(message)
#     logging.info(message)



