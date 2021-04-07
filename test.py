import requests
import time
import json
import sys
from pyquery import PyQuery
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Tino API</h1>
<p>Email: support@tino.org</p>
<p>Website: my.tino.org</p>'''

@app.route('/api/', methods=['GET'])
def api_id():
    
    results = []
    
    try:
        res = requests.get('https://cunghocwp.com', timeout=10)
        results.append(res.text)
    except:
        results.append('REQUEST TIMEOUT!')

    return jsonify(results)

if __name__ == '__main__':        
    try:
        if (sys.argv[1]):
            app.run(host='0.0.0.0', port=sys.argv[1])
    except:
        app.run()
    
        