import csv

count = dict()

for row in csv.reader(open('passwd.txt'), delimiter=':'):
    shell = row[-1]
    count[shell] = count.get(shell, 0) + 1  # add & update

print(count)
