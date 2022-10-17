from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# init app
app = Flask(__name__)
app.config.from_object(__name__)

# create db config
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db, marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# db tables
class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  description = db.Column(db.String(400))

  def __init__(self, title, description):
    self.title = title
    self.description = description

class TodoSchema(ma.Schema):
  class Meta:
    fields = ('id', 'title', 'description')

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

# enable CORS
CORS(app, resources={r'/api': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'Content-Type'

## endpoints
# echo test
@app.route('/echo', methods=['GET'])
def echo():
  return jsonify("Hello world")

# create new todo
@app.route('/api/todo', methods=['POST'])
@cross_origin(origin='*', headers=['content-type'])
def add_todo():
  # get the data
  title = request.json['title']
  description = request.json['description']
  
  # create an instance
  new_todo = Todo(title, description)

  # save the todo in the db
  db.session.add(new_todo)
  db.session.commit()

  #return the created todo
  return todo_schema.jsonify(new_todo)
  
# get all todos
@app.route('/api/todo', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type'])
def get_todos():
  # get the todos from the db
  all_todos = Todo.query.all()

  # get the todos as per the schema
  result = todos_schema.dump(all_todos)

  # return the todos
  return jsonify(result)

# get single todo
@app.route('/api/todo/<id>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type'])
def get_todo(id):
  todo = Todo.query.get(id)
  # return todo as per schema
  return todo_schema.jsonify(todo)

# update a todo
@app.route('/api/todo/<id>', methods=['PUT'])
@cross_origin(origin='*', headers=['Content-Type'])
def update_todo(id):
  # get the todo first
  todo = Todo.query.get(id)
  # get the data
  title = request.json['title']
  description = request.json['description']

  # set the data
  todo.title = title
  todo.description = description

  # update the db
  db.session.commit()

  # return the new todo as per the schema
  return todo_schema.jsonify(todo)

# delete a todo
@app.route('/api/todo/<id>', methods=['DELETE'])
@cross_origin(origin='*', headers=['Content-Type'])
def delete_todo(id):
  # get the todo to be deleted
  todo = Todo.query.get(id)

  # delete from the db
  db.session.delete(todo)

  # commit on the db
  db.session.commit()

  # return the deleted todo as per the schema
  return todo_schema.jsonify(todo)

# start the app
if __name__ == '__main__':
  app.run()