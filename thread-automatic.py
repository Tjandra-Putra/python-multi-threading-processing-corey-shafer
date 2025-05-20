# why threading? need to speed up program, running different tasks at the same time
# CPU bound vs IO bound
# CPU bound: CPU crunching numbers
# IO bound: waiting for something to happen, like a file to be read or a network request, downloading a file
# IO File --> a lot of time waiting for something to happen

import concurrent.futures
import time

start = time.perf_counter()

SLEEP_TIME = 1  # seconds
DYNAMIC_SLEEP_TIME = [5, 4, 3, 2, 1]  # seconds
THREADS = 10  # number of threads to create


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done sleeping...{seconds} second(s)"


with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something, SLEEP_TIME)  # schedules function to be executed and returns a future object (to check results, running)
    # print(f1.result())  # blocks until the function is done executing, returns the result of the function

    # dynamic sleeps for testing, different sleep times
    # submit approach
    # results = [executor.submit(do_something, sec) for sec in DYNAMIC_SLEEP_TIME]

    # map approach
    results = executor.map(do_something, DYNAMIC_SLEEP_TIME)  # returns an iterator of results

    for result in results:
        print(result)

    # for fixed sleep times
    # results = [executor.submit(do_something, SLEEP_TIME) for _ in range(THREADS)]

    # get results
    for f in concurrent.futures.as_completed(results):
        print(f.result())  # blocks until the function is done executing, returns the result of the function


finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} second(s)")
