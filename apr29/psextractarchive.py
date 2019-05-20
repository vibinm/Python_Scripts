import zipfile
import os
import os.path as path


def extract_zip(archive_name, target_directory):
    if not path.isdir(target_directory):
        os.mkdir(target_directory)

    with zipfile.ZipFile(archive_name, mode='r') as zf:
        zf.extractall(target_directory)


extract_zip('src.zip', '/tmp/catch22')
