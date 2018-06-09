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

# create a list and square of it in another list

integer = []

for x in range(0,6):
    print("enter the integer",integer)

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

