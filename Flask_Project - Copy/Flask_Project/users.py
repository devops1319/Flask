from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        data = pd.read_csv('users.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        new_data = pd.DataFrame({
            'userId'      : [args['userId']],
            'name'       : [args['name']],
            'city'      : [args['city']]
        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('users.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 201

api.add_resource(Users,'/users')


if __name__=='__main__':
    app.run()
'''from flask import Flask
from flask_restful import Api,Resource,reqparse
import pandas as pd
from flask import request

app=Flask(__name__)
api=Api(app)

class Users(Resource):
    def get(self):
        data=pd.read_csv('users.csv')
        data=data.to_dict('records')
        return {'data':data},200

    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('userId',required=True)
        parser.add_argument('name',required=True)
        parser.add_argument('city',required=True)
        args=parser.parse_args()

        data=pd.read_csv('users.csv')

        new_data=pd.DataFrame({
            'userId':args['userId'],
            'name':args['name'],
            'city':args['city']
        })

        data=data.append(new_data,ignore_index=False)
        data.to_csv('users.csv',index=False)
        return {'data':new_data.to_dict('records')},201

api.add_resource(Users,'/users')


if __name__=='__main__':
    app.run()'''
