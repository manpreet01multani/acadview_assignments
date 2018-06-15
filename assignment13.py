# 1.Name and handle the Exception Occured in a Program
# it is ZeroDivisionError

a=3
if a<4:
 try:
    a=a/(a-3)
 except ZeroDivisionError:
    print("value is not allowed")

# 2.Name and handle the Exception Occured in a Program
#it is Indexerror

l=[1,2,3]
try:
 print(l[3])
except IndexError:
    print("index is not here")

# 3.What will be the output of the following code:
#An exception.

# 4.What will be the output of the following code:
#-5.0
#a/b result in 0

# 5.Try Exception Handling(Import Error,Value Error and Index Error)

l=['a','b','c']
try:
 l=int(input("enter the values"))
except IndexError:
    print("index is not here")
except ImportError:
    print("module is here")
except ValueError:
    print("value is not allowed")

# 6.Create a user-defined exception AgeTooSmallError() that warns the user when they entered age less than 18

class Error(Exception):
    pass
class ValueTooSmall(Error):
    pass
class ValueTooLarge(Error):
    pass

age=18
while True:
  try:
      num=int(input("enter the numbers"))
      if age>num:
         raise ValueTooSmall
      elif age<num:
         raise ValueTooLarge
      break
  except ValueTooSmall:
       print("value is small,repeat")
       print()
  except ValueTooLarge:
       print("value is small,repeat")
       print()
print("you got it")


