"""ssh client"""
import paramiko


class CustomSSHClient:
    port = 22
    """single threaded ssh client using Python"""
    def __init__(self, host, port=0, user="", pwd=""):
        self.host = host
        if port:
            self.port = port
        self.user = user
        self.pwd = pwd
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, port, self.user, self.pwd)

    def check_output(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        output = stdout.read().decode('utf-8')
        return output if output else stderr.read().decode('utf-8')  # bytes into unicode

    def __del__(self):
        self.ssh.close()


if __name__ == '__main__':
    ssh = CustomSSHClient('localhost', 22, 'training', 'training')
    op = ssh.check_output('ifconfig')
    print(op)
