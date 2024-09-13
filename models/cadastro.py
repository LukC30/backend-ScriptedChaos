from flask import jsonify

def cadastro(username, password):
    return jsonify({
        'userName' : username,
        'password' : password
    })
    

    