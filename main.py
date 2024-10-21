from flask import Flask
from classes.database import Database
from flask import Flask, request, jsonify
from models.login import login

app = Flask(__name__)
database = Database(user="root", password="", host="3306", database="db_trabalho")


@app.route('/', methods=["GET"])
def xd():
    return jsonify(login("xd", "XD"))

@app.route('/colab', methods=["POST"])
def insertColaborador():
    json = request.get_json()
    database.insertDatabase(table="tbl_colaborador", fields="nome, email, cpf, telefone", values=f"{json.nome}, {json.email}, {json.cpf}, {json.telefone}")



if __name__ == '__main__':
    app.run(debug=True)
