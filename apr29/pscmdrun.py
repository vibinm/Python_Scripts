import sys
import subprocess
import re
"""http://collabedit.com/6h2v5"""

if sys.platform == 'linux':
    cmd = ['ifconfig']
else:
    cmd = ['ipconfig']

op = subprocess.check_output(cmd)
# print(op.decode('utf-8'))  # bytes into unicode

pattern = r'\b([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\.'
pattern += r'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\.){2}'
pattern += r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\b'

for m in re.finditer(pattern, op.decode()):
    print(m.group())
