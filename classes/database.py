import mysql.connector


class Database:
    def __init__(self, user, password, host, database):
        db_config = {
            self.user : user,
            self.password : password,
            self.host : host,
            self.database : database
        }
    
        db = mysql.connector.connect(db_config)




