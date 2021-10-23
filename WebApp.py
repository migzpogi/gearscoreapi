import configparser

from flask import Flask, request, render_template
from flask_restplus import Api, Resource
import requests

from gslib.initproperties import InitProperties
from gslib.gsapp import GSApp

gsapp_prop = InitProperties('WebApp.ini')
gsapp = GSApp(gsapp_prop)
app = Flask(__name__)


@app.route("/")
def index():
    config = configparser.ConfigParser()
    config.read('WebApp.ini')
    item_id = request.args.get('item')
    if item_id is None:
        return render_template('home.html', item_id=None, gear_score=None, item_name="Welcome!")
    elif item_id == 'random': # TODO
        return render_template('index.html', item_id=None, gear_score=None, item_name="Random item feature soon!")
    else:
        try:
            r = requests.get(f"http://{config['api']['host']}:{config['api']['port']}/gs/api/v1/{item_id}")
            response = r.json()
            if response.get("gearScore"):
                return render_template('index.html', item_id=item_id, gear_score=response.get("gearScore"), item_name=response.get("name"))
            else:
                return render_template('error.html', item_id=None, gear_score=None, item_name="None")
        except:
            return render_template('error.html', item_id=None, gear_score=None, item_name="None")


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
    def get(self, id):
        return gsapp.get(id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
