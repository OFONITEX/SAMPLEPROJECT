
# some basic functions and methods applied on string data type

var1 = "programming is easy with python"
#index  0123456789012345678901234567890

# get the length of the string 
len(var1)

# count the number of character or substring
var1.count("i")


# find and index
var1.find("python")
var1.index("python")

# change the case of the string
var1.upper()
var1.lower()

var2 = "python"
print(var2)

var2.ljust(12)
var2.rjust(12)
var2.ljust(12, "o")

# format() method

# the total order value for Mr. Gates is $2000

user_name = "Gates"

order_value = int(input("please enter the order value : "))

# 1. format by sequence
result = "the total order value for Mr. {} is ${}."
result.format(user_name, order_value)


# format by numeric indexes
result = "customer name is Mr. {0}.the total order value for Mr. {0} is ${1}."
result.format(user_name, order_value)


# 3. format by named indexes or keys
result = "the total order value for Mr. {name} is ${value}"
result.format(name = user_name, value=order_value)






















