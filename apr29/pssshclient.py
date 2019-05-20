import paramiko
import hashlib


class CustomSSHClient:
    def __init__(self, host, port, user, pwd):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, self.pwd)

    def upload(self, src, dest):
        sftp = self.ssh.open_sftp()
        sftp.put(src, dest)
        sftp.close()

    def check_output(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        return stdout.read().decode()

    def __del__(self):
        self.ssh.close()


ssh = CustomSSHClient('localhost', 22, 'training', 'training')
ssh.upload('src.zip', 'source.zip')
op = ssh.check_output('sha1sum source.zip').split()
print(op)
digest = hashlib.sha1(open('src.zip', 'rb').read()).hexdigest()

if digest == op[0]:
    print('upload successfully')
else:
    print('err....')