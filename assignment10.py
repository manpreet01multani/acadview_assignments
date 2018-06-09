#1

class Animals:
    def animal_attributes(self,tail):
        print("animals have",tail,"tail")
class Tiger(Animals):
    def tiger_attributes(self,nutrition):
        print("Tiger is",nutrition)
tig=Tiger()
tig.animal_attributes(1)
tig.tiger_attributes('carnivores')

#2

 #AB
 #AB

#3

class Cop:
    def _init_(self,name,experience):
      self.name=name
      self.experience=experience
    def display_details(self):
        print(self.name,"cop is on duty with",self.experience,"years of experience")
    def update_details(self):
        self.name='Sherlock'
        self.experience=4
class Mission(Cop):
    def _init_(self):
         super(Mission,self). _init()
    def display_mission(self,mission):
        print("The active mission is",mission)
    def assign_cop(self,mission):
        print(self.name,"has been assigned",mission)
mission = Mission('Sherlock',9)
mission.display_mission('Secret')
mission.display_details()
mission.assign_cop('secret')

#4
class Shape:
    def _init_(self,length,breadth):
        self.length=length
        self.breadth.breadth
    def area(self):
        print("the area is",self.length*self.breadth,"units")
class Rectangle(Shape):
    def _init_(self):
        super(Rectangle,self)._init_()
class Square(Shape):
    def _init_(self):
        super(Square,self)._init_()
rect=Shape(5,9)
rect.area()
sq=Shape(6,6)
sq.area()

