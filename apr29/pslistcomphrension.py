"""list comprehension"""
import pprint

with open('passwd.txt') as fp:  # context manager
    users = [line.split(':') for line in fp if 'bash' in line]  # list comprehension

pprint.pprint(users)
