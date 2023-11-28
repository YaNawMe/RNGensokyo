import sqlite3
import requests

from game_database import SQLLogin
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Login(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()

            parser.add_argument('user', required=True, location="args")
            parser.add_argument('pass', required=True, location="args")

            args = parser.parse_args()

            database = SQLLogin.get_data()

            for data in database:
                if (args["user"], args["pass"]) == (data[1], data[2]):
                    return {"message": "Registered successfully!", "ID": data[0]}, 200
            
            return {"message": "Username or Password is incorrect."}, 400

        except Exception as ex:
            return {"error": str(ex)}, 500

class Register(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()

            parser.add_argument('user', required=True, location="args")
            parser.add_argument('pass', required=True, location="args")

            args = parser.parse_args()

            if len(args["user"]) > 32:
                return {"message": "Username cannot be more than 32 characters."}, 400
            
            elif len(args["pass"]) > 32:
                return {"message": "Password cannot be more than 32 characters."}, 400

            SQLLogin.insert_data(args["user"], args["pass"])

            return {"message": "Registered successfully!"}, 200
        
        except Exception as ex:
            return {"error": str(ex)}, 500


api.add_resource(Register, "/register")
api.add_resource(Login, "/login")

if __name__ == '__main__':
    app.run(debug=True)