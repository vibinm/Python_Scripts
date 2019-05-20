
"""
112
<ascii char="p">112</ascii>
"""
list_of_ascii = [112, 101, 116, 101, 114, 32, 112, 97, 110]


def tag_it(av):
    return '<ascii char="{}">{}</ascii>'.format(chr(av), av)


m = map(tag_it, list_of_ascii)
m = map(lambda av: '<ascii char="{}">{}</ascii>'.format(chr(av), av), list_of_ascii)
for tag in m:
    print(tag)
