import requests
import time
import json
import sys
from pyquery import PyQuery
import flask
from flask import request, jsonify
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

app = flask.Flask(__name__)
app.config["DEBUG"] = True

class SourcePortAdapter(HTTPAdapter):
    """"Transport adapter" that allows us to set the source port."""
    def __init__(self, port, *args, **kwargs):
        self._source_port = port
        super(SourcePortAdapter, self).__init__(*args, **kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, source_address=('', self._source_port))

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Tino API</h1>
<p>Email: support@tino.org</p>
<p>Website: my.tino.org</p>'''

@app.route('/api/', methods=['GET'])
def api_id():
    
    results = []
    
    try:
        s = requests.session()
        s.mount('https://cunghocwp.com', SourcePortAdapter(6000))
        res = s.get('https://cunghocwp.com', timeout=30)
        s.close()
        results.append(res.text)
        
    except Exception as err:
        results.append('ERR:{0}'.format(err))

    return jsonify(results)

if __name__ == '__main__':  
    try:                 
        if (sys.argv[1]):
            app.run(host='0.0.0.0', port=sys.argv[1])
    except:
        app.run()
    
        