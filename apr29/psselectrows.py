import sqlite3

connect = sqlite3.connect('may02.sqlite')
cur = connect.cursor()

query = 'delete from passwd where uid < 1000'
cur.execute(query)
connect.commit()

query = 'select * from passwd order by login'
cur.execute(query)
print(cur.description)

heading = [column_info[0] for column_info in cur.description]

for row in cur.fetchall():
    for name, value in zip(heading, row):  # parallel iteration
        print(name, ':', value)
    print()
