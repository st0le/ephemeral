#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ephemeral by st0le
# quick way share text between your network devices 

from flask import Flask, request, render_template, redirect, url_for
db = {}
app = Flask(__name__)

def get_client_ip(request):
    # PythonAnywhere.com calls our service through a loabalancer
    # the remote_addr is therefore the IP of the loaabalancer, PythonAnywhere stores Client IP in header
    if request.headers['X-Real-IP']: return request.headers['X-Real-IP']
    return request.remote_addr


if __name__ == "__main__":
    app.run(host="0.0.0.0")

@app.route('/')
def get():
    ip = get_client_ip(request)
    return render_template("index.html", text = db.get(ip, ''))

@app.route('/', methods=['POST'])
def post():
    ip, content = get_client_ip(request), request.form.get('text')
    if len(content) == 0:
        del db[ip]
    else:
        db[ip] = content
    return redirect(url_for('get'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")