from flask import Flask, render_template
import requests, json, pprint

app = Flask(__name__)

def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    return response.json()['response']['serviceTicket']
@app.route('/')
def index():
    return render_template('topology.html')

@app.route('/api/topology')
def topology():
    url = 'https://sandboxapicem.cisco.com/api/v1/topology/physical-topology'
    header = {"content-type": "application/json", "X-Auth-Token": t}
    res = requests.get(url, headers=header, verify=False)
    return res.json()['response']

if __name__ == '__main__':
    t = new_ticket()
    app.run(debug=True)
