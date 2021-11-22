'''
__author__ = 'Matt Turner'
__purpose__ = 'Establish connection to various data sources'
__current_sources__ = 
    - Snowflake

'''

import snowflake.connector
import yaml
import sys, os
import pymongo

from pymongo import MongoClient

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from utils.Utils import get_logger, get_config



class DBConnection():
    def __init__(self, src, db, schema, charset='utf-8'):
        config = get_config('/Users/matt.turner/Documents/git/de-as-a-service/config/db-connection.yaml')
        print(config)
        self.charset = charset
        self.logger = get_logger()
        self.db_info = {}

        if src.upper() == 'SNOWFLAKE':
            self.db_type = 'SNOWFLAKE'
            self.db_info['account'] = config['snow']['account']
            self.db_info['user'] = config['snow']['user']
            self.db_info['password'] = config['snow']['password']
            self.db_info['warehouse'] = config['snow']['warehouse']
            self.db_info['role'] = config['snow']['role']
            self.db_info['database'] = db
            self.db_info['schema'] = schema
        
        if src.upper() == 'MONGODB':
            self.db_type = 'MONGO'
            self.db_info['user'] = config['mongo']['user']
            self.db_info['passowrd'] = config['mongo']['password']
            self.db_info['host'] = config['mongo']['host']
            self.db_info['port'] = config['mongo']['port']

        self.connect()

    
    def connect_snowflake(self):
        try:
            self.db = snowflake.connector.connect(**self.db_info)
        except snowflake.connector.Error as err:
            self.logger.error(
                f"Error connecting to snowflake account: {err}"
            )
            self.logger.error(err)
            exit(1)

    
    def connect_mongo(self):
        try:
            self.db = MongoClient(f"mongodb://{self.db_info['user']}:{self.db_info['password']}@{self.db_info['host']}:{self.db_info['port']}")
        except pymongo.errors.ConnectionFailure as err:
            self.logger(f'Unable to establish connection to MongoDB host: {err}')
            self.logger.error(err)
            exit(1)


    def connect(self):
        if self.db_type == 'SNOWFLAKE':
            self.connect_snowflake()
        elif self.db_type == 'MONGO':
            self.connect_mongo()
        else:
            self.logger.error(f'Database connection of type "{self.db_type}" was not found')
            exit(1)
