# string data type
var_str = "my name is ofonmbuk"
print(var_str)

# assign multiple string to a variable

# 1. using triple quotes
var_str2 = """my name is ofonmbuk.
i'm a python programmming student"""
print(var_str2)

# 2. using new line character
var_str3 = "my name is ofonmbuk. \ni'm a python programmming student"
print(var_str3)

# string as an array of characters or collection of characters
# string indexing and slicing

var_str4 = 'my name is ofonmbuk'
#index pos  012345678901234567

# access using the index position
print(var_str4[0])

# access range of characters or slicing of the string
print(var_str4[3:7])

# access using the negative index that starts at the end
print(var_str4[-6:-2])


# basic string operators

# concatenation of strings
var1 = "hello"
var2 = "world"

var3 = var1 + " " +var2
print(var3)

# search for a substring using in and not in
"hello" in var3

"hello" not in var3

# formatting of the string using %
print("my name is %s an my age is %i "%("ofonmbuk", 30))

# raw string operator using r
var1 = r"c:\user\test.data"

print(var1)