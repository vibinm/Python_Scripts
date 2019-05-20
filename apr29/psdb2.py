"""to create table"""
import sqlite3

"""http://collabedit.com/x7rtp"""

connect = sqlite3.connect('may02.sqlite')
cur = connect.cursor()

query = """
create table passwd(
login varchar(32),
pwd varchar(4),
uid int,
gid int, 
gecos varchar(128),
home varchar(64), 
shell varchar(32))
"""
cur.execute(query)
cur.close()
connect.close()