#parent class
class Parent:
    a =10 
    def hello(self):
        print("Hello World")

# child class
class Child(Parent): # inheriting the property of the parent class to the child class 
    pass


c1 = Child() # creating the object c1 of Child cals

print(c1.a) # accessing the property of the parent class through the object of child class ==> that is inheritance
print(c1.hello())


# another example 

class Person: # Person is parent class
    def  __init__(self,name,age):# constructor
        self.name = name
        self.age = age
    def eat(self):
        print("Person can eats momo, chowmien")

class Employee(Person): #person is a employee (IS_A Relation) , employee is child class
    def __init__(self, name, age, eno, esal):
        super().__init__(name,age)
        self.name = name 
        self.age = age 
        self.eno = eno 
        self.esal =  esal
    
    def work(self):
        print("Employee can do work")
    
    def empinfo(self):
        print("Emolyee Name ", self.name)
        print("Emolyee Age ", self.age)
        print("Emolyee  Number", self.eno)
        print("Emolyee salary ", self.esal)

e1 = Employee("Nitesh", 25, "1234567890", 25000)
e1.eat()
e1.work()
e1.empinfo()