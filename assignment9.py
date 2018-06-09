# 1

class Circle():
 def __init__(self,radius):
    self.radius = radius
 def getArea(self):
    return 3.14*self.radius*self.radius
 def getCircumference(self):
    return self.radius*2*3.14
radius = input("enter radius:")
cir = Circle(radius)
cir.getArea()

# 2
class Student:
 def __init__(self,rollno,age):
     self.rollNo=rollno
     self.name=age
 def display(self):
     print(self.rollNo)
     print(self.name)

roll = input("enter roll number:")
name = input("enter name:")
s=Student(roll,name)
s.display()

#3
class Temperature():
   def convertFahrenheit(self,celsius):
    return(celsius*9/5)+32
   def convertCelsius(self,fehrenheit):
    return(fehrenheit - 32)*5/9
temp=Temperature()
c=temp.convertFahreheit(100)
f=temp.convertCelsius(98.4)
print(c,f)

#4
class MovieDetails:
 def __init__(self,name,artist,year,rating):
     self.name=name
     self.artist=artist
     self.year=year
     self.rating=rating
 def display(self):
    print("A",self.name,"Zoya",self.artist,"had released in",self.year,"with ratings",self.ratings)
 def update(self):
    name=input("enter the movie name:")
    self.name = name
    artist = input("enter the artist name:")
    self.artist = artist
    year = input("enter the year of release:")
    self.year = year
    ratings = input("enter the ratings:")
    self.ratings = ratings
    print("A",self.name,"Zoya",self.artist,"had released in",self.year,"with ratings",self.ratings)
movie=MovieDetails('ABC','XYZ',2000,6.7)
movie.display()
movie.update()

#5
class Expenditure:
 def __init__(self,savings,expenditure):
     self.savings=savings
     self.expenditure=expenditure
 def display_expenditure(self):
     print(self.expenditure)
     print(self.savings)
 def cal_salary(self):
     total=self.savings+self.expenditure
     print("The total salary is",total)
savings=input("enter the savings:")
expen=input("enter expenditure")
exp=Expenditure(savings,expen)
exp.display_expense()
exp.cal_salary()









