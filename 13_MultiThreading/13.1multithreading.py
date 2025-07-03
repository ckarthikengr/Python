## Multithreading
## when to use multi threading
### I/O bound taks: Tasks taht spend more time waiting for I/P operations (e.g, file operation)
## concurrent execution: Whenyou want to improve the throughput of your application by parallel execution

import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for  letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")


## create 2 threads
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)

start_time=time.time()
t1.start()
t2.start()


##wait forthe thread to complete
t1.join()
t2.join()
#print_number()
#print_letter()
finished_time=time.time()-start_time

print(f"Finished time {finished_time}")
