from flask import Flask
from flask_restful import Api, Resource, reqparse
import sqlite3

app = Flask(__name__)
api = Api(app)

connect = sqlite3.connect('Api.db', check_same_thread=False)
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS 
            users(
               name TEXT,
               gmail TEXT 
            )""")
connect.commit()

class User(Resource):
    def get(self):
        cursor.execute("SELECT name FROM users")
        names = cursor.fetchall()
        for name in names:
            return name[0]
        
class Name_gmail(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        name = parser.add_argument("name", type=str)
        gmail = parser.add_argument("gmail", type=str)
        cursor.execute("INSERT INTO users(name, gmail) VALUES(?, ?);", (name, gmail))
        connect.commit()

api.add_resource(User, "/api/user")
api.add_resource(Name_gmail, "/api/users/<string:name>/<string:gmail>")

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
