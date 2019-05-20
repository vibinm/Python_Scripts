print(hex)
print(hex(15))

items = [1, 2, 3, 1, 4, 2, 5, 6, 7]

m = map(hex, items)
print(m)
for item in m:
    print(item)


m = map(ord, 'peter pan')
print(list(m))