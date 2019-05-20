import re

s = 'the python and perl scripting'
pattern = 'P.+?N'  # non-greedy match

m = re.search(pattern, s, re.I)

if m:
    print('match string :', m.group())
    before = s[:m.start()]
    after = s[m.end():]
    print(before)
    print(after)
else:
    print('failed to match')
