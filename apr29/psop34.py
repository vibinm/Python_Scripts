temp = [bin(i) for i in range(10)]
print(temp)
print()

temp2 = {bin(i) for i in range(10)}   # set compre.
print(temp2)
print()


temp2 = {i: bin(i) for i in range(10)}  # dict comprehension
print(temp2)
print()
