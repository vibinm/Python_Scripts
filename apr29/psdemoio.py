"""demo for the IO"""
try:
    name = input('enter the name :')
    city = input('enter the city :')
    zip_code = int(input('enter the postal code :'))

    print('name :', name)
    print('city :', city)
    print(zip_code)
    print(type(zip_code))
except ValueError as err:
    print(err)
