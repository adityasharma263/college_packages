#-*- coding: utf-8 -*-
__author__ = 'aditya'


from ts import app
from flask import render_template, request, make_response, jsonify, abort, redirect, session, url_for
import requests
app.secret_key = "college data secret key"


@app.route('/admin/college', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('partner-registration-form.html')
    elif request.method == 'POST':
        post_data = request.form.to_dict()
        college_url = 'http://127.0.0.1:5000/api/v1/college'
        data = requests.get(url=college_url, params=post_data).json()
        res = requests.post('http://127.0.0.1:5000/api/v1/college', json=post_data)
        print(res.json(), "response")
        response = res.json()
        print(response)
        return render_template('partner-registration-form.html', response=response)


@app.route('/admin/package', methods=['GET', 'POST'])
def package():
    if request.method == 'GET':
        return render_template('package-entry-form.html')
    elif request.method == 'POST':
        post_data = request.form.to_dict()
        res = requests.post('http://127.0.0.1:5000/api/v1/package', json=post_data)
        print(res.json(), "response")
        response = res.json()
        return render_template('package-entry-form.html', response=response)


@app.route('/admin/student', methods=['GET', 'POST'])
def student():
    if request.method == 'GET':
        args = request.args.to_dict()
        return render_template('students-registration-form.html', args=args)
    elif request.method == 'POST':
        post_data = request.form.to_dict()
        res = requests.post('http://127.0.0.1:5000/api/v1/student', json=post_data)
        print(res.json(), "response")
        response = res.json()
        return render_template('students-registration-form.html', response=response)


@app.route('/college/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('partner-login.html')
    elif request.method == 'POST':
        post_data = request.form.to_dict()
        session["post_data"] = post_data
        # college_url = 'http://127.0.0.1:5000/api/v1/college'
        # data = requests.get(url=college_url, params=post_data).json()
        # if len(data['result']['college']) > 0:
        #     data = data["result"]["college"][0]
        # else:
        #     data = {}
        # resp = make_response(render_template('partner-dashboard.html', data=data))
        # resp.set_cookie('userID', post_data['username'])
        # session = requests.Session()
        # print(session.cookies.get_dict())
        # response = session.get('http://127.0.0.1:5000/college/login')
        # print(response.cookies.get_dict())
        return redirect(url_for('college_dashboard'))


@app.route('/college/dashboard', methods=['GET'])
def college_dashboard():
    if 'post_data' in session:
        post_data = session["post_data"]
        college_url = 'http://127.0.0.1:5000/api/v1/college'
        data = requests.get(url=college_url, params=post_data).json()
        if len(data['result']['college']) > 0:
            data = data["result"]["college"][0]
            for package in data["packages"]:
                package["student_link"] = 'http://127.0.0.1:5000/admin/student?college_id=' + str(data["id"]) + \
                                          '&package_id=' + str(package["id"])
        else:
            data = {}
        # resp = make_response(render_template('partner-dashboard.html', data=data))
        # resp.set_cookie('userID', post_data['username'])
        return render_template('partner-dashboard.html', data=data)
    return "You are not logged in <br><a href = '/college/login'></b>" + \
           "click here to log in</b></a>"


@app.route('/package/list', methods=['GET'])
def package_list():
    package_url = 'http://127.0.0.1:5000/api/v1/package'
    data = requests.get(url=package_url).json()['result']['package']
    if 'post_data' in session:
        post_data = session["post_data"]
        resp = make_response(render_template('all-packages.html', data=data))
        resp.set_cookie('username', post_data['username'])
        return resp
    return render_template('all-packages.html', data=data)


@app.route('/package/<package_id>', methods=['GET'])
def package_detail(package_id):
    package_url = 'http://127.0.0.1:5000/api/v1/package'
    data = requests.get(url=package_url, params={"id": package_id}).json()
    if len(data['result']['package']) > 0:
        data = data["result"]["package"][0]
    else:
        data = {}
    return render_template('package-detail.html', data=data)


@app.route('/')
def bag_pack_home():
    return render_template('index.html')


@app.errorhandler(400)
def page_not_found():
    return render_template("404.html"), 400


