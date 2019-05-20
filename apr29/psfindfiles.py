import os
import pprint

items_found = dict()

for dirpath, dirnames, filenames in os.walk(r'/home/ravi'):
    pdfs = [file_name for file_name in filenames if file_name.endswith('.pdf')]

    if pdfs:
        items_found[dirpath] = pdfs

pprint.pprint(items_found)
