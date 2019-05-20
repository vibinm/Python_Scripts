from os import listdir
from os.path import isfile, isdir, getsize, getmtime, join
from time import ctime

dir_path = r'/tmp'
# abs_path = dir_path +'/'+listdir(dir_path)[0]
abs_path = join(dir_path, listdir(dir_path)[0])
print(abs_path)
print()
print(isfile(abs_path))
print(isdir(abs_path))
print(getsize(abs_path))
print(getmtime(abs_path))
print(ctime(getmtime(abs_path)))