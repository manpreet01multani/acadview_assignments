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


def factorial(number):
    product=1
    for i in range(number):
        product=product*(i*1)
    return product
user_input=int(input("enter the number:"))
factorial_of_user_input = factorial(user_input)
print (factorial_of_user_input)


print("Factorial is:")


#find the perfect number


def perfect (n):
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