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
