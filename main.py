from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

library = {1: {'name': 'Python', 'base': 145},
           2: {'name': 'JS', 'base': 335}}

parser = reqparse.RequestParser()
parser.add_argument('name',type=str)
parser.add_argument('base',type=int)


class Main(Resource):

    def get(self, lib_id):
        if lib_id == 0:
            return library
        else:
            return library[lib_id]

    def delete(self, lib_id):
        del library[lib_id]
        return library

    def post(self, lib_id):
        library[lib_id] = parser.parse_args()
        return library

    def put(self, lib_id):
        library[lib_id] = parser.parse_args()
        return library


api.add_resource(Main, '/api/library/<int:lib_id>')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='127.0.0.1')