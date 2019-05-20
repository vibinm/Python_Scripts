"""log parser"""

import re

pattern = '^root'
pattern = 'bash$'
pattern = '^$'
pattern = 'b.t'
pattern = 'b[aeiou]t'
pattern = 'b[^aeiou]t'
pattern = r'\b[6-9][0-9]{9}\b'


with open('contacts.csv') as fp:
    for line in fp:
        if re.search(pattern, line, re.I):
            print(line, end='')
