import multiprocessing
import time
import random
from datetime import datetime


def wait_and_print_time():
    # Wait for a random number of seconds between 0 and 1
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)

    # Print the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(
        f"Process {multiprocessing.current_process().name} finished after waiting {wait_time:.2f} seconds. Current time: {current_time}"
    )


if __name__ == "__main__":
    # Create three processes
    processes = []
    for _ in range(3):
        process = multiprocessing.Process(target=wait_and_print_time)
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()
