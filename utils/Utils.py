'''
__author__ = 'Matt Turner'
__purpose__ = 'Small utility functions to call throughout app'

'''

import logging
import yaml

def get_logger():
    FORMAT = '%(asctime)s - %(funcName)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    logger = logging.getLogger(__name__)
    return logger


def get_config(file_name):
    with open(file_name, 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg
