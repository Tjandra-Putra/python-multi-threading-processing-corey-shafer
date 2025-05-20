# why threading? need to speed up program, running different tasks at the same time
# CPU bound vs IO bound
# CPU bound: CPU crunching numbers
# IO bound: waiting for something to happen, like a file to be read or a network request, downloading a file
# IO File --> a lot of time waiting for something to happen

import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done sleeping...")


do_something(1)
do_something(1)

finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} second(s)")
