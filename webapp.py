from flask import Flask
from flask import render_template
from flask import request
import http.client
import json
import sys


app = Flask(__name__)

global token
global ben_id

@app.route("/")
def landing_page():
    context = {'project': "flask-bootstrap", 'author': "Anubhav Sinha", 'items':["python", "flask", "jinja2", "bootstrap", "font-awesome", "jquery"] }

    global token
    token = ''
    
    return render_template('landing_page.html', **context)

@app.route('/people')

def getPeople():
    if token == '':
            return render_template('notoken.html')
    else:    
        print(token)
        conn = http.client.HTTPSConnection("api.tryfinch.com")

        headers = {
            'Content-Type': "application/json",
            'Finch-API-Version': "2020-09-17",
            'Authorization': "Bearer "+token+""
            }

        conn.request("GET", "/employer/directory", headers=headers)

        res = conn.getresponse()

        data = res.read()
        
        json_data = json.loads(data)

        return render_template('directory.html',data=json_data)

@app.route('/company')

def getCompany():

    if token == '':
        return render_template('notoken.html')
    else:
        conn = http.client.HTTPSConnection("api.tryfinch.com")

        headers = {
            'Content-Type': "application/json",
            'Finch-API-Version': "2020-09-17",
            'Authorization': "Bearer "+token+""
            }

        conn.request("GET", "/employer/company", headers=headers)

        res = conn.getresponse()
        data = res.read()

        json_data = json.loads(data)

        return render_template('company.html',data=json_data)

@app.route('/payroll')

def getPayroll():
    if token == '':
            return render_template('notoken.html')
    else:
            def payroll():

                conn = http.client.HTTPSConnection("finch-sandbox.vercel.app")

                headers = {
                    'Content-Type': "application/json",
                    'Finch-API-Version': "2020-09-17",
                    'Authorization': "Bearer sandbox-token-c5777705-0253-4497-b7f9-db7548153739"
                    }

                conn.request("GET", "/api/employer/payment?start_date=2021-12-01&end_date=2022-11-01", headers=headers)

                res = conn.getresponse()

                data = res.read()
                
                json_data = json.loads(data)

                return json_data

            def people():
                conn = http.client.HTTPSConnection("api.tryfinch.com")

                headers = {
                    'Content-Type': "application/json",
                    'Finch-API-Version': "2020-09-17",
                    'Authorization': "Bearer "+token+""
                    }

                conn.request("GET", "/employer/directory", headers=headers)

                res = conn.getresponse()

                data = res.read()
                
                json_data = json.loads(data)

                return json_data

            pr = payroll()
            my_people = people()
            return render_template('payment.html',data=pr, people=my_people)

@app.route('/benefits')

def getBenefits():
    if token == '':
            return render_template('notoken.html')
    else:
            def getBenefits():

                conn = http.client.HTTPSConnection("api.tryfinch.com")

                headers = {
                    'Content-Type': "application/json",
                    'Finch-API-Version': "2020-09-17",
                    'Authorization': "Bearer "+token+""
                    }

                conn.request("GET", "/employer/benefits", headers=headers)

                res = conn.getresponse()

                data = res.read()
                
                json_data = json.loads(data)

                return json_data

            def people():
                conn = http.client.HTTPSConnection("api.tryfinch.com")

                headers = {
                    'Content-Type': "application/json",
                    'Finch-API-Version': "2020-09-17",
                    'Authorization': "Bearer "+token+""
                    }

                conn.request("GET", "/employer/directory", headers=headers)

                res = conn.getresponse()

                data = res.read()
                
                json_data = json.loads(data)

                return json_data


            benefits = getBenefits()
            my_people = people()

            return render_template('benefits.html',data=benefits, people=my_people)

@app.route('/getCode', methods=['POST'])

def authCode():
    auth_code = request.get_json()
    access_token = getAccessToken(auth_code)

    global token
    token = access_token

    return access_token

def getAccessToken(auth_code):

    code = auth_code['code']
    conn = http.client.HTTPSConnection("api.tryfinch.com")

    headers = {
        'Content-Type': "application/json",
        }
    body = '{\n    "client_id": "07de7bbc-b8aa-4f35-82cd-4bf934ad3da1",\n    "client_secret": "finch-secret-dev-Kct69y972Of47sx9fpxbuVeTCNZ47MW5B4DpOhnD",\n    "code": "'+ code +'",\n    "redirect_uri": "https://tryfinch.com"\n}'
    conn.request("POST", "/auth/token", headers=headers, body=body)

    res = conn.getresponse()

    data = res.read()
    json_data = json.loads(data)

    authentication_token = json_data['access_token']

    return json_data['access_token']


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
