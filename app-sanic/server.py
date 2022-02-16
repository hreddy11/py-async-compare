from sanic import Sanic
from sanic.response import text
from sanic.response import json
from db import get_top_10, get_one_country

# print(get_one_country(243))


app = Sanic("MyHelloWorldApp")


@app.get("/")
async def hello_world(request):
    top_10 = get_top_10()
    return json(top_10)

@app.route('/<tag>')
async def tag_handler(request, tag):
    one_c = get_one_country(tag)
    return json(one_c)

