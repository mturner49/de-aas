import os, sys
import boto3

from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
from io import BytesIO


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from libs.DBConnection import DBConnection
from utils.Utils import get_logger


class Load():

    def __init__(self, src, target, database, schema):
        self.s3_client = boto3.client('s3')
        self.s3_resource = boto3.resource('s3')
        
        self.logger = get_logger()
        self.src = src
        self.target = target
        self.database = database
        self.schema = schema

        self.db = DBConnection(self.src, self.database, self.schema)
        self.db_info = self.db.db_info


    def write_to_table(self, df, table_name, **kwargs):
        target_url = None
        if self.target == "SNOWFLAKE":
            target_url = URL(**self.db_info)

        db_connection = create_engine(target_url)
        try:
            self.logger.info(f"Writing to {self.database} and table: {table_name}")
            df.to_sql(name=table_name, con=db_connection, if_exists="append", index=False, **kwargs)
        except Exception as e:
            self.logger.error(e)
            exit(1)
    

    def write_csv_to_s3(self, bucket_name, blob_name, df, header=True, compression='gzip', sep='|', index=False):
        csv_buffer = BytesIO()
        df.to_csv(
            csv_buffer,
            header=header,
            compression=compression,
            sep=sep,
            index=index
        )
        csv_buffer.seek(0)
        self.s3_resource.Object(bucket_name, blob_name).put(Body=csv_buffer.getvalue())