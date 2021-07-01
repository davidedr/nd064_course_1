from flask import Flask
from flask import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    return json.dumps({'result': 'OK - healty'}), 200, {'ContentType':'application/json'} 

@app.route("/metrics")
def metrics():
    return json.dumps({'UserCount': 140, 'UserCountActive': 23}), 200, {'ContentType':'application/json'} 

if __name__ == "__main__":
    app.run(host='0.0.0.0')
