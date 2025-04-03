'''
Shadow Devo Money Gang - Danny Mok, Colyi Chen, Kevin Liu, Tawab Berri
SoftDev
Spring 2025
p04 - Trump Insults
'''

import sqlite3, csv

DB_FILE = "database.db"

db = sqlite3.connect(DB_FILE, check_same_thread = False)
c = db.cursor()

with open("app/static/trump_insult_tweets_2014_to_2021.csv", "r") as file:
    text = csv.reader(file)
    csv = []
    for row in text:
        csv.append(row)
    print(csv)

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
    db.commit()

def createU(name, passw):
    c.execute("INSERT INTO users (username, password) VALUES (?, ?);", (name, passw))
    db.commit()
    print(f"added user {name} to database!")

def getUserPass(id):
    c.execute("SELECT username, password FROM users WHERE id = ?", (id,))
    row = c.fetchone()
    if row == None:
        return None
    return [row[0], row[1]]
