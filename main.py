from flask import Flask
from classes.database import Database
from flask import Flask, request, jsonify
from models.login import login

app = Flask(__name__)
database = Database(user="root", password="admin", host="localhost", database="db_trabalho")


@app.route('/', methods=["GET"])
def xd():
    return jsonify({"xd" : "XD"})

@app.route('/colab', methods=["POST"])
def insertColaborador():
    json = request.get_json()
    database.insertDatabase(table="tbl_colaborador", fields="nome, email, cpf, telefone", values=f"'{json['nome']}', '{json['email']}', '{json["cpf"]}', '{json['telefone']}'")
    return jsonify({"message" : "Cadastro feito com sucesso"}), 200

@app.route('/users', methods=['GET'])
def getUsers():
    database.getUsers()
    return jsonify({"message" : "Cadastro feito com sucesso"}), 200


if __name__ == '__main__':
    app.run(debug=True)
