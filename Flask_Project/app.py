from flask import Flask,Request
from flask_restful import Resource,Api

app = Flask(__name__)
api=Api(app)

class Hello(Resource):
    def __init__(self):
        pass
    def get(self):
        return {'about':'Hello world'}
    
    
api.add_resource(Hello,'/')
if __name__=='__main__':
    app.run(debug=True)