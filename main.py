# This is a comment. It is ignored by the interpreter

# Printing
print("Hola me amigos")
print("I am mayank", 13)

# Variables
var = 1
var321 = "344.444"

# Data Types
## String
string1 = "Hello World!!"
string2 = '11.3'
## Float
float1 = 23.0
## Int
integer1 = -2
integer2 = 5
## Bool
boolean1 = True
boolean2 = False

# Some useful functions
input1 = input("Name: ") ## Getting User Input
ord1 = ord("Z") ## Show the ascii code of a character
len1 = len("hello WOrld djdicbhfalbci") ## Number of items in a list
range1 = range() ## Creates a collection of numbers based on the input we give it

# Arithmetic Operators
multiplication = 1*3
division = 2/23567
addition = 1+2
subtraction = 5-333
exponent = 22**22
percent = 22 % 9

# String methods
hello0 = "hello".upper() # Uppercases the string
hello1 = "hello".upper() # Lowercases the string
hello2 = "hello".capitalize() # Capitalize the string
hello3 = "hello".count("ll") # Count the number of things in the string
hello4 = hello3 + hello1
hello5 = hello4 * 4

# Conditional Opeators
equality1 = "hello"
equality2 = "hello1"
equality = 92 == 2
print(equality1 == equality2) # Check if both things are same

noequality1 = "hello"
noequality2 = "hello1"
print(equality1 != equality2) # Check if both things are not the same

# If/Else/Else If
x = 1
y = 3
z = "9.00344444422133"
if x == 1:
  print("some stuff")
  print("This is 1")
elif y > 3:
  print("Y is greater than three")
  print("more stuff!")
else:
  print("NOTHING IS TRUE.") 

# Lists(Are mutable/Can be changed)
list1 = [111, "Truehola", True, False]
list1.append("5666.00.0") ## Add/Appends a item to a list
list1.extend([1, 2, True, False, "hello World"]) ## Adds/Appends every item from the list to a list
list1.pop(2) ## Remove the last item of the list if the index is not provided
print(list1[1]) ## Print the item of a specific index

# Tuples(Are not mutable/Cannot be changed)
tuple1 = (0,102,0.4,5)

# For Loop
testlist = [0,1,"h", True]
for i in range(len(testlist)):
  print(i)

# While Loop
x = 1
while x == 1:
  print("Hello Python!!")
  x += 1

# Slice Opeator (Works on strings, lists and tuples)
slice1 = [0,1,2,3,4,5,6,7,8,9,10]
sliced = slice1[1:9:3] # Start at 1, Stop at 9 and Increment by 1
sliced2 = slice1[::-1] # This will reverse a list

# Sets (Does not track the indexs and is super fast)
set1 = set() # Use this if you know the set is going to be empty
set2 = {1,2,456,78,"hola"} # Use this if you know the set is not going to be empty
set2.remove("hola") # Remove a element from the set
set1.add(1) # Add a element to the set
print(1 in set1) # Check if that element is in the set
set1.difference(set2) # Difference between two sets
set1.union(set2) # Add to sets
set1.intersection(set2) # Find out the same elements between two sets

# Dicts/Dictioneres
dict1 = {
  "name": "Mayank",
  "age": 13 
}

dict1.values() # No of values in the dictionary
del dict1["name"] # Delete the key
dict1.keys() # No of keys in the dictionary

# Functions
def func():
  print("hello python")
func()

def add(num1, num2):
  print(num1 + num2)
add(1, 2)