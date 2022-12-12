from flask import Flask
from flask import render_template
from flask import request
import http.client
import json
import sys



app = Flask(__name__)
@app.route("/")
def landing_page():
    context = {'project': "flask-bootstrap", 'author': "Anubhav Sinha", 'items':["python", "flask", "jinja2", "bootstrap", "font-awesome", "jquery"] }
    return render_template('landing_page.html', **context)

@app.route('/people')
# ‘/’ URL is bound with hello_world() function.
def getPeople():

    conn = http.client.HTTPSConnection("finch-sandbox.vercel.app")

    headers = {
        'Content-Type': "application/json",
        'Finch-API-Version': "2020-09-17",
        'Authorization': "Bearer sandbox-token-c5777705-0253-4497-b7f9-db7548153739"
        }

    conn.request("GET", "/api/employer/directory", headers=headers)

    res = conn.getresponse()

    data = res.read()
    
    json_data = json.loads(data)

    return render_template('directory.html',data=json_data)

@app.route('/company')
# ‘/’ URL is bound with hello_world() function.
def getCompany():

    conn = http.client.HTTPSConnection("finch-sandbox.vercel.app")

    headers = {
        'Content-Type': "application/json",
        'Finch-API-Version': "2020-09-17",
        'Authorization': "Bearer sandbox-token-c5777705-0253-4497-b7f9-db7548153739"
        }

    conn.request("GET", "/api/employer/company", headers=headers)

    res = conn.getresponse()
    data = res.read()

    json_data = json.loads(data)

    return render_template('company.html',data=json_data)

@app.route('/payroll')
# ‘/’ URL is bound with hello_world() function.
def getPayroll():

    conn = http.client.HTTPSConnection("finch-sandbox.vercel.app")

    headers = {
        'Content-Type': "application/json",
        'Finch-API-Version': "2020-09-17",
        'Authorization': "Bearer sandbox-token-c5777705-0253-4497-b7f9-db7548153739"
        }

    conn.request("GET", "/api/employer/directory", headers=headers)

    res = conn.getresponse()

    data = res.read()
    
    json_data = json.loads(data)

    return render_template('directory.html',data=json_data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
