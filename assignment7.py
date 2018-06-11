# calculate the area of circle.

pi=3.14
def area(radius):
    area=round(pi*radius*radius)
    return area
m=int(input("enter the radius of circle"))
print("the area of circle is",area(m))

#find power of other number

def power(base,exp):
    if exp==1:
        return(base)
    if exp !=1:
        return(base*power(base,exp-1))
base=int(input("enter base:"))
exp=int(input("enter the exponential value:"))
print("Result:",power(base,exp))

#find factorial and store in dictionary

def factorial(n):
 if n==1:
     return 1
 else:
     return n * factorial(n-1)
print(factorial(5))
dict={}
dict[5]=factorial(5)
dict[4]=factorial(4)
dict[3]=factorial(3)
print(dict)

#find the perfect number


def perfect(n):
 sum=0
 for i in range(1,n):
    if n%i==0:
      sum=sum+i
 if sum==n:
    return True
 else:
    return False
# calling method in for loop
for i in range(1,1000):
 if perfect(i):
  print(i)

 # print  table 0f 12

def table(n):
 n=12
 for i in range(1,11):
     print(n,'x',i,'=',n*i)
table(12)