# a = 10 # global variable

# def f1():
#     a = 20 
#     b =100   # localvariable
#     global c # making local variable  to global variable
#     c = 300 
#     print(b)
#     print(globals()["a"]) # accessing global varaible that name is same as local varibale inside the function
# f1()

# *******Recursive fucntion**********

# program to find factorial number 

# num = int(input("Enter the number : "))

# def fact(num):
#     if num == 0 :
#         result = 1
#     else:
#         result = num * fact(num - 1)
    
#     return result

# print(f"The factorial of {num} is {fact(num)}")
    

# ********** Anonymous function or Lamda function*********

# s = lambda n:n*n # lamda function
# print("The square is : ",s(4))

# max_num = lambda a,b: a if a>b else b 

# print("The maximum number is :", max_num(10,100))


# filter(function, sequence)

# def isEven(n):
#     if n%2 == 0:
#         return True 
#     else:
#         return False

# l = [1,2,3,4,5,6,7,8,9,10]
# l1 = list(filter(isEven,l))
# print(l1)

l = [1,2,3,4,5,6,7,8,9,10]
l1 = list(filter(lambda x:x%2==0,l))
print(l1)



# function aliasing
def hello(name):
    print("Hello", name)

wish = hello # fucntion aliasing
hello("Isha")
wish("nitehs")



# Nested Function

def outer():
    print("Outer function execution.")
    def inner():
        print("Inner function execution")
    print("outer function calling inner funtion")

    return inner


f1=outer()
f1()