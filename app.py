from flask import Flask, redirect, request, render_template, url_for, session, g
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
# users = {
#     'admin': 'password',
#     'student': 'password',
#     'parent': 'password'
# }

users = {
    'person1': 
        {
            'password': 'password',
            'type': 'admin'
        },
    'person2': 
        {
            'password': 'password',
            'type': 'student'
        },
    'person3':         
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
                return redirect(url_for('parent'))
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
        return render_template('tasks.html')

    return redirect('login')


@app.route('/parent', methods=['GET'])
def parent():
    if g.user:
        return render_template('parents.html')
    
    return redirect('login')


@app.route('/admin', methods=['GET'])
def admin():
    if g.user:
        return render_template('admin.html')

    return redirect('login')

  

        

if __name__ == '__main__':
    app.run(debug=True)