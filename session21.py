# class Test:
#     def __init__(self):
#         print("This is the constructor")
#     def __del__(self):
#         print("This is the destructor")

    
# t = Test()
# t = None
# print("End oa Application")

# accessing  a member of one class  into another class
### Composition #####
# class Engine:
#     a = 10 
#     def __init__(self):
#         self.b = 20 
#     def m1(self):
#         print("this is engine")

# class Car:
#     def __init__(self):
#         self.engine = Engine() # creating the object of Engine Class no need of self refrence variable
#     def m2(self):
#         print("car object using engine object")
#         print(self.engine.a)
#         print(self.engine.b)
#         print(self.engine.m1())

# c = Car()
# c.m2()


# another method

# class Car:
#     def __init__(self,name,model,color):
#         self.name = name
#         self.model = model
#         self.color = color
#         pass
#     def getinfo(self):
#         print(f"Car Name : {self.name} \n Car model : {self.model} \n Car color : {self.color}")
    
# class Employee:
#     def __init__(self,ename,eno,car):
#         self.ename = ename 
#         self.eno = eno
#         self.car = car 
#     def empinfo(self):
#         print("Employee Name:",self.ename)
#         print("Employee Number:",self.eno)
#         print("Employee Car Infor:")
#         self.car.getinfo()       
              
# c = Car("Tesla", "V2", "Black")
# e = Employee("Nitesh", "1234", c)
# e.empinfo()
