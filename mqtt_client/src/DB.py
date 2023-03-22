from pymongo import MongoClient
from os import getenv
from datetime import datetime
import logging


class DB:
    def __init__(self) -> None:
        host = getenv("DB_HOST")
        port = int(getenv("DB_PORT"))
        user = getenv("DB_USER")
        password = getenv("DB_PASSWORD")
        db_name = getenv("DB_NAME")
        self.client = MongoClient(
            host=host, port=port, username=user, password=password)

        try:
            self.client.admin.command('ping')
            self.db = self.client[db_name]
            logging.debug("DB => Connexió correcte!")
        except Exception as e:
            print(f"DB ERROR => {e}")
            exit()

    def insert(self, collection, document) -> int:
        format = "%Y/%m/%d %H:%M:%S"
        document['created_at'] = datetime.now().strftime(format)
        document['updated_at'] = datetime.now().strftime(format)
        collection = self.db[collection]
        return collection.insert_one(document=document).inserted_id
