from psdirlisting import DirectoryListing
from json import dump


class DirectoryListing2JSON(DirectoryListing):
    """derived class"""

    def to_json(self, json_file):
        with open(json_file, 'w') as fw:
            dump(self.container, fw, indent=2)

    def to_xml(self, xml_file):
        pass


if __name__ == '__main__':
    DirectoryListing2JSON(r'/tmp', r'/home/ravi').to_json('tmp.json')
