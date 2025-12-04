class Student:
    school_name = "Balmandir Secondary School"
    def __init__(self, name):
        self.name = name

        print(self.name)
        #access class variable inside constructor using self variable
        print(self.school_name)
        #access class variable inside constructor using class name 
        print(Student.school_name)
    

s1 = Student("Nitesh")

print("Outside class")
print(s1.school_name)

