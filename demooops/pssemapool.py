import threading
import logging
from time import sleep
"""http://collabedit.com/xhgk6"""
logging.basicConfig(format='%(threadName)s : %(message)s')


class Pool:
    """semaphore pool"""

    def __init__(self):
        self.sema_pool = list()

    def add_to_pool(self, thread_name):
        self.sema_pool.append(thread_name)
        logging.warning('added to the pool : {}'.format(self))

    def remove_from_pool(self, thread_name):
        self.sema_pool.remove(thread_name)
        logging.warning('removed : {}'.format(self))

    def __str__(self):
        return str(self.sema_pool)


def task_set(semaphore_pool, sema_obj):
    """child threads"""
    sleep(1)
    t_name = threading.currentThread().name
    logging.warning('waiting to join : {}'.format(semaphore_pool))

    with sema_obj:
        semaphore_pool.add_to_pool(t_name)
        sleep(1)
        semaphore_pool.remove_from_pool(t_name)


def main():
    """main thread"""
    pool = Pool()
    sema = threading.Semaphore(3)

    for _ in range(9):
        threading.Thread(target=task_set, args=(pool, sema)).start()

    for t in threading.enumerate():
        if t is not threading.currentThread():
            t.join()


if __name__ == '__main__':
    main()
