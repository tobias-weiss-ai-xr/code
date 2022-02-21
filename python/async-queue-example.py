# https://realpython.com/python-async-features/
import queue
import time

from codetiming import Timer


def task(name, work_queue):
    timer = Timer(text=f'Task {name} elapsed time: {{:.1f}}')
    while not work_queue.empty():
        delay = work_queue.get()
        print(f'Task {name} running')
        timer.start()
        timer.stop()
        yield


def main():
    """A simple async example"""
    work_queue = queue.Queue()

    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    tasks = [task("One", work_queue), task("Two", work_queue)]

    # for t, n, q in tasks:
    #     t(n, q)

    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True


if __name__ == "__main__":
    main()
