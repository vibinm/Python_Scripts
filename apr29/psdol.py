import csv
import pprint

with open('passwd.txt') as fp:
    content = {row[0]: row[1:] for row in csv.reader(fp, delimiter=':')}

pprint.pprint(content)