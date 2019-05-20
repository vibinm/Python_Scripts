"""list of users from the passwd database"""

list_of_users = list()

try:
    with open('passwd.txt') as fp:  # context manager
        for line in fp:
            login = line.split(':')[0]
            list_of_users.append(login)

    list_of_users.sort()
    
    with open('passwd.dat', 'w') as fw:
        for line_no, user in enumerate(list_of_users, 1):
            content = '{:>6}  {}'.format(line_no, user)
            print(content)
            fw.write(content + '\n')

except (FileNotFoundError, IOError) as err:
    print(err)
