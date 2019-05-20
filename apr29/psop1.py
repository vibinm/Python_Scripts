developers = ['pam', 'jane', 'tim', 'nick']
tester = ['pam', 'nick', 'amanda', 'kim']


x = set(developers)
y = set(tester)

print(x.intersection(y))
print(list(x.intersection(y)))
print(x & y)
print()

print(x.union(y))
print(x | y)
print()
print(x.difference(y))
print()
print(y - x)