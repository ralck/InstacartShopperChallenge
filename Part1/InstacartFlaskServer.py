from flask import Flask, g, redirect, render_template, request, session
import os

app=Flask(__name__, static_url_path='')
app.secret_key = os.urandom(16)

@app.before_request
def before_request():
    g.user = None
    if('user' in session):
        g.user = session['user']


@app.route('/', methods=['GET', 'POST'])
def rootDir():
    if request.method == 'POST':
        # POST
        print("POST")

    return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/backgroundCheck', methods=['GET', 'POST'])
def backgroundCheck():
    # TODO: validate form submission
    return render_template('backgroundCheck.html')

@app.route('/confirmation')
def confirmation():
    # TODO: Create session cookie
    return render_template('confirmation.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/account')
def account():
    return render_template('account.html')
