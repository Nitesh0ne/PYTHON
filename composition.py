# Car class has Engine object ==> Has A Relation
class Engine:
    a = 10 
    def __init__(self):
        self.b = 20 
    
    def m1(self):
        print("This is Engine")
    
class Car:
    def __init__(self):
        self.engine = Engine() 
    def m2(self):
        print("car onbject using Engine Object")
        print(self.engine.a)
        print(self.engine.b) # member of Engine  class is  
        self.engine.m1


c = Car()

c.m2()


