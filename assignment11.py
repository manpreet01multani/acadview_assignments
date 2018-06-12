# create a threading process.
import time
import threading
from threading import Thread

def sleepMe():
    print("Thread is sleeping",threading.currentThread().getName())
    time.sleep(5)
    print("Thread is awaking", threading.currentThread().getName())
t = Thread(target=sleepMe, args=())
t.start()



# make a thread that prints number.

import time
import threading
from threading import Thread

def sleepMe():
    print("Thread is sleeping",threading.currentThread().getName())
    print("Thread is awaking", threading.currentThread().getName())

for i in range(0,10):
 print(i)
 time.sleep(1)
t = Thread(target=sleepMe, args=())
t.start()

# make a thread for list of five elements.

import time
import threading
from threading import Thread

def sleepMe(i,M):
    time.sleep(M)
    print("thread %i"%(i))
u=[3,7,5,9,8]
M=2
for i in u:
    th=Thread(target=sleepMe,args=(i,M,))
    th.start()
    M+=2

# call factorial function using thread.

import time
import threading
from threading import Thread

def factorial(n):
  fact=1
  while(n>0):
      fact=fact*n
      n=n-1
      print("factorial:", fact)
t = Thread(target=factorial,args=(5,))
t.start()



