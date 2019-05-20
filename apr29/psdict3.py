info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

item = 'version'

if item in info:  # validate for the key
    info[item] = 3.6  # update

print(info)
print()

info['arch'] = 'x86_64'  # add
print(info)
print()

# add
# update
# delete
# lookup aka read
# iterate
