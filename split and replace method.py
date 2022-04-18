
# introduction of split method of string

var3 = "John,M,42,8000,software Developer"


name, gender, age, salary, role = var3.split(sep=",")


# check isnumeric before converting and 
# performing numerical operations

salary.isnumeric()

salary = float(salary)


# replace method
var1 = "John plays football. John plays tennis."

print(var1)

varC = input("current value to be replaced : ")
varN = input("please enter the new value : ")
count = input("number of instances to be removed :")

var1.replace(varC, varN, int(count))