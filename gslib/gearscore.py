import pymongo


class MongoDBClient:
    def __init__(self, host, port, username, password, authSource, authMechanism):
        self.host = host
        self.port = int(port)
        self.username = username
        self.password = password
        self.authSource = authSource
        self.authMechanism = authMechanism

        self.client = self.__create_client()
        self.database = None
        self.collection = None

    def __create_client(self):
        """
        Creates the MongoDB client
        :return:
        """

        mdbclient = pymongo.MongoClient(host=self.host, port=self.port, username=self.username, password=self.password,
                                     authsource=self.authSource, authMechanism=self.authMechanism)
        return mdbclient

    def get_item_details(self, item_id):
        """
        Queries the database for the given item
        :param item_id:
        :return:
        """

        db = self.client['warmane']
        col = db['items']

        query = {
            "itemID": int(item_id)
        }

        result = col.find_one(query)

        if result:
            response = {
                        'itemID': result['itemID'],
                        'name': result['name'],
                        'gearScore': result['GearScore']
                    }
        else:
            response = None

        return response


def foo():
    return True