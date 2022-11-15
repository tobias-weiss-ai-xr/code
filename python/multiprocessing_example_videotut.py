import logging
import multiprocessing
import random
import time
from multiprocessing.context import Process


def work(item, count):
    name = multiprocessing.current_process().name
    logging.info(f"{name} started: {item}")
    for x in range(count):
        logging.info(f"{name}: {item} = {x}")
        time.sleep(1)
    logging.info(f"{name} finished")
    return item + " is finished"


def proc_result(result):
    logging.info(f"Result: {result}")


def main():
    logging.basicConfig(
        format="%(levelname)s - %(asctime)s: %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
    )

    max = 5
    pool = multiprocessing.Pool(max)

    results = []
    for x in range(max):
        item = "Item" + str(x)
        count = random.randint(1, 5)
        r = pool.apply_async(work, args=[item, count], callback=proc_result)
        results.append(r)

    for r in results:
        r.wait()

    pool.close()
    pool.join()
    logging.info("Finished")


if __name__ == "__main__":
    main()
