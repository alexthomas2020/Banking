# Banking Application
# Author: Alex Thomas
# Updated: 11/08/2020

import logging

"""
Banking Application - Logger. This can be invoked from other files.
# ****Log Params Captured*****
# asctime - Human-readable time when the LogRecord was created
# filename - Filename portion of pathname.
# funcName - Name of function containing the logging call.
# lineno - Source line number where the logging call was issued 
# levelname - Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
# message - The logged message, computed as msg % args. 
# Ref: https://docs.python.org/3/library/logging.html
"""


def bank_log(log_file, name):
    logger = name
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s: %(name)s: %(filename)s: %(funcName)s: %(lineno)s: %(levelname)s: %('
                                  'message)s')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


