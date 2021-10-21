import configparser
import unittest

import requests


class TestAPI(unittest.TestCase):

    @staticmethod
    def __load_config():
        config = configparser.ConfigParser()
        config.read('WebApp.ini')

        return config

    def test_correctitemid_status200(self):
        """
        GIVEN correct item id
        WHEN /gs/api/v1/54590 is called
        THEN it returns status 200
        :return:
        """
        config = self.__load_config()
        url = f"http://{config['api']['host']}:{config['api']['port']}/gs/api/v1/54590"
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

    def test_correctitemid_correctresponsebody(self):
        """
        GIVEN correct item id
        WHEN /gs/api/v1/54590 is called
        THEN it returns correct message body
        :return:
        """
        config = self.__load_config()
        url = f"http://{config['api']['host']}:{config['api']['port']}/gs/api/v1/54590"
        r = requests.get(url)

        expected = {
            'itemId': 54590,
            'name': 'Sharpened Twilight Scale',
            'gearScore': 310
        }

        self.assertEqual(r.json(), expected)

    def test_itemidnotindb_returnerr002(self):
        """
        GIVEN item id not in database
        WHEN /gs/api/v1/54590123 is called
        THEN it returns message body with error 002
        :return:
        """
        config = self.__load_config()
        url = f"http://{config['api']['host']}:{config['api']['port']}/gs/api/v1/54590123"
        r = requests.get(url)

        expected = {
                "ErrorCode": "E001",
                "ErrorMessage": "Item ID not in database."
            }

        self.assertEqual(r.json(), expected)

    def test_itemidnotvalid_return4042(self):
        """
        GIVEN item id not valid
        WHEN /gs/api/v1/asdfg is called
        THEN it returns message 404
        :return:
        """
        config = self.__load_config()
        url = f"http://{config['api']['host']}:{config['api']['port']}/gs/api/v1/asdfg"
        r = requests.get(url)

        self.assertEqual(r.status_code, 404)


if __name__ == '__main__':
    unittest.main()