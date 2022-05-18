from flask import Flask,jsonify,request
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)
#data={'name':'sumana',
#        'address':'Nellore'}

class Hello(Resource):
    def get(self):
        return jsonify({'name':'sumana',
        'address':'Nellore'},200)
    
  
api.add_resource(Hello,'/')
if __name__=='__main__':
    app.run(debug=True)