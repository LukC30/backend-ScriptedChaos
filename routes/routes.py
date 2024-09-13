from flask import Flask, request, jsonify
from models.login import login


app = Flask(__name__)
@app.route('/', methods=["GET"])
def xd():
    return login("oi", "viado")

if __name__ == '__main__':
    app.run(debug=True)