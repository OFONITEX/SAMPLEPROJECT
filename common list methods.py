
# accept the list elements until user enters zero

varT = True
num_list = []

while varT:
    num = int(input("please enter a number : "))
    
    if num == 0:
        varT = False
    else:
        num_list.append(num)
        

# number of elements in a list
 len(num_list)

# concatenate the lists
list2 = [45, 15, 35]

conlist = num_list + list2

num_list = num_list + list2

# extend method (similar to concatination)
num_list.extend (list2)

# calculate the average of all numerical elements in the list

average = sum(num_list) / len(num_list)

# sort the content of the list
num_list.sort() #ascending order

num_list.sort(reverse=True)

# index method to know the index position ofan element
# only returns the first index value
# returns valueerror if num not found
snum = int(input("please enter the number to search for : "))

position = num_list.index(snum)

print("we have found the number {} at index position {}".format(snum, position))











