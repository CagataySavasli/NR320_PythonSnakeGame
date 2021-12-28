import sqlite3

con = sqlite3.connect("nr320.db")

cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS players (name TEXT NOT NULL UNIQUE,password TEXT,maxScore INT)")
    con.commit()

def signin(name, password):
    try:
        cursor.execute("INSERT INTO players (name, password, maxScore) VALUES(?, ?, ?)", (name, password, 0))
        con.commit()
    except Exception as e:
        return False

def editScore(name, score):
    cursor.execute("SELECT p.maxScore FROM players as p WHERE p.name = '{}'".format(name))
    row = cursor.fetchall()
    if row[0][0] < score:
        cursor.execute("UPDATE players SET maxScore = ? WHERE name = ?", (score, name))
        con.commit()
        return score
    return row[0][0]

def login(name,password):
    cursor.execute("SELECT COUNT(name) FROM players WHERE name = ? AND password = ?",(name, password))
    row = cursor.fetchall()
    return row[0][0]

def checkForSignin(name):
    cursor.execute("SELECT COUNT(name) FROM players WHERE name = '{}'".format(name))
    row = cursor.fetchall()
    return row[0][0]

def getRank(name):
    cursor.execute("SELECT name, ROW_NUMBER() OVER(ORDER BY maxScore desc) RowNumber FROM players")
    row = cursor.fetchall()
    for index in row:
        if index[0] == name:
            return [index[1],len(row)]


signin("ali","a")
signin("ali2","a")
signin("ali3","a")
signin("ali4","a")
signin("ali5","a")
signin("ali6","a")

editScore("ali", 14)
editScore("ali2", 8)
editScore("ali3", 24)
editScore("ali4", 6)
editScore("ali5", 2)
editScore("ali6", 6)

print("Your rank is "+str(getRank("ali")[0])+" amoung "+str(getRank("ali")[1])+".")

