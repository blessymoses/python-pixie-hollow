from flask import Flask, request, jsonify
from models import Schema
from service import CategoryService

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers[
        "Access-Control-Allow-Headers"
    ] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):
    return f"Hello {name}"


@app.route("/category", methods=["GET"])
def list_todo():
    return jsonify(CategoryService().list())


@app.route("/category/<item_id>", methods=["PUT"])
def update_item(item_id):
    return jsonify(CategoryService().update(item_id, request.get_json()))


@app.route("/category/<item_id>", methods=["GET"])
def get_item(item_id):
    return jsonify(CategoryService().get_by_id(item_id))


if __name__ == "__main__":
    Schema()
    app.run(debug=True, host="0.0.0.0", port=8888)
