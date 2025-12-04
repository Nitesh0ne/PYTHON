class EmptyClass:
    pass

class Student:
    """This class is  made for student"""
    def __init__(self): # _-init__ is the python constructor 
        self.name = "MyName"
        self.Roll = 1234
    
    def talk(self):
        print("Print Name :", self.name)
        print("Print Roll Number :", self.Roll)

# print(Student.__doc__) # print doc string
# help(Student)
s1 = Student()
print(s1.name)
print(s1.Roll)
