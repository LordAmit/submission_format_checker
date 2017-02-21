#!/usr/bin/python3
import sys
import os
import log


logger = log.setup_logger('root')
logger.debug('main message')



def check_zip():

    logger.debug('')

if __name__ == "__main__":
    import config_reader
    if len(sys.argv) >= 2:
        working_directory = sys.argv[1]
        if not(os.path.isdir(working_directory)):
            message = "Problem: "+working_directory+" not found."
            logger.debug(message)
            exit(1)
        else:
            message = 'Working directory: ' + working_directory + 'found'
            logger.debug(message)
            check_zip()