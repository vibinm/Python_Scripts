"""demo for the python's iterator """
import os
import time

file_names = [r'/etc', r'/etc/group', '/etc/resolv.conf']

for file_name in file_names:
    print(file_name)
    print('\t', time.ctime(os.stat(file_name).st_mtime))
    print()
