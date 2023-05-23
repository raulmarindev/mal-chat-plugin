import json

import quart
import quart_cors
from quart import request

app = quart_cors.cors(quart.Quart(__name__),
                      allow_origin="https://chat.openai.com")


@app.get("/anime/<string:anime_name>")
async def get_anime(anime_name):
    return quart.Response(response=json.dumps({"anime_name": anime_name}), status=200)

@app.get("/manga/<string:manga_name>")
async def get_manga(manga_name):
    return quart.Response(response=json.dumps({"manga_name": manga_name}), status=200)


@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")


@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")


def main():
    app.run(debug=True, host="0.0.0.0", port=5003)


if __name__ == "__main__":
    main()