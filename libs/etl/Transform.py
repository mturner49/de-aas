'''
__author__ = 'Matt Turner'
__purpose__ = 'Perform transformations & operations on datasets'

'''

import os, sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from libs.DBConnection import DBConnection


class Transform():
    def __init__(self, src, database, schema):
        self.src = src
        self.database = database
        self.schema = schema
        self.sf = DBConnection(self.src, self.database, self.schema)

        self.db = self.sf.db

    
    def manual_sql(self, query):
        cur = self.db.cursor()
        df = cur.execute(query).fetch_pandas_all()

        return df


    def get_count(self):
        cur = self.db.cursor()
        total = cur.execute(f'SELECT count(*) from {self.database}.DWADMIN.{self.schema};').fetchone()[0]
        cur.close()

        print(total)