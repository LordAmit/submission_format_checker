#!/usr/bin/python

import logging
import time

def setup_logger(name):
    
    filename = time.strftime("%d_%m_%Y") + '.log';
    logging.basicConfig(filename=filename, level=logging.DEBUG)


# def log_this(message):
#     print(message)
#     logging.info(message)



