import sqlite3
import requests
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
        
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