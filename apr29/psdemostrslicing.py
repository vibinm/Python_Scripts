s = 'root:x:0:0:root:/root:/bin/bash'
print(s.index(':'))

print(s[:s.index(':')])