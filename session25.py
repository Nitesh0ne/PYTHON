# Polymorphism 

# 1.overloading
# A. Operator Overlaoding


# class Book:
#     def __init__(self, pages):
#         self.pages  = pages

# b1 = Book(200)
# b2 = Book(200)


# class Student:
#     def __init__(self,name,roll_number,marks):
#         self.name = name
#         self.roll_number    = roll_number
#         self.marks = marks
    
#     def __str__(self):
#         return f"this is {self.name} {self.roll_number} object"


# s1 = Student("Pragyan",102,99)
# s2 = Student("Pragyan",202,100)

# print(s1)
# print(s2)



class Book:
    def __init__(self,pages):
        self.pages = pages
    
    def __add__(self,other):
        return Book(self.pages+other.pages)
    
    b1 = Book(100)
    b2 = Book(200)
    b3 = Book(300)

# overriding 
# Ducktyping