"""list of users from the passwd database"""

list_of_users = list()

try:
    fp = open('passwd.txt')

    for line in fp:
        login = line.split(':')[0]
        list_of_users.append(login)

    fp.close()

    list_of_users.sort()

    for line_no, user in enumerate(list_of_users, 1):
        print('{:>6}  {}'.format(line_no, user))

except (FileNotFoundError, IOError) as err:
    print(err)
