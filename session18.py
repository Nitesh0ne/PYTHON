class Student:
    """This class is  made for student"""
    def __init__(self):
        self.name = "MyName"
        self.Roll = 1234
    
    def talk(self):
        print("Print Name :", self.name)
        print("Print Roll Number :", self.Roll)

s = Student()
