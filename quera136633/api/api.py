from flask import Flask, Response
import os
app = Flask(__name__)

@app.route("/")
def success():
    server = os.environ.get('HOSTNAME')
    status = os.environ.get('STATUS')
    return server, int(status)
