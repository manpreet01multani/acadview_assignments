# 1 find length of tuple
x = ('1','2','3','4','5','6')
print(len(x))

# 2 find largest and smallest element

print ("maximum "+max(x))
print ("minimun "+min(x))

# 3 product of all the elements of the tuple
a = (4,5,6,7,7)
prod = 1
for i in a:
    prod = prod*i
print(prod)

'''
Q4 Create two set using user defined values. 
    1. Calculate difference between two sets.
    2. Compare two sets.
    3. Print the result of intersection of two sets.
'''
#calculate difference between two sets.
setx = set (["mango","bnana"])
sety = set(["apple","mango"])
setb = setx - sety
print(setb)

#compare two sets.

setc = setx & sety
print(setc)
if setx==setc:
    print("sets are same")
else:
    print("sets are not same")

#print result of intersection of two sets

setd = setx & sety
print(setd)

# Create a dictionary to store name and marks of 10 students by user input.

dict = {}
for i in range(1,4):
    name = input("enter student name: ")
    dict[name]=input('enter student marks: ')
print(dict)

# sorting dict
import operator
sorteddict = sorted(dict.items(), key=operator.itemgetter(1))
print (sorteddict)

# count in MISSISSIPP

s = 'MISSISSIPP'

l = [x for x in s]
print(l)
for x in l:
    print("count of %s is %d"%(x,l.count(x)))