info = {
    'host': 2.2,
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

for key, value in info.items():  # key, value pair
    if 2.2 == value:
        print(key, '->', value)
