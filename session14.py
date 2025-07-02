# def hello(fname,lname): # fucntion defination
#     print(f"Hello {fname} {lname}") # function body 

# hello("Nitesh","Nepali") # function call 

# def square(num):
#     print(f"Square of the {num} is", num*num)

# num=eval(input("Enter the  number: "))
# square(num)


# def add(a,b):
#     sum = a+b
#     print(sum)

# print("The sum is :",add(20,10))


# def fact(num):
#     result = 1
#     while num > 1 :
#         result = result * num
#         num = num -1
#     return result 

# print(fact(100))



# Returning two value

# def sum(a,b):
#     add = a+b
#     return add

# sum(20,10) # positional argument , 

# Default argument

def function_name(a, *args):
    print(a)
    print(args)
function_name(10,)