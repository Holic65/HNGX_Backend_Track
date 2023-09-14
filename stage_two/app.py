from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import uuid
import sqlite3
from users import db, Users


app = Flask(__name__)
api = Api(app)
app.config['STRICT_SLASHES'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app )

Data = []


@app.before_request
def create_table():
    db.create_all()

#route to query all users using GET request
@app.route('/api/', methods=['GET'])
def get_all():
    users = Users.query.all()
    user_list = [{'name': user.name, 'userid': user.userid} for user in users]
    return jsonify(user_list), 200


#route to create new user using POST request
@app.route('/api/', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = uuid.uuid4().hex
    if data is None:
        return jsonify({'error': 'Name is missing'}), 400
    
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    
    user = Users(data['name'], user_id)
    db.session.add(user)
    db.session.commit()
    return jsonify({'name': data['name'], 'userid': user_id}), 201


#route to query user with userid using GET request 
@app.route('/api/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = Users.query.filter_by(userid=user_id).first()
    if not user:
        return jsonify({'error': 'data not found'}), 400
    return jsonify({'name': user.name, 'userid': user.userid})


#route to update user using PUT request
@app.route('/api/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    user = Users.query.filter_by(userid=user_id).first()
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Name is missing'}), 400
    if 'name' in data:
        new_name = data['name']
    else:
        return jsonify({'error': 'Name is missing'}), 400
    
    if not user:
        return jsonify({'error': 'Invalid userid'}), 400
    
    user.name = new_name
    db.session.commit()

    return jsonify({'name': user.name, 'userid': user.userid}), 200


#route to delete user using DELETE request
@app.route('/api/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Users.query.filter_by(userid=user_id).first()
    if not user:
        return jsonify({'error': 'Invalid userid'})
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)