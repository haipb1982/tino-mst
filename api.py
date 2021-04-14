import requests
import time
import json
import sys
from pyquery import PyQuery
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#################################
def writeLog(strErr):    
    file_object = open('errorLog.log', 'a')
    file_object.writelines(strErr)
    file_object.close()


# qstr : 111655768
def crawlDataBySearch(qstr):

    result={
        'id': '',       
        'success': 0, 
        'type': '', 
        'typeId': 0, 
        'url': '', 
        'force-search': '1', 
        'numRows': 1,
        'taxinfo':'',
        'taxdetails':'',
        'name':'',
        'alternateName':'',
        'taxID':'',
        'address':'',
        'alumni':'',
    }

    try:
        url = 'https://masothue.com'
        # q=111655768&type=auto&token=e2rCP0ONvG&force-search=1
        myobj = {'q': qstr,'type':'auto','token':'','force-search':'1'}

        # print(myobj)

        response = requests.post(url + '/Ajax/Search', data = myobj)

        res = json.loads(response.text)

        # print(response.status_code)
        # print(response.json())
        # print(json.loads(response.text))

        result['id'] = qstr
        if (res['success'] !=1):
            return result

        result['success'] = res['success']
        result['type'] = res['type']
        result['typeId'] = res['typeId']
        result['url'] = res['url'] 
        result['force-search'] = res['force-search'] 

        time.sleep(1)

        response = requests.get(url + res["url"])

        pq = PyQuery(response.content)        

        tag1 = pq('table.table-taxinfo')
        tag2 = pq('table.table')

        result['taxinfo'] = tag1.html()
        result['taxdetails'] = tag2.html()

        result['name'] =tag1('[itemprop=name]').text()
        result['alternateName'] =tag1('[itemprop=alternateName]').text()
        result['taxID'] =tag1('[itemprop=taxID]').text()
        result['address'] =tag1('[itemprop=address]').text()
        result['alumni'] = tag1('[itemprop=alumni]').text().replace('Người đại diện','').strip()

        # print(result)

    except Exception as exc: 
        mess = f'{qstr} has error : {exc}'
        writeLog(mess)
        print(mess)

    return result


def create_json_file(mst, data, output_file):
    if data !='' and mst !='':
        with open(output_file, "w+") as f:
            # f.writelines("'{}':'{}'".format(mst, data))
            f.writelines(data)

def processMST(fromMST, toMST):    
    while fromMST < toMST :
        mstData =  crawlDataBySearch('031' + str(fromMST))
        if (mstData):
            create_json_file(fromMST,mstData,'./results/'+ str(fromMST) + '.json')
        fromMST +=1

#################################

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Tino API</h1>
<p>Email: support@tino.org</p>
<p>Website: my.tino.org</p>'''

@app.route('/api/', methods=['GET'])
def api_id():
    
    if 'id' in request.args:
        # id = int(request.args['id'])
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."

    results = []
    
    mstData =  crawlDataBySearch(id)
    # create_json_file(fromMST,mstData,'./results/'+ str(fromMST) + '.json')
    # print(mstData)
    results.append(mstData)
    # print(results)
    return jsonify(results)

if __name__ == '__main__':    
    
    try:
        if (sys.argv[1]):
            app.run(host='0.0.0.0', port=sys.argv[1])
    except:
        app.run()
    
        