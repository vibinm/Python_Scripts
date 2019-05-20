"""abstract member/archive"""
from glob import glob
from abc import ABC, abstractmethod
from zipfile import ZipFile
# from tarfile import TarFile

"""http://collabedit.com/u2582"""


class ArchiveManager(ABC):
    """abstract class"""

    @abstractmethod
    def save(self):
        """abstract methodf"""


class ZIPArchive(ArchiveManager):
    def __init__(self, name):
        self.archive_name = name

    def save(self, *args):
        with ZipFile(self.archive_name, mode='w') as zw:
            for file_name in args:
                zw.write(file_name)
                print('{}: added'.format(file_name))


class TarArchive(ArchiveManager):
    def __init__(self, _):
        pass

    def save(self):
        pass


def make_archive(archive_name, **kwargs):
    """factory method"""
    archive_type = kwargs.get('archive_type')

    if archive_type == 'zip':
        return ZIPArchive(archive_name)
    elif archive_name == 'tar':
        return TarArchive(archive_name)
    else:
        raise UnSupportedArchiveError('{}: format not yet supported....'.format(archive_type))


class UnSupportedArchiveError(Exception):
    """custom exception"""


if __name__ == '__main__':
    try:
        archive = make_archive('src.zip', archive_type='rar')
        archive.save(*glob('*.py'))
    except UnSupportedArchiveError as err:
        print('handle exception & throwing it')
        raise
