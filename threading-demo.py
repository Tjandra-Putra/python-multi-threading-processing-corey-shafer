# why threading? need to speed up program, running different tasks at the same time
# CPU bound vs IO bound
# CPU bound: CPU crunching numbers
# IO bound: waiting for something to happen, like a file to be read or a network request, downloading a file
# IO File --> a lot of time waiting for something to happen

import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done sleeping...")


threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()  # wait for thread to finish


# # threads
# t1 = threading.Thread(target=do_something, args=[1])
# t2 = threading.Thread(target=do_something, args=[1])

# # start threads
# t1.start()
# t2.start()

# # making sure threads finish before moving on to calculate the time
# t1.join()  # wait for thread to finish
# t2.join()  # wait for thread to finish

finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} second(s)")
