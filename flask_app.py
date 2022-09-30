from flask import Flask, jsonify, request
app = Flask(__name__)

data = [
    {
        'Contact': '6412363420', 
        'Name':'Raju',
        'done':False,
        'id':1
    },
    {
       'Contact': '6412363420', 
        'Name':'Rahul',
        'done':False,
        'id':2
    }
]

@app.route("/")

def hello_world():
    return "hello World"

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please provide the data"
        },400)
    contact = {
       'id': data[-1]['id']+1, 
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False  
    }    
    data.append(contact)
    return jsonify({
            "status":"Success",
            "message":"Task added sucessfully"
        })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":data
    })

if(__name__=="__main__"):
    app.run(debug = True)