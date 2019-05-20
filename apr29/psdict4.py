info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

value = info.pop('desc')  # delete
print(value)
print()
print(info)
print()

