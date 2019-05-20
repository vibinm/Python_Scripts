import csv
import pprint

keys = ['pwd', 'uid', 'gid', 'gecos', 'home', 'shell']

with open('passwd.txt') as fp:
    content = {row[0]: dict(zip(keys, row[1:])) for row in csv.reader(fp, delimiter=':')}

pprint.pprint(content)