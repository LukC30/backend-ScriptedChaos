from flask import Flask

from flask import Flask, request, jsonify
from models.login import login



app = Flask(__name__)
@app.route('/', methods=["GET"])
def xd():
    return jsonify(login("xd", "XD"))

if __name__ == '__main__':
    app.run(debug=True)