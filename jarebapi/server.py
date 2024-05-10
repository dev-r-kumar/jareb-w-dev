from flask import Flask, request, url_for, redirect, jsonify, render_template
import LightContextHandler
from flask_cors import CORS
import requests

app = Flask(__name__, template_folder=".")
CORS(app)

@app.route("/")
def index():
    return ""

@app.route("/chat")
def chat():
    try:
        query = request.args.get("u")
        res = LightContextHandler.nanoQueryEnhance(query)
        return jsonify({"res": res})
    except requests.exceptions.ConnectionError as e:
        return render_template('webexception.html')


if __name__ == "__main__":
    app.run(host=('192.168.1.133'), port=("5555"), debug=True)

