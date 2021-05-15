from flask import Flask, render_template, request
app = Flask(__name__)

import requests
import json

@app.route('/')
def hello_world():
    r = requests.get(f'http://web:8000{request.path}')
    j = json.loads(r.text)
    
    return render_template('index.html', lolka=j['response'])