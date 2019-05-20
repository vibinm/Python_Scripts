"""delete by value"""
items = [2.2, 'pam', .98, 3.4, 1.2, 'pam', 'pam', 'pam', 'pam', 2.3, 'pam', 'pam']
item = 'pam'

while item in items:
    items.remove(item)

print(items)
print()
