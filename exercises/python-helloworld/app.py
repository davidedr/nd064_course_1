from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    response = json.dumps({'result': 'OK - healty'}), 200, {'ContentType':'application/json'} 
    app.logger.info("Status report successfull")
    return response

@app.route("/metrics")
def metrics():
    response = json.dumps({'UserCount': 140, 'UserCountActive': 23}), 200, {'ContentType':'application/json'} 
    app.logger.info("Status report successfull")
    return response

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
