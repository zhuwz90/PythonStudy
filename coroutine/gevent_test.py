from gevent import spawn, joinall, monkey

monkey.patch_all()

import time
import threading


run_times = 100000

def task(pid):
    """
    Some non-deterministic task
    """
    time.sleep(2)
    if pid % 1000 == 0:
        print('Task %s done' % pid)


def synchronous():
    for i in range(run_times):
        task(i)


def asynchronous():
    g_l = [spawn(task, i) for i in range(run_times)]
    joinall(g_l)


def multithread():
    threads = []
    for i in range(run_times):
        t = threading.Thread(target=task, args=(i,))
        threads.append(t)

    for i in range(run_times):
        threads[i].start()

    for i in range(run_times):
        threads[i].join()


if __name__ == '__main__':
    # print('Synchronous:')
    # start = time.time()
    # synchronous()
    # end = time.time()
    # print(end - start)

    print("*" * 20)
    print('Asynchronous:')
    start = time.time()
    asynchronous()
    end = time.time()
    print(end - start)

    # print('*' * 20)
    # print('multithread:')
    # start = time.time()
    # multithread()
    # end = time.time()
    # print(end - start)

