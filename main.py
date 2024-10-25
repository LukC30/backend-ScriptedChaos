from flask import Flask
from classes.database import Database
from flask import Flask, request, jsonify
from models.login import login

app = Flask(__name__)
# database = Database(user="root", password="admin", host="localhost", database="db_trabalho")
database = Database(user="root", password="", host="localhost", database="db_trabalho")

@app.route('/', methods=["GET"])
def xd():
    return jsonify({"xd" : "XD"})

@app.route('/colab', methods=["POST"])
def insertColaborador():
    json = request.get_json()
    if 'nome' not in json:
       return jsonify({"message" : "Nome não incluido no cadastro"})
    if 'email' not in json:
       return jsonify({"message" : "Email não incluido no cadastro"})
    if 'cpf' not in json:
       return jsonify({"message" : "Cpf não incluido no cadastro"})
    if 'telefone' not in json:
       return jsonify({"message" : "Telefone não incluido no cadastro"})
    
    database.insertDatabase(table="tbl_colaborador", fields="nome, email, cpf, telefone", values=f"'{json['nome']}', '{json['email']}', '{json["cpf"]}', '{json['telefone']}'")
    return jsonify({"message" : "Cadastro feito com sucesso"}), 200

@app.route('/users', methods=['GET'])
def getUsers():
    user = ""
    try:
        user = database.get_users()
        jsonify({"message" : f"Usuarios exibidos com sucesso\n{len(user)}"}), 200
        return user
    except Exception as e:
        return jsonify({"message" : f"Um erro ocorreu: {e}, {type(user)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
