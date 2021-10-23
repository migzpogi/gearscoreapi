from flask import Response
import json


class GSApp:
    def __init__(self, gsapp_prop):
        self.gsapp_prop = gsapp_prop
        self.mdb_client = self.gsapp_prop.mdb_client

    def __create_response_object(self, body):
        response_object = Response(
            response=json.dumps(body),
            mimetype='application/json'
        )
        response_object.headers['Trace'] = '001'
        return response_object

    def get(self, id):
        """
        GET
        :param id:
        :return:
        """

        # print(self.mdb_client.get_random_itemid())

        mdb_response = self.mdb_client.get_item_details(id)

        if mdb_response:
            body = {
                "gearScore": mdb_response['gearScore'],
                'itemId': mdb_response['itemID'],
                'name': mdb_response['name']
            }
            return self.__create_response_object(body)
        else:
            body = {
                "ErrorCode": "E001",
                "ErrorMessage": "Item ID not in database."
            }
            return self.__create_response_object(body)