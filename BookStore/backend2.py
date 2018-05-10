
import pyscopg2

createCommand = 'CREATE TABLE IF NOT EXISTS bkStore (itemName TEXT, quantity INTEGER, price REAL)'


def createCmd (sqlStmt):

    
def insertCmd (item, amt, price):


def deleteItemCmd (item):

def updateCmd (item, amt, price)

def observe():
    rows = view('SELECT * FROM bkstore')
    for row in rows:
        print(row)


def view (sqlStmt):
    return rows


# testing
createCmd(createCommand)
insertCmd('Calculus I', 25, 9.99)
insertCmd('Calculus II', 25, 19.99)
insertCmd('Calculus III', 25, 49.99)
observe()
deleteItemCmd('Calculus I')
observe()
updateCmd('Calculus II', 10, 19.99)
observe()



