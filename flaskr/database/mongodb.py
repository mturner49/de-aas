from pymongo import MongoClient


class Mongo:
    def __init__(self, conn_str: str):
        self.conn_str = conn_str


    def connect(self):
        """Connect to the MongoDB instance"""
        client = MongoClient(self.conn_str)
        return client
    

    def create_database(
        self,
        db_name: str,
        coll_name: str,
        payload: dict) -> None:
        """Create a new database in MongoDB"""
        db_client = self.connect()

        db = db_client[db_name]
        coll = db[coll_name]
        coll.insert_many(payload)

        print(coll)