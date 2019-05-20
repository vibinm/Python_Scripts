from random import shuffle

items = list(range(1, 200))
shuffle(items)
print(items)

m = map(lambda n: n % 7 == 0, items)
print(list(m))
print()

m = filter(lambda n: n % 7 == 0, items)
print(m)
# print(list(m))
for item in m:
    print(item)
print()
