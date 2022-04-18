# use of nested loop for creating the table of numbers from 1 to 19

# i, j for cross table numbers 

for i in range (1,20,1):
    print("") #prints every new iteration in a new line 
    for j in range (1,11,1):
        result = i * j
        print (result, end=" ") #prints the next result on the next line with space
        
        

