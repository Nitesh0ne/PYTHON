# tuple

t1 = 10,20,30,40,
print(type(t1))
print(t1)
t2 = () 
print(type(t2))
t3 =(1,) # single value  tuple comma is must
print(type(t3))


list= [1,2,3,4,6]
t5 = tuple(list)
print(type(t5))


#Accessing  the tuple element 

t6 = (0,1,2,3,4,5,6,7,8,9)

print(t6[:])
print(t6[0:])
print(t6[:-1])
print(t6[0:-1:2])


# Some Important Function of tuple

print(len(t6))