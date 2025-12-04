'''
# import math
# print(dir(math))
# # print(help(math))
# help(math.pi)

# import random 

# # for i in range(10):
# #     print(random.random())
# # print(random.randint(1,6)) # print the random  number between 1 to 6 (inclusive)

# # print(random.uniform(1,10))
# print(random.randrange(10))
# print(random.randrange(1,10))
# print(random.randrange(1,10,2))


# program to  generate otp number (6 number)

from random import * 

# # for i in range(10):
# #     print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')
# otp=''
# for i in range(6):
#     otp = otp + str(randint(0,9))
# print(otp)
# generate fake employe data 

alphabets   = "abcdefghijkmnopqrstuvwxyz"
digit       = '0123456789'
cities      = ["ktm","pkr","htd","chitwan","butwal"]
designation = ["Software Engineer", "Team Lead", "Project Manager"]


def get_fake_name():
    name= choice(alphabets).upper()
    n = randint(2,9)
    for i in range(n):
        name= name + choice(alphabets)
    return name



def get_fake_e_num():
    e_num = 'e_'
    for i in range(4):
        e_num = e_num + choice(digit)

    return e_num



def get_fake_salary():
    esal = uniform(10000,50000)
    return esal


def get_fake_city():
    city = choice(cities)
    return city 

def get_fake_m_no():
    m_no = choice ("6789")
    for i in range(9):
        m_no = m_no + choice(digit)
    return m_no




print("Employee Records")

for i in range(9):
    print("Employee Name           : ", get_fake_name())
    print("Employee Number         : ",get_fake_e_num())
    print("Employee City           : ",get_fake_city())
    print("Employee Mobile Number  : ",get_fake_m_no())
    print("Employee Salary         : ",get_fake_salary())
    print()
'''
#---------------------------------------------------

# Python package 


