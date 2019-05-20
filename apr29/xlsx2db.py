"""dump into the table"""
import pyexcel
import sqlite3

connect = sqlite3.connect('may02.sqlite')
cur = connect.cursor()
query = 'insert into passwd values (?, ?, ?, ?, ?, ?, ?)'

sheet = pyexcel.get_sheet(file_name='passwd.xlsx')
content = [row for row in sheet]

cur.executemany(query, content)
connect.commit()

cur.close()
connect.close()

