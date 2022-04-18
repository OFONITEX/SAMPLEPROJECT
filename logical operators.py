# logical operators of and, or


# accept the input

# and

salary = int(input("please enter your salary : "))

age = int(input("please enter your age : "))

print("")

if salary >= 7000 and age>= 45:
    print("auto approved.")
else:
    print("approve manually.")
    
    # or
salary = int(input("please enter your salary : "))

age = int(input("please enter your age : "))

print("")
if salary >= 7000 or age>= 45:
    print("auto approved.")
else:
    print("approve manually.")