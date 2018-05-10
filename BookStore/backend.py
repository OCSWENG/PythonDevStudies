import sqlite3

global db = 'BookStore.db'
global createStmt = "CREATE TABLE IF NOT EXISTS bkStore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)"
def connect():
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(createStmt)
    conn.commit()
    conn.close()

global insertStmt = "INSERT INTO bkStore VALUES (NULL,?,?,?,?)"
def insert(title,author,year,isbn):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(insertStmt,(title,author,year,isbn))
    conn.commit()
    conn.close()
    view()

global updateStmt = "UPDATE bkStore SET title=?, author=?, year=?, isbn=? WHERE id=?"
def update(id,title,author,year,isbn):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(updateStmt,(title,author,year,isbn,id))
    conn.commit()
    conn.close()

global viewStmt = "SELECT * FROM bkStore"
def view():
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(viewStmt)
    rows=cur.fetchall()
    conn.close()
    return rows

global searchStmt = "SELECT * FROM bkStore WHERE title=? OR author=? OR year=? OR isbn=?"
def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(searchStmt, (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

global deleteStmt = "DELETE FROM bkStore WHERE id=?"
def delete(id):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(deleteStmt,(id))
    conn.commit()
    conn.close()

connect()