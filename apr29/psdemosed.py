import re
import fileinput
import time

for line in fileinput.input('passwd.txt', inplace=True, backup=time.strftime('%d%m%Y%H%M%S')+'.bak'):
    if fileinput.filelineno() <= 10:
        line = re.sub(':', ',', line)

    print(line, end='')
