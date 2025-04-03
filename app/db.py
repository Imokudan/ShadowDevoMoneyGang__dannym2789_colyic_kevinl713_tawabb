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

with open("app/static/trump_insult_tweets_2014_to_2021.csv", "r") as file:
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
    c.execute("SELECT id FROM users WHERE username = ?" (name,))
    r = c.catchall()
    if (len(r) == 0):
        c.execute("INSERT INTO users (username, password) VALUES (?, ?);", (name, passw))
        db.commit()
        print(f"added user {name} to database!")
        return True
    else:
        print("user alrdy in db")
        return False

def getPass(user):
    c.execute("SELECT password FROM users WHERE username = ?", (user,))
    row = c.fetchone()
    if row == None:
        return None
    return row[0]
