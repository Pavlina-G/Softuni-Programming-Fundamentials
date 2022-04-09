word = input()
list = []

for i in range(len(word)):
    if word[i].isupper():
        list.append(i) # .append() - add something to a list(string, number, object, list)
print(list)

# Python List append() Method

# Example
# Add an element to the fruits list:

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

# Definition and Usage
# The append() method appends an element to the end of the list.
#
# Syntax
# list.append(elmnt)

# More Examples
# Example
# Add a list to a list:

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
