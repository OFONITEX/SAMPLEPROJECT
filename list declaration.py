#-------------------------------------------------------------
# initialise and create a list variable using
# 1. initial set of values
# 2. empty square brackets
# 3. list() function 
# 4. by asssigning or copying the existing list.
#-------------------------------------------------------------


# initial set of values

list1 = ["joy", "john", "alia"]
print(list1)

# empty square
list2 = []
print(list2)

# using list function
list2 = list()
print(list2)

# assign the label
list2 = list1
print(list2) 

# copy the content to different location

list3 = list1.copy()
print(list3)


# access the elements of the lists


list1 = ["joy", "john", "alia"]

list1.append("alex")

list3 = list1.copy()

print(list1[2])

print(list3[-1])

# acess the portion or sub list

list1 = ["joy", "john", "alia"]
print(list1[1:2]) # prints from index 1 and stops before index 2


list1 = ["joy", "john", "alia"]
print(list1[1:])  # prints from index one to the last value

list1 = ["joy", "john", "alia"]
print(list1[0:-2])


# negative index range
list1 = ["joy", "john", "alia"]
print(list1[-3:-1]) # prints from -3 but dont include -1


# access all the elements and process the data

for name in list1:
    print(name)
    
# seach an element in the list
sname = input("please enter the name to search. ")

if sname in list1:
    print("we have found the name.")
else:
    print("we have not found the name you were searching for ")
    
    
# add, update and delete elements of a python lists
list1 = ["joy", "john", "alia"]

list1.insert(2, "bob")
print(list1)

# update elements of the list

list1[2] = "Bill"
print(list1)

# delete an element of the list
del list1[2]

# remove
list1.remove("joy")
print(list1)

# pop method
list1.pop(0)
print(list1)

# clear all the elements of the list
list1.clear()























