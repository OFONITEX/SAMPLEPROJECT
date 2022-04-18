# creat a menu driven phonebook to accept the input from the user 
# to add and search for a contact


# initialize the varibles
varT        = True
sublist     = []
phonebook   = []

# Run the loop. create an outline structure first.
while varT:
    print("")
    print("        Welcome to the phonebook       ")
    print("---------------------------------------")
    print("   Please choose one of the options below. ")
    print("   A - To Add a contact")
    print("   S - To Search a contact")
    print("   E - To Exit the phonebook")
    
    print("This is menu.")
    option = input("option : ")
    
    if option == "E":
        varT = False
        
    elif option == "A":
       name    = input("please enter the name :     ")
       num     = input("please enter the number :   ")
       email   = input("please enter the email ID : ")
    
       sublist = [name, num, email]
        
       phonebook.append(sublist)
       print("the contact {} has been added successfully.".format(name))
        
    elif option == "S":
        sname = input("please enter the name to search for : ")
        found = False
        
        for sublist in phonebook:
            if sname in sublist:
                print("{} is in the phonebook and here are the details.".format(sname))
                print("sublist")
                found = True
                
        
        if not found:
            print("{} is not found in the phonebook.".format(sname))
        
    else:
        print("sorry, you have chosen a wrong option.")