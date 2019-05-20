temp = [hex(item) for item in range(10)]
print(temp)
print()

items = [2, 1, 3, 2, 4, 3, 5, 6, 9, 7]
temp2 = [i ** i for i in items]
print(temp2)
print()

temp3 = [i for i in items]
print(temp3)
print()

temp4 = [i for i in items if i%2]  # compound list comprehension
print(temp4)
print()