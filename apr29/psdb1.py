import sqlite3


connect = sqlite3.connect('may02.sqlite')
cur = connect.cursor()

query = 'select sqlite_version()'
cur.execute(query)
print(cur.fetchone())

cur.close()
connect.close()