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
        all_users = [{"name": i[0]} for i in names]
        return all_users
        
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

class RenderGmail(Resource):
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int, required=True)
        parser.add_argument("name", type=str)
        parser.add_argument("gmail", type=str)
        args = parser.parse_args()
        user_id = args["id"]
        name = args.get("name")
        gmail = args.get("gmail")

        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        data = cursor.fetchone()
        if data:
            if name:
                cursor.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
            if gmail:
                cursor.execute("UPDATE users SET gmail = ? WHERE id = ?", (gmail, user_id))
            connect.commit()
            return {"message": "Данные пользователя обновлены"}, 200
        else:
            return {"message": "Пользователь не найден"}, 404
        

class DeletDmail(Resource):
    def delet(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int, required=True)
        args = parser.parse_args()
        user_id = args["id"]
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        data = cursor.fetchone()
        if data:
            cursor.execute(f"DELETE FROM users WHERE id = ?{user_id}")
            connect.commit()
            return {'message':"Пользователь удален"}
        else:
            return{'message':"Ошибка"}

api.add_resource(User, "/api/user")
api.add_resource(Name_gmail, "/api/users")
api.add_resource(RenderGmail, '/api/render')
api.add_resource(DeletDmail, '/api/del')


if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
