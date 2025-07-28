# # List

# a = [1,1,2,3,4,5,6,"hello"]
# print(a)

# a.append("Namaste")
# print(a)

# a.remove("Namaste")
# print(a)


# b = eval(input("Enter the list:"))
# print(b)
# print(type(b))




# converting range into list 
r = list(range(1,11))
print(r)
print(type(r))

# converting string into list 

str = list("python")
print(str)
print(type(str))


c = "My  name is nitesh".split()
print(c)
print(type(c))



# Accessing the element of the list
# 1. Indexing 2. slicing 

d = [1,2,3,4,5,6,7,8,9]

# slicing
# print(d[::-2])


# list vs mutability 
# list is mutable 

# print(d)
# print(id(d))

# d.append("ten")
# print(id(d))

# for x in d:
#     print(x)


print(len(d))
print(d.count(1)) 