#  check membership using if statement

string = "python programming is fun."

sub = input("please enter the key word to search : ")

print ("")

if sub not in string:
    print("the search result is positive.")
else:
    print("the search result is empty.")
        