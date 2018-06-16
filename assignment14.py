# 1. Write a Python program to count the frequency  a file.

count=0
with open('hello.txt','r',encoding='utf-8') as f:
    for line in f:
        words=line.split()
        count += len(words)
print("number of words:")
print(count)

# 2. Write a Python program to copy the contents of a file

with open ('hello.txt','r',encoding='utf-8') as f:
    with open('me.txt','w',encoding='utf-8') as f1:
        for line in f:
            f1.write(line)

#3.Write a Python program to combine each line from first file.

with open('hello.txt','r',encoding='utf-8')as f ,open('me.txt','r',encoding='utf-8')as f2:
    for line1,line2 in zip(f,f2):
        print(line1+line2)

#4.WAP of python to perform read and sorting of 10 random numbers.

import random
with open('me.txt','w')as f:
 for i in range(int(input("enter the numbers"))):
     line=str(random.randint(1,10))
     f.writelines(line+'\n')
     print(line)
with open('me.txt')as f1:
    lines=f1.read().splitlines()
lines.sort()
with open('band_sorted.txt','w',encoding='utf-8')as f2:
 for i in lines:
    f2.write(str(i)+ '\n')

#5.Write a Python program to read last n lines of a file.

myvar=open('hello.txt','r',encoding='utf-8')
line=myvar.readlines()
myvar=line[len(line)-1]
print(line[4:6])
myvar.close



