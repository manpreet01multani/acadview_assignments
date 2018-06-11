#Take 10 integers from user and print it on screen.

count = 0
while(count< 9):
    print ('the count is',count)
    count = count+1

#Write an infinite loop.

count = 0
while True:
    print(count)
    count += 1
    if count == 7:
        break

# create  a user defined dictionary

dict = {}
for i in range(1,3):
    name = input("enter the name:")
    dict[name] = input("enter the age:")
print(dict)

# print pattern

n = input("enter the number of rows")
for i in range(1, 5):
  for j in range(1, i+1):
    print("* ", end = " ")
  print()

# Square of list integer.

l = []
for x in range(0,5):
 l.append(int(input("enter the list elements: ")))
 l1 = []
for x in l:
 l1.append(x*x)

print(l)
print(l1)

# Select and remove element from list.

list=[1,2,3,4,5]
l= int(input("enter the value to delete"))
for x in list:
  if  x ==l:
    list.remove(x)
for x in list:
 print(x)

# print even and odd numbers.

l=[]
l1=[]
for i in  range(1,101):
    if i%2==0:
      l.append(i)
    else:
       l1.append(i)
print(l)
print(l1)

# Arrange separate list  for integer, strings and float.

l = [1,2,'Ram', 4.5]
intl=[]
strl=[]
floatl=[]
for x in l:
  if type(x)==int:
    intl.append(x)
  elif type(x)==str:
    strl.append(x)
  else:
    floatl.append(x)
print(intl)
print(strl)
print(floatl)








