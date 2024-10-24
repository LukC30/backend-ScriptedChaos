import mysql.connector
from flask import jsonify
import mysql.connector.cursor


class Database():
    xd = None

    def __init__(self, user, password, host, database):
        try:
            self.xd = mysql.connector.connect(host = host, user= user, password = password, database = database)
            print("===Connected on database===")
        except Exception as e:
            return print(f"Erro: {e}")
        return 
    
    def Cursor(self):
        return self.xd.cursor()
    def Execute(self, command):
        return self.Cursor().execute(command)
    def FetchAll(self):
        return self.Cursor().fetchall()
    def Close(self):
        return self.Cursor().close()
    def Commit(self):
        return self.xd.commit()


    def Build_Sql_command(self, fields, table, values):
        self.command = f"Insert into {table}({fields}) values({values})"
        return self.command
    def Build_Sql_command(self, fields, table, values):
        return    
    def insertDatabase(self, fields, table, values, runTime=1):
        try:
            self.Execute(self.Build_Sql_command(fields, table, values))
            self.Commit()
        except Exception as e:
            return print(f"Erro no cadastro: {e}")
        return print(f"cadastro feito com sucesso, {str(runTime)} cadastros feitos")
    
    def getUsers(self):

        return