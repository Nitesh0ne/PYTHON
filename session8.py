# FLOW CONTROL IN PYTHON 
# 1. Conditional Statment
# 1.1 if Statement


# name = input("Enter a name: "
# if name == "hhhh" :
#     print("Name is  on the list")
# else:
#     print("Name is  not in the list")

# num1 = eval(input("Enter the first number "))
# num2 = eval(input("Enter the second number "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")

# elif num2> num1:
#     print(f"{num2}  is greater than {num1}")

# WAP to find smallest of given 2 numbers
# WAP to find smallest of given 3 numbers
# WAP to find given number is odd or even

# Switch statement 

# sub = input("Enter  a fav sub of Engineering :")

# # match sub:
# #     case "DSA":
# #         print("")
# #     case "MAth":
# #         print("")
# #     case _:
# #         print("no subject")


# switch statement 

# subject= input("Enter your favour subject : ")

# match subject:
#     case "Network":
#         print(f"Your favourite subject is {subject}")
#     case "Programming":
#         print(f"Your favourite subject is {subject}")
#     case "Linux":
#         print(f"Your favourite subject is {subject}")
#     case "CEH" :
#         print(f"Your favourite subject is {subject}")
#     case _:
#         print("You subject is not in the list ")

# using Switch case 
words_upto_19 = ["zero", "one", "two", "three", "Four", "five", "Six", "Seven", "eight", "nine", "ten", "eleven", "twleve", "thirteen", "Fourteen", "Fifteen", "sixteen", "Seventeen", "eighteen", "Nineteen"]

words_for_tens = ["","", "twenty", "thirty", "fourtey", "fiftey", "Sixtey", "Sventy", "eighty"]


n = int(input("Enter any number : "))

if n == 0:
    output= "zero"
elif n<=19:
    output= words_upto_19[n]
elif n<=99:
    output = words_for_tens[n//10]+" "+words_upto_19[n%10]

print(output)