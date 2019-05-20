"""string formatting"""
# {:fmt-str}

import math

try:
    radius = float(input('enter the radius :'))
    area = math.pi * radius ** 2
    content = 'given radius : {}\narea : {:.3f}'.format(radius, area)
    print(content.upper())
except ValueError as err:
    print(err)
