from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'himanshu'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = [
    {
        'name':'item1',
        'price': 10
    }
]

class item(Resource):
    def get(self,itemname):
        for item in items:
            if item['name'] == itemname:
                return item
        return 'item not found'
    @jwt_required()
    def post(self,itemname):
        requestdata = request.get_json()
        for item in items:
            if item['name'] == itemname:
                return 'item already exists'
        else:

            newitem = {
                'name': requestdata['name'],
                'price': requestdata['price']
            }
            items.append(newitem)
            return jsonify({'items':items})


api.add_resource(item,'/item/<string:itemname>')

app.run()