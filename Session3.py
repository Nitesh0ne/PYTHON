# complex number
# complex number in the form of a + bj where a and b is real number and j is imaginary part 
# note : imaginary  part should be represented by j or J only 


# a = 2 + 3j
# b = 0b10101 + 3j
# print(a)
# print(type(a))
# print(a.imag) # imaginary part 
# print(a.real) # Real Part


# Boolean Data type 

# a = True  # true 
# a = 1      # true
# a = 10      # true
# a = None  # false
# print(bool(a))
# print(type(a))

# String Data type 

# str1 = "This is string"
# str2 = 'This is string'
# str3 = '''This is string'''
# str4 = '''4df'''
# print("all the format i acceptable",str1)
# print("all the format is acceptable",str2)
# print("all the format is acceptable",str3)
# print("all the format is acceptable",str4)

# str5= '''Learning python 
# is fun
# '''
# print("all the format is acceptable",str5)

# Slicing of string
# a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print("Alphabet letter ",a)
# count = 0
# for i in a : 
#     count = count + 1

# print("Total alphabet is  : ",count)

# ind = len(a)-1
# print(a[0].lower()+a[ind].lower())

# type conversion

# type converion of fundamental data type : int, float, complex, bool, string, complex
a = 10 # integer
print(float(a)) # coverting into float
print(complex(a)) # converting into complex
print(bool(a)) # converting into boolean 
print(str(a)) # converting into string
print(float(a)) # converting into float 

b = 10.50 # float
print("Converted b into intger",int(a)) # coverting into integer
print("Converted b into complex",complex(a)) # converting into complex
print("Converted b into boolean",bool(a)) # converting into boolean 
print("Converted b into string",str(a)) # converting into string

print("---------------------------------------------------------")
 
c = 10.5 + 3j # complex
print("complex number cannot be converted into integer")
#  # coverting into integer 
print("complex number cannot be converted into float")
print("Converted b into boolean",bool(c)) # converting into boolean 
print("Converted b into string",str(c)) #


print("---------------------------------------------------------")
 
d = True # boolean
print("Converted b into intger",int(d)) # coverting into integer
print("Converted b into float",float(d)) # converting into float
print("Converted b into complex",complex(d)) # converting into boolean 
print("Converted b into string",str(d)) #


print("---------------------------------------------------------")
 
e = "7" # string
# e - "dfasd" it is not possible  to convert into  int float complex
print("Converted b into intger",int(e)) # coverting into integer
print("Converted b into float",float(e)) # converting into float
print("Converted b into complex",complex(e)) # converting into complex
print("Converted b into bool",bool(e)) # converted into boolean




print("Fundamental Data Type vs Immutability")

a = 100 
print(id(a))


a = 100 # here a new object is created , 
print(id(a))
