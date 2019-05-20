import psutil
import os

for process in psutil.process_iter(attrs=['pid', 'name', 'username']):
    if 'chrome' in process.info['name'] and process.info['username'] == 'ravi':
        os.kill(process.info['pid'], 9)
