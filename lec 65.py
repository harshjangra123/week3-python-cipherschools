 #practice for loop 
# ask user name and count each character
# "Harsh Raj"
# H : 1
# a : 2
# r : 1
# s : 1
# h : 1
#   : 1
# R : 1
# j : 1  
name = input("Enter your name- ")
temp = ""
for i in range(len(name)):
    if name [i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]