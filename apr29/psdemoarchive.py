import zipfile
import glob


def make_archive(archive_name, *args):
    """variable len arguments"""
    with zipfile.ZipFile(archive_name, mode='w') as zf:
        for file_name in args:
            zf.write(file_name)
            print('{} added'.format(file_name))


make_archive('src.zip', *glob.glob('*.py'))
