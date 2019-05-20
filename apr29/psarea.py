import math

try:
    radius = float(input('enter the radius :'))
    area = math.pi * radius ** 2
    print('given radius :', radius)
    print('area :', area)
except ValueError as err:
    print(err)
