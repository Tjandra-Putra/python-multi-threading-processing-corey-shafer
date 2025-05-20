# why threading? need to speed up program, running different tasks at the same time
# CPU bound vs IO bound
# CPU bound: CPU crunching numbers
# IO bound: waiting for something to happen, like a file to be read or a network request, downloading a file
# IO File --> a lot of time waiting for something to happen

import threading
import time

start = time.perf_counter()

SLEEP_TIME = 1.5  # seconds
THREADS = 10  # number of threads to create


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done sleeping...")


threads = []

for _ in range(THREADS):
    t = threading.Thread(target=do_something, args=[SLEEP_TIME])  # takes the target function and the arguments for that function to pass to it
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()  # wait for thread to finish before moving on to calculate the time


finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} second(s)")
