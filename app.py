#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ephemeral by st0le
# quick way share text between your network devices 

from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object(".config.PythonAnywhereConfig")

db = SQLAlchemy(app)

class Entry(db.Model):
    ip = db.Column(db.String(255), primary_key=True)
    text = db.Column(db.String(10*1024*1024))

    def __init__(self, ip, text):
        self.ip = ip
        self.text = text

    def __repr__(self):
        return "Entry <{}, {}>" % (self.ip, self.text)

def get_client_ip(request):
    # PythonAnywhere.com calls our service through a loabalancer
    # the remote_addr is therefore the IP of the loaabalancer, PythonAnywhere stores Client IP in header
    if request.headers.get('X-Real-IP', False): return request.headers['X-Real-IP']
    return request.remote_addr

@app.route('/')
def get():
    client_ip = get_client_ip(request)
    entries = Entry.query.filter_by(ip = client_ip).first()
    content = entries.text if entries != None else ""
    return render_template("index.html", text = content)

@app.route('/', methods=['POST'])
def post():
    client_ip, content = get_client_ip(request), request.form.get('text')
    entry = Entry.query.filter_by(ip = client_ip).first()
    if entry == None:
        entry = Entry(client_ip, content)
        db.session.add(entry)
    else:
        entry.text = content
    db.session.commit()
    return redirect(url_for('get'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(host="0.0.0.0")