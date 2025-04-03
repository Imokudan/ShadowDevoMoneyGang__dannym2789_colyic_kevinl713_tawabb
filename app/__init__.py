import os, db, sqlite3
from flask import Flask,render_template,request,session,redirect,url_for,flash

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def home():
    #db.create()
    return render_template('home.html')

@app.route("/visualization")
def visual():
    #Check login
    if 'username' not in session:
        return redirect('/')
    return render_template('home.html')

#Checks if user info is the same as the one saved in database
@app.route("/login")
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    #Check if user and pass match database
    if (username == db.getPass(username)):
        print("login successful!")
        session['username'] = username
        return redirect('/')
        #redirects to home page
    return render_template('login.html')

#Adds user info to database
@app.route("/register", methods=['GET', 'POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if (db.createU(username, password)):
        return redirect('/')
    #Check if username is the same otherwise add to database
    return render_template('register.html')

@app.route("/preferences")
def preferences():
    if 'username' not in session:
        return redirect('/')
    return render_template('home.html')

@app.route("/interest")
def interest():
    if 'username' not in session:
        return redirect('/')
    return render_template('home.html')

if __name__ == "__main__":
    app.debug = True
    app.run(use_reloader=False, debug=False)
