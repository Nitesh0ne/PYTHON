a= input("Enter the  first number") 
b= input("Enter the  second number") 
c= input("Enter the  third number") 

if a>b and a > c :
    print(a,"is greater number than ",b,"and",c)
elif b> c :
    print(b, "is greater than ",a,"and",c)
else:
    print(c, "is greater than ",a,"and",b)
