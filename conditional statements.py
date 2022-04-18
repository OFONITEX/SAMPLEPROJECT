# basics of onditional statements - if-else statements

# accept the input from the user

salary = int(input("please enter your salary :"))
if salary > 5000:
     print("congratulations. loan approved")
else: 
    salary < 5000
    print("sorry, loan not approved")


# short-hand if statement

salary = int(input("please enter your salary :"))
if salary > 5000: 
    print("approved")
   
# short-hand if-else statement
print("approved.") if salary > 5000 else print("not approved") 


# use of boolean variable in if-else
var1 = True

if var1:
    print("value is true")
else:
    print("value is false")
    
    
# check whether the variable is empty

var_str = "python"

if var_str:
    print("this variable is neither empty nor zero")

    # or
    
var_str = 0

if var_str:
    
    print("this variable is neither empty nor zero")
else:
    print("this variable is empty")
   
    
# pass in an if statement
# dont do anything if there is value else display error

var_str = 10

if var_str:
    pass
else:
    print("this variable is empty.")
    
    
# nested if-else as well as elif

# accept the salary from the user.
salary = int(input("please enter the salary : "))

# if-else conditions
if salary >= 7000:
    print("the loan is approved.")
else:
    if salary >= 5000:
        print("goes for manual approval.")
    else:
        print("sorry, your loan is rejected.")
    

# use of elif
    
if salary >= 7000:
    print("the loan is approved.")
elif salary >= 5000:
    print("sent for manual approval.")
else:
    print("sorry, your loan is rejected.")  
    
    
    
    
    
    
    
    
    
    
    
    
    