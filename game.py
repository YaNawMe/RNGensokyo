import sqlite3
import requests
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class SQL():
    connection = sqlite3.connect('UserDatabase.db', check_same_thread=False)

    @classmethod
    def get_data(cls) -> list[tuple]:
        sql_command = """SELECT * FROM User"""
        data = cls.connection.execute(sql_command)
        
        print(data.fetchall())

        return data.fetchall()

    @classmethod
    def insert_data(cls, username, password):
        sql_command = """INSERT INTO User(Username, Password) VALUES (:name, :pass)"""
        cls.connection.execute(sql_command, {"name": username, "pass": password})
        cls.connection.commit()
    
    @classmethod
    def replace_data(cls, id, username, password):
        sql_command = """REPLACE INTO User(Username, Password) VALUES(:name, :pass) WHERE ID = :id"""
        cls.connection.execute(sql_command, {"id": id, "name": username, "pass": password})
        cls.connection.commit()
    
    @classmethod
    def delete_data(cls, *ids, **kwargs):
        if "delete_all" in kwargs:
            if kwargs["delete_all"]:
                sql_command = """DELETE FROM User"""
                cls.connection.execute(sql_command)
                cls.connection.commit()
        
        else:
            for id in ids:
                sql_command = """DELETE FROM User WHERE ID = :id"""
                cls.connection.execute(sql_command, {"id": id})
                cls.connection.commit()
        
class Login(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()

            parser.add_argument('Username', required=True, location="args")
            parser.add_argument('Password', required=True, location="args")

            args = parser.parse_args()

            SQL.insert_data(args["Username"], args["Password"])

            return {"message": "Registered successfully!"}, 200
        
        except Exception as ex:
            return {"error": ex}, 500
        
api.add_resource(Login, "/login")

if __name__ == '__main__':
    app.run()