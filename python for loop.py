# python for loop

name = input("please enter the name : ")

i = 1

for letters in name:
    print ("character number {} is {} ,".format(i, letters))
    
    i += 1


# using range in loops

for i in range(1,10,2):
    print(i)



#  using range in for loop

 name = input("please enter the name :")
 
 # i goes from 0 index until end of the string
 
 length = len(name)

for i in range(0, length, 1):
    print("character number {} is {} ".format(i+1, name[i]))
    
    
# for loops using enumerate
name = input("please enter the name :")

# run the for loop using enumerate
for i, letters in enumerate(name, start=1):
    print("character number {} is {} ".format(i, letters))
