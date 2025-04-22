try:
    import os, db, sqlite3
except:
    import os, db, sqlite3
from flask import Flask,render_template,request,session,redirect,url_for,flash

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def home():
    #db.create()
    print("before")
    datastore = db.printdb()
    print("after dbprint")
    if 'username' in session:
        print("logged in")
        return render_template('home.html', loggedin=True, data=datastore)
    return render_template('home.html', loggedin=False, data=datastore)

@app.route("/visualization")
def visual():
    #Check login
    if 'username' not in session:
        return redirect('/')
    return render_template('visualization.html')

#Checks if user info is the same as the one saved in database
@app.route("/login", methods=['GET','POST'])
def login():
    if 'username' in session:
        print("ALREADY LOGGED IN")
        redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        #Check if user and pass match database
        if(db.getPass(username) == password):
            session['username'] = username
            return redirect('/visualization')
        else:
        #RETURN ERROR MESSAGE
            return render_template('login.html', error = "INCORRECT USERNAME OR PASSWORD")

    return render_template('login.html')


#Adds user info to database
@app.route("/register", methods=['GET', 'POST'])
def register():
    if 'username' in session:
        redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if(db.createU(username,password)):
            session['username'] = db.getUser(username)
            return redirect('/preferences')
        else:
            return render_template('register.html', error = "USERNAME EXISTS")
    #Check if username is the same otherwise add to database
    
    return render_template('register.html')

@app.route("/preferences", methods=['GET', 'POST'])
def preferences():
    if 'username' not in session:
        return redirect('/')
    #Set preferences for tweets
    pref = request.form.get('preference')
    if pref != None:
        db.setPrefs(pref)
    return render_template('preferences.html')

@app.route("/interest")
def interest():
    if 'username' not in session:
        return redirect('/')
    pref = db.getPrefs(session['username'])
    #Get the preferences of the user then fetch it from database
    tweets = db.getTweet(pref)
    print(tweets)
    #Display tweets in html
    return render_template('interest.html')

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run(use_reloader=False, debug=False, host='0.0.0.0')
