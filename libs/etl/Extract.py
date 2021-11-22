'''
__author__ = 'Matt Turner'
__purpose__ = 'Extract data from desired sources'

'''

import os, sys
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from libs.DBConnection import DBConnection
from utils.Utils import get_logger

class Extract():
    def __init__(self, src, database, schema):
        self.src = src
        self.database = database
        self.schema = schema
        self.logger = get_logger()

        self.sf = DBConnection(self.src, self.database, self.schema)

        self.db_info = self.sf.db_info


    # read data from table via query
    def read_data_into_df(self, sql, **kwargs):
        try:
            df = pd.read_sql(sql, con=self.db_info, **kwargs)
        except Exception as e:
            self.logger.error(e)
            exit(1)
        return df

    # read dataframe into csv
    def write_to_csv(self, df, file_name, **kwargs):
        try:
            df.to_csv(file_name, mode="a", header=False, index=False, **kwargs)
        except Exception as e:
            self.logger.error(e)
            exit(1)



