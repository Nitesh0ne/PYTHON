# # Set in python 
# s = {10,20,30,40}
# # s.pop()
# print(s)



# converting list into  the  dictionary 

rec = {}

n = int (input("Enter the number of students : "))
i = 1

while i <=n:
    name = input ("Enter the name of the student: ")
    marks = input ("Enter the marks of the student: ")
    rec[name]=marksi = i+1

print("The records of the student are :")

for k,v in rec.items():
    print(k,v)