s = 'root:x:0:0:root:/root:/bin/bash'
delimiter = ':'

items = s.split(delimiter)
print(items)
print()

print(s.split(':')[0])  # indexing
print()

print(s.split(':')[1:])  # slicing
print()

for item in items:  # iterate
    print(item)
