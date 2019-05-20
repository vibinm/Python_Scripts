import re

for line in open('listing.dat'):
    print(re.split('[:,;]| +', line))

"""http://collabedit.com/6h2v5"""