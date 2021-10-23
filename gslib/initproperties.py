import configparser
from gslib.gearscore import MongoDBClient
import random


class InitProperties:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.__load_config()

        self.mdb_client = self.__init_mdbclient()
        self.item_ids = self.mdb_client.get_distinct_itemids()

    def __load_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_path)

        return config

    def __init_mdbclient(self):
        mdb_client = MongoDBClient(self.config['mongodb']['host'],
                                   self.config['mongodb']['port'],
                                   self.config['mongodb']['user'],
                                   self.config['mongodb']['pass'],
                                   self.config['mongodb']['authsrc'],
                                   self.config['mongodb']['authmech'])

        return mdb_client

    def get_random_itemid(self):
        return random.choice(self.item_ids)