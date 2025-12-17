# # super method 


# class P:
#     def m1(self):
#         print("This is Parent Method")

# class C(P):
#     def m1(self):
#         super().m1()
#         print("This is child class")

# c = C()
# c.m1()


# class P:
#     a = 10 # static variable 
#     def __init__(self):
#         self.b = 20 
#         print("Parent  class constructor is called.")
    
#     def m1(self):
#         print("Parent class instance method is called")
    
#     @classmethod
#     def m2(cls): # class method
#         print("Parent  class class method is called")
    
#     @staticmethod
#     def m3(): # static method 
#         print("parent class static method")

# class C(P): # child class inherit P
#     a = 20000 
#     def __init__(self):
#         super().__init__() # called parent class constructor
#         self.b = 30000
#         print("Child class constructor is called")
       
# c = C()
# #print(c.b) 


# class Person:
#     def __init__(self, name, age):
#         self.name   = name 
#         self.age    = age
    
#     def display(self):
#         print("Name : ", self.name)
#         print("Age : ", self.age)

# class Student(Person):
#     def __init__(self, name, age, roll_num, mark):
#         super().__init__(name,age)
#         self.roll_num = roll_num
#         self.mark  = mark 
    
#     def display(self):
#         super.display()
#         print("Roll Number : ", self.roll_num)
#         print("Marks : ", self.mark)
         

# s = Student("Pragyan",20,101,99)
# s.display()

# =========================================================

# class A:
#     def m1(self):
#         print("A class Method")

# class B(A):
#     def m1(self):
#         print("B class Method")
# class C(B):
#     def m1(self):
#         print("C class Method")
# class D(C):
#     def m1(self):
#         print("C class Method")
# class E(D):
#     def m1(self):
#         super(B,self).m1() # called  method of parent oF B i,e A
#         A.m1(self) # called method of A 
#         print("E class Method")

# e = E()
# e.m1()

#Case 1: From child class we are not allowed to access parent class instance varible by super(), compulsory we should use self only
# but we can use super method to access class and static variable


# case 2: From child class constructor and instance method we can access parent class instance static  and class method also constructor by using super()

# case 3: From child class method we cannot access parent  class  instance method and constructor by using super() directly. 
# but indirectly we can access class and static method.

# case 4: In child class static method we are not allowed to use super() generally but we can use in a special way
