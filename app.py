import json
from flask import Flask,Response,redirect,url_for,request,jsonify

app = Flask(__name__,static_folder='static', static_url_path="/static")

tasks=[]

@app.route('/tasks/',methods = ['GET'])
@app.route('/tasks/<task_id>',methods = ['GET'])
def get_task2(task_id=None):
    return jsonify(tasks)

@app.route('/tasks',methods = ['POST'])
def create_task():
    tasks.append(request.json)
    return redirect(url_for('get_task'))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")