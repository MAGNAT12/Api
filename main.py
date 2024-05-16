from flask import Flask
from flask_restful import Api, Resource, reqparse
import sqlite3

app = Flask(__name__)
api = Api(app)

connect = sqlite3.connect('Api.db', check_same_thread=False)
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS 
            users(
               id INTEGER PRIMARY KEY,
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
        parser.add_argument("name", type=str)
        parser.add_argument("gmail", type=str)
        args = parser.parse_args()
        name = args["name"]
        gmail = args["gmail"]
        cursor.execute(f"SELECT `name`, `gmail` FROM `users` WHERE `name` = '{name}' AND `gmail` = '{gmail}' ")
        data = cursor.fetchone()
        if data is None:
            name = args["name"]
            gmail = args["gmail"]
            cursor.execute("INSERT INTO users(name, gmail) VALUES(?, ?);", (name, gmail))
            connect.commit()
            return {'message':'Вы зарегистрированны'}  # Возвращаем пустой словарь в случае отсутствия данных
        else:
            return {'message':'Вы уже зарегистрированны'}

class Render_gmail(Resource):
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str)
        parser.add_argument("gmail", type=str)
        args = parser.parse_args()
        name = args["name"]
        gmail = args["gmail"]
        cursor.execute(f"SELECT `name`, `gmail` FROM `users` WHERE `name` = '{name}'")
        data = cursor.fetchone()
        if data is None:
            name = args["name"]
            gmail = args["gmail"]
            cursor.execute(f"UPDATE users SET name = ?,gmail = ? WHERE id = ? {name, gmail}")
            connect.commit()
            return {'message':'Вы изменино'}  # Возвращаем пустой словарь в случае отсутствия данных
        else:
            return {'message':'Вы не изменино'}
        
        
api.add_resource(User, "/api/user")
api.add_resource(Name_gmail, "/api/users")
api.add_resource(Render_gmail, '/api/render')

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
