from db import get_top_10, get_one_country
import json



from meinheld import patch

patch.patch_all()

from bottle import Bottle


app = Bottle()


@app.route("/")
def index():
    top_10 = json.dumps(get_top_10())
    return top_10


@app.route("/user/<id:int>")
def user_info(id):
    one_c = json.dumps(get_one_country(id_=id))
    return one_c

