from flask import Flask

from db import get_top_10, get_one_country
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    top_10 = json.dumps(get_top_10())
    return top_10

@app.route("/<id>")
def hello_world_one(id):
    one_c = json.dumps(get_one_country(id_=id))
    return one_c

