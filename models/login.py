from flask import jsonify

def login(username, password):
    return jsonify({"userName" : username,
                    "password" : password
                    })
