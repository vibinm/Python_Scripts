"""immutable object, read-only list"""
items = (2.2, 'pam', 'tim', 'kim', .98, 1.2, 3., 4, 5.6, 'eva')
print(items)
print(type(items))
print(len(items))

# items[-1] = 'wall-e'

print(items[-3])  # indexing
print()
print(items[:-3])  # slicing
print()

for item in items[:-3]:  # iterate
    print(item)
