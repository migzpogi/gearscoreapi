import unittest
from gslib.gearscore import MongoDBClient, foo
import configparser


class TestMongoClient(unittest.TestCase):

    def __load_config(self):
        config = configparser.ConfigParser()
        config.read('WebApp.ini')

        return config

    def __load_mdbclient(self):
        config = self.__load_config()
        mdb_client = MongoDBClient(config['mongodb']['host'],
                                   config['mongodb']['port'],
                                   config['mongodb']['user'],
                                   config['mongodb']['pass'],
                                   config['mongodb']['authsrc'],
                                   config['mongodb']['authmech'])

        return mdb_client

    def test_foobar(self):
        self.assertTrue(foo())

    def test_uwsgiconfig(self):
        config = self.__load_config()
        self.assertTrue(config["uwsgi"]["master"])

    def test_correctitemid(self):
        """
        GIVEN correct item id
        WHEN get_item_details() is called
        THEN it returns correct item information
        :return:
        """
        mdb_client = self.__load_mdbclient()
        mdb_response = mdb_client.get_item_details(54590)

        expected = {
                    'itemID': 54590,
                    'name': 'Sharpened Twilight Scale',
                    'gearScore': 310
                }

        self.assertEqual(expected, mdb_response)

    def test_itemidnotfound(self):
        """
        GIVEN item id is not in database
        WHEN get_item_details() is called
        THEN it returns None
        :return:
        """
        mdb_client = self.__load_mdbclient()
        mdb_response = mdb_client.get_item_details(54590123)

        expected = None

        self.assertEqual(expected, mdb_response)


if __name__ == '__main__':
    unittest.main()