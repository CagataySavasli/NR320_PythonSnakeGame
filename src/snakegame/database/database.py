import sqlite3

con = sqlite3.connect("nr320.db")

cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS players (name TEXT NOT NULL UNIQUE,password TEXT,maxScore INT)")
    con.commit()