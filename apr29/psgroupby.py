import csv
import pprint

group_by = dict()

for row in csv.reader(open('passwd.txt'), delimiter=':'):
    user, shell = row[0], row[-1]

    # if shell not in group_by:
    #     group_by[shell] = list()
    #
    # group_by[shell].append(user)
    group_by.setdefault(shell, []).append(user)

# pprint.pprint(group_by)

for shell_name, list_of_users in group_by.items():
    print(shell_name)
    for user in list_of_users:
        print('\t', user)
    print()