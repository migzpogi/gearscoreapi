from flask import Flask, request, jsonify, Response, render_template
from flask_restplus import Api, Resource
from gslib.gearscore import MongoDBClient
import configparser
import requests

import json

app = Flask(__name__)


@app.route("/")
def index():
    item_id = request.args.get('item')
    if item_id is None:
        return render_template('index.html', item_id=None, gear_score=None, item_name="Welcome!")
    elif item_id == 'random':
        return render_template('index.html', item_id=None, gear_score=None, item_name="Random item feature soon!")
    else:
        try:
            r = requests.get(f"http://host/gs/api/v1/{item_id}")
            response = r.json()
            if response.get("gearScore"):
                return render_template('index.html', item_id=item_id, gear_score=response.get("gearScore"), item_name=response.get("name"))
            else:
                return render_template('index.html', item_id=None, gear_score=None, item_name="Wrong item number!")
        except:
            return render_template('index.html', item_id=None, gear_score=None, item_name="Some error")



api = Api(
    app=app,
    version='1.0',
    description='TEST API',
    doc='/swagger/',
    default='default',
    default_label='Swagger'
)


@api.route("/gs/api/v1/<int:id>")
class GearScore(Resource):
    def __create_response_object(self, body):
        response_object = Response(
            response=json.dumps(body),
            mimetype='application/json'
        )
        response_object.headers['Trace'] = '001'
        return response_object

    def get(self, id):
        config = configparser.ConfigParser()
        config.read('WebApp.ini')

        mdb_client = MongoDBClient(config['mongodb']['host'],
                                   config['mongodb']['port'],
                                   config['mongodb']['user'],
                                   config['mongodb']['pass'],
                                   config['mongodb']['authsrc'],
                                   config['mongodb']['authmech'])

        mdb_response = mdb_client.get_item_details(id)

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
