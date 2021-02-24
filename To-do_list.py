import firebase_admin
from firebase_admin import credentials,db
from flask import Flask,jsonify,abort,request

cred = credentials.Certificate("api-tdl-firebase-adminsdk.json")
default_app=firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://api-tdl-default-rtdb.firebaseio.com/'
})

print(default_app)

ref=db.reference('/')

def Read():
    print(ref.get())

def Create():
    ref.set({
        'tasks':{
            '1':{
                'Name':'Ir a bañarse',
                'Check':False
            },
            '2':{
                'Name':'Estudiar',
                'Check':False
            },
        }
    })

def Update():
    pass

def Delete():
    pass

Create()

'''
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
    app.run(debug=True)'''