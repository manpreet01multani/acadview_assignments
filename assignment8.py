# 1. what is time tuple
# which contains nine tuple.

# 2.write a program to get formatted time.

import time
ti = time.gmtime()
print("time calculated using asctime()is:",end ="")
print(time.asctime(ti))

#Extract month from time

import  datetime
from datetime import date
d = date.today()
print(d)
print(d.month)

#Extract day from time

import  datetime
from datetime import date
d = date.today()
print(d)
print(d.day)

##Extract date from time

import  datetime
from datetime import date
d = date.today()
print(d)
print(d.day)

# print localtime method.

import time
ti = time.gmtime()
print("time calculated using ctime()is:",end ="")
print(time.ctime())

# find factorial of a number.

import math
print(math.factorial(9))

#find the gcd of number.

import  math
print(math.gcd(2,6))

#use of os package:
#get current working directory.

import os
print(os.getcwd())

#get the user environment.

import  os
print(os.environ)

