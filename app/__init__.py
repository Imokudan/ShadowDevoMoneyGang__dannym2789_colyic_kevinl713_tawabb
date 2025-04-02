import sqlite3
import os
from flask import Flask,render_template,request,session,redirect,url_for,flash

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/visualization")
def visual():
  return render_template('home.html')

#Checks if user info is the same as the one saved in database
@app.route("/login")
def login():
  return render_template('home.html')

#Adds user info to database
@app.route("/register")
def register():
  return render_template('home.html')

@app.route("/preferences")
def preferences():
  return render_template('home.html')

@app.route("/interest")
def interest():
  return render_template('home.html')

if __name__ == "__main__":
    app.debug = True
    app.run(use_reloader=False, debug=False)
