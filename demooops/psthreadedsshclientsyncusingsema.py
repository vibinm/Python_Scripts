"""threaded ssh client"""
"""http://collabedit.com/x96c2"""
import threading
from pssshclient import CustomSSHClient
from pyexcel import get_sheet
import logging
from time import sleep

logging.basicConfig(format='%(threadName)s : %(message)s')
target_file = 'sshresponse.log'


class ThreadedSSHHandler(CustomSSHClient):
    def __init__(self, host, port, user, pwd, job, lock):
        self.job = job
        self.lock = lock
        self.t_name = threading.currentThread().name
        super().__init__(host, port, user, pwd)
        self.task_runner()

    def task_runner(self):
        payload = self.check_output(self.job)
        caption = '{} ran {} @ {}'.format(self.t_name, self.job, self.host)

        logging.warning('checking for the lock')

        with self.lock:
            logging.warning('acquired the lock')

            with open(target_file, 'a') as fw:
                """critical section"""
                fw.write(caption.center(80, '-') + '\n')
                fw.write(payload + '\n')
                sleep(1)
                logging.warning('done with critical section')

            logging.warning('releases the lock')


class ThreadedSSHClient:
    list_of_threads = list()

    def __init__(self, ssh_host_file):
        self.host_file = ssh_host_file
        self.parse_ssh_host_file()

    def parse_ssh_host_file(self):
        sheet = get_sheet(file_name=self.host_file)
        lock = threading.Semaphore(1)  # sync using Semaphore
        # print(lock.locked())
        for ssh_config in sheet:
            ssh_config.append(lock)
            t = threading.Thread(target=ThreadedSSHHandler, args=ssh_config)
            ThreadedSSHClient.list_of_threads.append(t)
            t.start()

        for child in ThreadedSSHClient.list_of_threads:
            child.join()


if __name__ == '__main__':
    ThreadedSSHClient('../hosts.xlsx')
