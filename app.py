from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = 'your secret key'


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form:
        username = request.form['username']
        session['username'] = username
        msg = 'Logged in successfully !'
        return render_template('index.html', msg=msg)

    return render_template('login.html', msg=msg)


if __name__ == '__main__':
    app.run()
