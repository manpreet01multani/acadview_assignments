# 1.Name and handle exception following condition:
#It is ZeroDivisionError .
a=3
if a<4:
 try:
  a=a/(a-3)
 except ZeroDivisionError:
     print("value is not allowed")

# 2.Name and handle exception following condition:
# It is IndexError.

l=[1,2,3]
try:
   print(l[3])
except IndexError:
    print("cannot find index")

#3.what will be the out[ut of code:
# An exception.

#4.what will be the out[ut of code:
#-5.0
#a/b result in 0

#5. Try excetion handling(import,value and index).


l=[1,2,3]
try:
     print(l[3])
except ImportError:
    print("file not open")
except ValueError:
    print("value is wrong")
except IndexError:
    print("index is incorrect")

#6.Create a user-defined exception AgeTooSmallError() that warns the user when they entered age less than 18
class Error(Exception):
    pass
class  ValueTooSmallError(Error):
    pass
class ValueTooLarge(Error):
    pass

age=18
while True:
  try:
      num=int(input("enter the number"))
      if age>num:
        raise ValueTooSmallError
      elif age<num:
         raise ValueTooLarge
      break
  except ValueTooSmallError:
    print("value is small,repeat")
    print()
  except ValueTooLarge:
    print("value is greater,repeat")
    print()
print("you got it")

