from pssshclient import CustomSSHClient
from psdemoarchives import make_archive
from glob import glob


class SFTPClient(CustomSSHClient):
    def __init__(self, host, port, user, pwd):
        super().__init__(host, port, user, pwd)
        self.sftp = self.ssh.open_sftp()

    def upload(self, src, dest):
        self.sftp.put(src, dest)
        print('{} uploaded as {}'.format(src, dest))

    def __del__(self):
        self.sftp.close()
        super().__del__()


if __name__ == '__main__':
    make_archive('pdfs.zip', archive_type='zip').save(*glob('/home/ravi/*.pdf'))
    ftp = SFTPClient('localhost', 22, 'training', 'training')
    ftp.upload('pdfs.zip', 'pdfs.zip')
    print(ftp.check_output('ls -l'))
