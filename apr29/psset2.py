# unordered collection
# unique
items = {1, 2.2, 'pam', 3, 4, 'jane', 'tim', 'kimberly', .98}
print(items)
print()

items.add('pip')
items.add(3.142)
print(items)
print()

items.remove('pam')  # delete
items.remove(.98)
print(items)
print()

for item in items:
    print(item)
