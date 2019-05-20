import os


def ls(dirpath='.'):
    """default argument"""
    for item in sorted(os.listdir(dirpath)):
        print(item)


ls()