# 1 list with user defined input
l = []
for i in range(0,5):
    l.append(input("enter value to be appended to the list: "))

print(l)

# 2. append the list to list

a = ['google','apple','facebook','microsoft','tesla']
l.extend(a)
#for x in a:
 #   l.append(x)
print(l)

#3. count an object from list

x = l.count('google')
print (x)

# 4 sort list
l.sort()
print (l)

# 5 merging list
c=[]
a = [5,3,2,5,2,4]
b = [5 ,6,68,67,45,45]
a.sort()
b.sort()
print (a,b)
c.extend(a)
c.extend(b)
c.sort()
print (c)

# 6 implement stack queue in list



# 7 count odd even no. in list

for x in a:
    if x%2==0:
        print("even  no.: ")
    else:
        print("odd no.: ")