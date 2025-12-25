## File Handling 

# f = open("abc.txt","r")
# print("This file that is opened : ", f.name)
# print("This file that is opened : ", f.mode)
# print("This file that is opened : ", f.closed)
# print("Is file readable ?", f.readable())
# print("Is file Writable ?", f.writable())


# f.close()
# print("This file that is opened : ", f.closed)

# Writing  Data to the text file  

f= open("abc.txt","w")
# f.write("Nitesh \n")
# f.write("Nitesh \n")
# f.write("Nitesh \n")
# f.write("Nitesh \n")
# f.writelines("Nitesh nepali")

# f.close()

list = ["Vaskar", "Dipesh", "Aayush"]
f.writelines(list)
# print("Writen in file successfully")
