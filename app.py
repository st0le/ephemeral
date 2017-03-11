from flask import Flask, request, render_template, redirect, url_for

db = {}
app = Flask(__name__)

@app.route('/')
def get():
    ip = request.remote_addr
    return render_template("index.html", text = db.get(ip, ''))

@app.route('/', methods=['POST'])
def post():
    ip, content = request.remote_addr, request.form.get('text')
    if len(content) == 0:
        del db[ip]
    else:
        db[ip] = content
    return redirect(url_for('get'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")