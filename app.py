from flask import Flask, redirect, request, render_template, url_for, session, g
import os
import json
import sys

app = Flask(__name__)
app.secret_key = os.urandom(24)
# users = {
#     'admin': 'password',
#     'student': 'password',
#     'parent': 'password'
# }

users = {
    'admin': 
        {
            'password': 'password',
            'type': 'admin'
        },
    'student': 
        {
            'password': 'password',
            'type': 'student'
        },
    'parent':         
        {
            'password': 'password',
            'type': 'parent'
        },
}

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return "Dropped!"


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        session.pop('user', None)

        if username in users and users[username]['password'] == password:
            session['user'] = username

            if users[username]['type'] == "student":
                return redirect(url_for('student'))
            elif users[username]['type'] == "parent":
                return redirect(url_for('grades'))
            elif users[username]['type'] == "admin":
                return redirect(url_for('admin'))

@app.route('/forms', methods=['GET'])
def forms():
    if g.user:
        return render_template('enrollment.html')
    
    return redirect('login')


@app.route('/student', methods=['GET'])
def student():
    if g.user:
        return render_template('studentoptions.html')

    return redirect('login')


@app.route('/parent', methods=['GET'])
def parent():
    if g.user:
        return render_template('parents.html')
    
    return redirect('login')

@app.route('/grades', methods=['GET'])
def grades():
    if g.user:
            return render_template('grades.html')
    
    return redirect('login')

@app.route('/clientform', methods=['GET'])
def clientform():
    if g.user:
            return render_template('clientintake.html')
    
    return redirect('login')


@app.route('/admin', methods=['GET'])
def admin():
    if g.user:
        return render_template('admin.html')

    return redirect('login')


@app.route('/studentoptions', methods=['GET'])
def studentoptions():
    if g.user:
        return render_template('studentoptions.html')

    return redirect('login')

@app.route('/lessons', methods=['GET'])
def lessons():
    if g.user:
        with open('Unit.json') as f:
            unit = json.load(f)
            return render_template('lessons.html', unit=unit)

    return redirect('login')

@app.route('/gameoptions', methods=['GET'])
def gameoptions():
    if g.user:
        return render_template('gameoptions.html')

    return redirect('login')

@app.route('/games', methods=['GET'])
def games():
    if g.user:
        return render_template('game.html')

    return redirect('login')

if __name__ == '__main__':
    app.run(debug=True)