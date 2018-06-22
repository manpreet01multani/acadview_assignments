#1.

import numpy as np
a=np.random.rand(10,1)
print(a)
print(np.sum(a)/10)

#2
import numpy as np

a = np.random.rand(10, 1)
print(a)
print(np.var(a))
print(np.std(a))

#3.
import numpy as np

A= np.random.rand(10, 20)
print(A)
B= np.random.rand(20,25)
print(B)
print(A.dot(B))
print(np.dot(A,B))
C=np.random.rand(10,25)
print(C)
print(np.sum(C))

#4.
import numpy as np
A=np.random.rand(10,1)
print(A)
def func(x):
    return(1 / (1+np.exp(-x)))
m=np.apply_along__axis(func,0,A)
print (m)

