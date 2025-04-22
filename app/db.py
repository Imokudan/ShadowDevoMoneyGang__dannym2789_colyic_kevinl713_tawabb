'''
Shadow Devo Money Gang - Danny Mok, Colyi Chen, Kevin Liu, Tawab Berri
SoftDev
Spring 2025
p04 - Trump Insults
'''

import sqlite3, csv

DB_FILE = "app/database.db"

db = sqlite3.connect(DB_FILE, check_same_thread = False)
c = db.cursor()

with open("app/static/trump_insult_tweets_2014_to_2021.csv", "r", encoding="utf-8") as file:
    text = csv.reader(file)
    csvo = []
    for row in text:
        csvo.append(row)
    #print(csv)
    csv = csvo[1:]
#print("db created!")
def create():
    c.execute("DROP TABLE IF EXISTS users;")
    c.execute(
        '''CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                target_pref TEXT,
                insult TEXT
                );
           ''')

    c.execute(
        '''CREATE TABLE IF NOT EXISTS csv (
            number INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            target TEXT NOT NULL,
            insult TEXT NOT NULL,
            tweet TEXT NOT NULL
        );
            ''')
    for row in csvo:
        c.execute("INSERT INTO csv (date, target, insult, tweet) VALUES (?, ?, ?, ?);", (row[1:]))
    db.commit()
create()
#print("db method")

def createU(name, passw):
    c.execute("SELECT id FROM users WHERE username = ?", (name,))
    r = c.fetchall()
    if (len(r) == 0):
        c.execute("INSERT INTO users (username, password) VALUES (?, ?);", (name, passw))
        db.commit()
        print(f"added user {name} to database!")
        return True
    else:
        print("user alrdy in db")
        return False
    
def getUser(user):
    c.execute("SELECT username FROM users WHERE username = ?", (user,))
    row = c.fetchone()
    print(f"returning username {row} for user {user}")
    if row == None:
        return None
    return row[0]

def getPass(user):
    c.execute("SELECT password FROM users WHERE username = ?", (user,))
    row = c.fetchone()
    print(f"returning password {row} for user {user}")
    if row == None:
        return None
    return row[0]

def printdb():
    c.execute("SELECT * FROM users;")
    u = c.fetchall()
    print(u)

    c.execute("SELECT * FROM csv;")
    s = c.fetchall()
    print(s[:25])
    return s

def getPrefs(user):
    c.execute("SELECT target_pref FROM users WHERE username = ?", (user,))
    ret = c.fetchall()
    print(f"returning preferences of user {user}: .{ret}.")
    if (ret == None): return None
    return ret

def getTweet(prefs):
    c.execute("SELECT tweet FROM csv WHERE target = ?", (prefs,))
    print("returning tweet given target")
    return c.fetchall()

def setPrefs(prefs):
    c.execute("INSERT INTO users (target_pref) VALUES (?);", (prefs,))
    print("user preferences updated")
    return True
