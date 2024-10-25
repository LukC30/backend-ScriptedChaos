import mysql.connector
from flask import jsonify
class Database():
    def __init__(self, user, password, host, database):
        try:
            self.xd = mysql.connector.connect(host=host, user=user, password=password, database=database)
            self.cursor = self.xd.cursor()
            print("=== Conectado ao banco de dados ===")
        except Exception as e:
            print(f"Erro: {e}")
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.xd:
            self.xd.close()

    def commit(self):
        self.xd.commit()
        
    def Build_Sql_command_Insert(self, fields, table, values):
        self.command = f"Insert into {table}({fields}) values({values})"
        return self.command

    def insertDatabase(self, fields, table, values, runTime=1):
        try:
            self.cursor.execute(self.Build_Sql_command_Insert(fields, table, values))
            self.commit()
        except Exception as e:
            return jsonify({"message" : f"error:{e}"})       

    def get_users(self):
        try:
            self.cursor.execute("SELECT * FROM tbl_colaborador")
            users = self.cursor.fetchall()  # Consome todos os resultados
            return users
        except Exception as e:
            print(f"Erro ao buscar usuários: {e}")
