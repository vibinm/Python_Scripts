from os import listdir
from os.path import join, isfile

dir_path = '/tmp'
m = map(lambda item: join(dir_path, item), listdir(dir_path))
file_names = filter(isfile, m)

for file_item in file_names:
    print(file_item)
