from xml.etree.ElementTree import Element, SubElement, ElementTree

root_tag = Element('directories')

dir_tag = SubElement(root_tag, 'directory')
dir_tag.set('name', '/tmp')  # set to an attribute

file_tag = SubElement(dir_tag, 'file')
file_tag.attrib = dict(size='1234', mtime='Sat 13 Apr 2019 12:12:12')
file_tag.text = 'temp.txt'  # set text node to the tag

doc = ElementTree(root_tag)
doc.write('tmp.xml')