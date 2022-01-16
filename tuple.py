"""
    Student ID = 20CE053
    Student Name = Smit Mataliya
    a. Write a Python program to create a tuple with different data types.
    b. Write a Python program to create a tuple with numbers and print one item.
    c. Write a Python program to add an item in a tuple.
    d. Write a Python program to convert a tuple to a string.
    e. Write a Python program to find the length of a tuple.
    
    GITHUB REPORSITORY LINK = https://github.com/smitmataliya/Practical-2.git
"""

# A. Write a python program to create a tuple with different data types.

tuple1 = (10,27,55,43,31)
tuple2 = ("Hello", "Python")
print(tuple1)
print(tuple2)

# B. Write a python program to create a tuple with numbers and print one item.

tuple = (1,2,3,4,5,6,7)
print("The number is : ",tuple[2])

# C. Write a python program to add an item in a tuple

tuple = (1,2,3,4,5)
tuple = tuple + (6,7,8)
print(tuple)

# D. Write a python program to convert a tuple with to a string

tuple = ('S' , 'M' , 'I' , 'T')
str = ''.join(tuple)
print("The String is: ",str)

# E. Write a program to find the length of the tuple

tuple = ('S','M','I','T')
print("Length of the tuple:", len(tuple))