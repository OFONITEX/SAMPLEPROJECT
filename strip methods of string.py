# strip(), lstrip() and rstrip()
var4 = "John   ,M,42,  8000  ,  software Developer\n"
name, gender, age, salary, role = var4.split(sep=',')

name = name.strip()

role = role.strip('\n')

# lstrip -leading or left
# rstrip - right or trailing

rstrip = name.rstrip()
lstrip = salary.lstrip()


































