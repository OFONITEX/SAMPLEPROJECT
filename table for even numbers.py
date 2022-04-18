# arithmetic operator of % to get the reminder
i = 6
i%2


# print a table for even numbers only

for i in range (1,20,1):
    if (i%2) != 0:
        continue
    
    for j in range (1,11,1):
        result= i * j
        print(result, end=" ")
    print("")
    
# print a table for first 10 numbers 

for i in range (1,20,1):
    
    if i > 10:
        break
    
    for j in range (1,11,1):
        result = i * j
        
        print(result, end=" ")
    print("")