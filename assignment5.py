#Take an input year from user and decide whether it is a leap year or not.

year = int(input("enter year: "))

if year % 4 == 0 and year % 100 != 0 :
    print(year,"is a Leap year ")
else:
     print(year,"is not leap year :")

#check the dimensions are of square or rectangle.

l = int(input("enter the length:"))
b = int(input("enter the breadth:"))

if l == b :
    print("dimension of square: ")
else:
    print("dimension of rectangle")

#determine oldest and youngest among them.

print("enter first age:")
first = input()
print("enter second age:")
second = input()
print("enter third age:")
third = input()

if first > second and first > third:
    print("oldest is",first)
else:
    print("youngest is",first)
if second > first and second > first:
    print("oldest is",second)
else:
    print("youngest is",second)
if third > first and third > first:
    print("oldest is",third)

#a competitor know which of these prizes they won based on the number of points they scored

num = int(input("insert a number"))

if num > 51 and num <= 150:
    print("congratulations! you won wooden dog")
elif num > 151 and num <= 180:
    print("congratulation! you won book")
elif num >181 and num <= 200:
      print("congratulations! you won chocolates")
else:
    print("no any prize")

#print total cost after getting discount.

quantity = int(input("enter quantity "))

if quantity*100 > 1000:
    discount = (0.1*quantity*100)
    print("getting discount")
    cost = (quantity*100) - (0.1*quantity*100)
    print("total cost",cost)
else:
    print("No discount")








