import sqlite3
connection = sqlite3.connect('flask_db.sqlite')

# with open('schema.sql') as f:
#     connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO UserData(email, first_name, last_name, password) VALUES(?, ?, ?, ?)", ("a@gmail.com", "pr","ch","abc"))

connection.commit()
connection.close()
