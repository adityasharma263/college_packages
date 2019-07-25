#-*- coding: utf-8 -*-
__author__ = 'aditya'

from ts import app
from flask import render_template, request, make_response, jsonify, abort, redirect
import requests

@app.route('/admin/college', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('partner-registration-form.html')
    elif request.method == 'POST':
        post_data = request.form.to_dict()
        res = requests.post('http://127.0.0.1:5000/api/v1/college', json=post_data)
        print(res.json(), "response")
        response = res.json()
        print(response,"aaasssssssssssssssssjhjh")
        return render_template('partner-registration-form.html', response=response)


@app.route('/college/login', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('partner-login.html')
    elif request.method == 'POST':
        post_data = request.form.to_dict()
        # res = requests.post('http://127.0.0.1:5000/api/v1/college', json=post_data)
        # print(res.json(), "response")
        # response = res.json()
        return render_template('partner-dashboard.html')

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



@app.route('/admin/student', methods=['GET','POST'])
def student():
    if request.method == 'GET':
        return render_template('students-registration-form.html')
    elif request.method == 'POST':
        post_data = request.form.to_dict()
        res = requests.post('http://127.0.0.1:5000/api/v1/student', json=post_data)
        print(res.json(), "response")
        response = res.json()
        return render_template('students-registration-form.html', response=response)

@app.route('/package/list', methods=['GET'])
def packagelist():
    team_url = 'http://127.0.0.1:5000/api/v1/package'
    data = requests.get(url=team_url).json()['result']['package']
    return render_template('all-packages.html', data=data)

@app.route('/package/college_dashboard', methods=['GET'])
def college_dashboard():
    team_url = 'http://127.0.0.1:5000/api/v1/college'
    data = requests.get(url=team_url).json()['result']['college']
    return render_template('partner-dashboard.html', data=data)

@app.route('/package/<package_id>', methods=['GET'])
def packagedetail(package_id):
    team_url = 'http://127.0.0.1:5000/api/v1/package'
    print("package", package_id)
    data = requests.get(url=team_url, params={"id": package_id}).json()
    if len(data['result']['package']) > 0:
        data = data["result"]["package"][0]
    else:
        data = {}
    return render_template('package-detail.html', data=data)



@app.errorhandler(400)
def page_not_found():
    return render_template("404.html"), 400





#
# @app.route('/dashboard', methods=['GET'])
# def dashboard():
#     rank = 0
#     score = 0
#     team_url = 'http://127.0.0.1:5000/api/v1/partner'
#     teams = requests.get(url=team_url).json()['result']['partners']
#     for team in teams:
#         if score == team['score']:
#             rank = rank
#         else:
#             rank = rank + 1
#         team['rank'] = rank
#         score = team['score']
#     return render_template('dashboard.html', teams=teams)
#
