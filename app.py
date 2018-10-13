from flask import Flask, redirect, request, render_template, url_for

app = Flask(__name__)

users = {
    'admin': 'password',
    'student': 'password',
    'parent': 'password'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            if username == 'student':
                return redirect(url_for('student'))
            elif username == 'parent':
                return redirect(url_for('forms'))
            elif username == 'admin':
                return redirect(url_for('admin'))

@app.route('/forms', methods=['GET'])
def forms():
    return render_template('forms.html')


                

        

if __name__ == '__main__':
    app.run(debug=True)