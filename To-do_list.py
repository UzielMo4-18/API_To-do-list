from flask import Flask,jsonify,abort,request
app=Flask(__name__)

tasks=[
    {
        'id':1,
        'name':'Ir a bañarse',
        'check':False
    },
    {
        'id':2,
        'name':'Estudiar',
        'check':False
    }
]

@app.route('/')
def hello_world():
    return "API TO-DO list"

@app.route('/api/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

@app.route('/api/tasks/<int:id>',methods=['GET'])
def get_task(id):
    result=0
    for task in tasks:
        if task['id']==id: result=task
    
    if result==0: abort(404)

    return jsonify({'task':result})

@app.route('/api/tasks',methods=['POST'])
def create_task():
    if not request.json: abort(404)

    task={
        'id':len(tasks)+1,
        'name':request.json('name'),
        'check': False
    }

    tasks.append(task)
    return jsonify({'task':task}),201

if __name__=='__main__':
    app.run(debug=True)