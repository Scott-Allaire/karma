from flask import Flask, redirect, jsonify
from flask.globals import request
from flask.helpers import url_for, flash, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.debug = True
app.secret_key = 'secret'
app.config.update({
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite',
    'SQLALCHEMY_TRACK_MODIFICATIONS': True
})
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(2048))
    points = db.Column(db.Integer)
    recurring = db.Column(db.Boolean)
    period = db.Column(db.String(255))
    next_due = db.Column(db.Date)
    active = db.Column(db.Boolean)


@app.route('/api/task/<id>', methods=['GET'])
def get_task(id):
    task = Task.query.filter_by(id=id).first()
    make_response(jsonify(task), 200)


@app.route('/api/task', methods=['GET'])
def get_tasks():
    tasks = Task.query.order_by(Task.next_due.desc()).paginate(1, 20, error_out=False)
    make_response(jsonify(tasks), 200)


@app.route('/api/task', methods=['POST'])
def create_task():
    task = Task()
    task.name = request.form['name']
    task.description = request.form['description']
    task.points = request.form['points']
    task.recurring = request.form['recurring']
    task.period = request.form['period']
    task.next_due = request.form['next_due']
    task.active = request.form['active']
    db.session.add(task)
    db.session.commit()
    make_response(jsonify(task), 201)


@app.route('/api/task/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    make_response(jsonify(task), 200)


if __name__ == '__main__':
    db.create_all()
    app.run()
