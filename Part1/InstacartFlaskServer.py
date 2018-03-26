from flask import Flask, g, redirect, render_template, request, session, url_for
import os
import json

app=Flask(__name__, static_url_path='')
app.secret_key = os.urandom(16)

@app.before_request
def before_request():
    g.email = None
    if('email' in session):
        g.email = session['email']
    if('firstName' in session):
        g.firstName = session['firstName']
    if('lastName' in session):
        g.lastName = session['lastName']



@app.route('/', methods=['GET', 'POST'])
def rootDir():
    if request.method == 'POST':
        # POST
        print("POST")

    return render_template('index.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        # Validate registration information
        hasError = False
        fNameError = ''
        lNameError = ''
        emailError = ''
        phoneError = ''
        if(request.form['firstName'] == ''):
            fNameError = 'Please enter a first name.'
            hasError = True
        if(request.form['lastName'] == ''):
            lNameError = 'Please enter a last name.'
            hasError = True
        if(request.form['emailAddr'] == ''):
            emailError = 'Please enter an email address.'
            hasError = True
        if(request.form['phoneNum'] == ''):
            phoneError = 'Please enter a phone number.'
            hasError = True
        if(hasError == True):
            return render_template('registration.html', firstNameError=fNameError, lastNameError=lNameError, emailError=emailError, phoneError=phoneError)
        else:
            session['fName'] = request.form['firstName']
            session['lName'] = request.form['lastName']
            session['emailAddr'] = request.form['emailAddr']
            session['phoneNum'] = request.form['phoneNum']
            session['over21'] = request.form['over21']
            session['bgCheckReady'] = True
            return redirect(url_for('backgroundCheck'))

    return render_template('registration.html')

@app.route('/backgroundCheck')
def backgroundCheck():
    if 'bgCheckReady' in session:
        if session['bgCheckReady'] == True:
            return render_template('backgroundCheck.html')

    return redirect(url_for("registration"))

@app.route('/confirmation')
def confirmation():
    userData = {}
    userData['fName'] = session['fName']
    userData['lName'] = session['lName']
    userData['emailAddr'] = session['emailAddr']
    userData['phoneNum'] = session['phoneNum']
    userData['over21'] = session['over21']
    print(json.dumps(userData, indent=4))
    return render_template('confirmation.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    session.pop('loggedIn', None)

    if request.method == 'POST':
        error = 'Invalid login information'
        if('emailAddr' not in request.form):
            return render_template('login.html', errorText=error)
        if('emailAddr' not in session):
            return render_template('login.html', errorText=error)
        if request.form['emailAddr'] == session['emailAddr']:
            session['loggedIn'] = True
            return redirect(url_for('account'))
        else:
            return render_template('login.html', errorText=error)

    return render_template('login.html')

@app.route('/account')
def account():
    return render_template('account.html', firstName=session['fName'], lastName=session['lName'], emailAddr=session['emailAddr'], phoneNum=session['phoneNum'])
