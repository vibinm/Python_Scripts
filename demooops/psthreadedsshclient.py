"""threaded ssh client"""
"""http://collabedit.com/x96c2"""
import threading
from pssshclient import CustomSSHClient
from pyexcel import get_sheet

target_file = 'sshresponse.log'


class ThreadedSSHHandler(CustomSSHClient):
    def __init__(self, host, port, user, pwd, job):
        self.job = job
        self.t_name = threading.currentThread().name
        super().__init__(host, port, user, pwd)
        self.task_runner()

    def task_runner(self):
        payload = self.check_output(self.job)
        caption = '{} ran {} @ {}'.format(self.t_name, self.job, self.host)

        with open(target_file, 'a') as fw:
            """critical section"""
            fw.write(caption.center(80, '-') + '\n')
            fw.write(payload + '\n')


class ThreadedSSHClient:
    list_of_threads = list()

    def __init__(self, ssh_host_file):
        self.host_file = ssh_host_file
        self.parse_ssh_host_file()

    def parse_ssh_host_file(self):
        sheet = get_sheet(file_name=self.host_file)

        for ssh_config in sheet:
            t = threading.Thread(target=ThreadedSSHHandler, args=ssh_config)
            ThreadedSSHClient.list_of_threads.append(t)
            t.start()

        for child in ThreadedSSHClient.list_of_threads:
            child.join()


if __name__ == '__main__':
    ThreadedSSHClient('../hosts.xlsx')
