"""classes & objects"""
from os import listdir
from os.path import join, isfile, getmtime, getsize, basename
from time import ctime
from pprint import pprint as pp


class DirectoryListing:
    """base class"""

    def __init__(self, *args):
        self.directories = args
        self.container = dict()
        self.read_directories()

    def read_directories(self):
        """read the content of the directories"""

        for dir_name in self.directories:
            m = map(lambda item: join(dir_name, item), listdir(dir_name))
            for file_name in filter(isfile, m):
                file_properties = [getsize(file_name), ctime(getmtime(file_name))]
                file_name = basename(file_name)
                self.container.setdefault(dir_name, {})[file_name] = file_properties


if __name__ == '__main__':
    dl = DirectoryListing(r'/tmp', r'/home/ravi')
    pp(dl.container, width=120)

# help(DirectoryListing)

"""
{
'd1' : {
        'f1': [size, mtime],
        'f2': [size, mtime],
        'f2': [size, mtime],
    },
'd2' : {
        'g1': [size, mtime],
        'g2': [size, mtime],
        'g3': [size, mtime],
    },.....
}
"""
