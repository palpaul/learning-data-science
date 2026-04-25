str = "Hello"
print(str)
print(type(str))
print(len(str))
print(str[0])  # Accessing the first character
print(str[1:5])  # Slicing the string means getting a substring from index 1 to 4 (5 is exclusive)  
print(str.upper())  # Converting to uppercase
print(str.lower())  # Converting to lowercase
print(str.replace("Hello", "Hi"))  # Replacing a substring example - replacing "Hello" with "Hi"
print(str.split())  # Splitting the string into a list of words example - splitting "Hello World" into ["Hello", "World"]
print(str + " World")  # Concatenating strings example - concatenating "Hello" with " World" to get "Hello World"
print(str * 3)  # Repeating the string example - repeating "Hello" three times to get "HelloHelloHello"
print(str.strip())  # Removing leading and trailing whitespace example - removing whitespace from "  Hello  " to get "Hello"
print(str.startswith("H"))  # Checking if the string starts with "H" example - checking if "Hello" starts with "H" to get True
print(str.endswith("o"))  # Checking if the string ends with "o" example - checking if "Hello" ends with "o" to get True
print(str.find("l"))  # Finding the index of the first occurrence of "l" example - finding the index of "l" in "Hello" to get 2
print(str.count("l"))  # Counting the occurrences of "l" example - counting how many times "l" appears in "Hello" to get 2
print(str.isalpha())  # Checking if the string contains only alphabetic characters example - checking if "Hello" contains only alphabetic characters to get True
print(str.isdigit())  # Checking if the string contains only digits example - checking if "Hello" contains only digits to get False
print(str.isalnum())  # Checking if the string contains only alphanumeric characters example - checking if "Hello123" contains only alphanumeric characters to get True
print(str[0], str[-1])  # Accessing the first and last characters example - accessing the first and last characters of "Hello" to get "H" and "o"
print(str[::-1])  # Reversing the string example - reversing "Hello" to get "olleH" 
print(str[0:2])  # Slicing the string to get the first two characters example - slicing "Hello" to get "He"
print(str[2:5])  # Slicing the string to get characters from index 2 to 4 example - slicing "Hello" to get "llo"
print(str[:2])  # Slicing the string to get every second character example - slicing "Hello" to get "Hlo"
print(str.center(20))  # Centering the string within a width of 20 characters example - centering "Hello" within a width of 20 to get "       Hello        "
print(str.ljust(20))  # Left-justifying the string within a width of 20 characters example - left-justifying "Hello" within a width of 20 to get "Hello               "
print(str.rjust(20))  # Right-justifying the string within a width of 20 characters example - right-justifying "Hello" within a width of 20 to get "               Hello"
print(str.zfill(20))  # Filling the string with zeros to a width of 20 characters example - filling "Hello" with zeros to get "000000000000000Hello"
print(str[2:])  # Slicing the string to get characters from index 2 to 4 example - slicing "Hello" to get "llo"


#string is immutable in python which means once a string is created, it cannot be changed. However, you can create a new string by performing operations on the original string. For example, if you want to change a character in a string, you can create a new string with the desired changes. Here's an example:
original_str = "Hello"
#original_str[0]= "H"  # This will raise an error because strings are immutable
print(original_str)  # Output: "H"


#here we are not modify the original string but creating a new string with the desired changes. We can change the second character to "a" to get "Hallo".
new_str = original_str[:1] + "a" + original_str[2:]  # Changing the second character to "a"
print(new_str)  # Output: "Hallo"
# Attempting to change the first character (this will not work because strings are immutable)   

#method -2 
sttr= "Python"
sttr2= "p"+ sttr[1:]  # Changing the first character to "p"
print(sttr2)  # Output: "python"

#method -3 using replace() method
str3= sttr.replace("P", "p")  # Replacing "P" with "p"
print(str3)  # Output: "python"


######
print("py" in "Python")  # Checking if "py" is a substring of "Python" - outputs False because it's case-sensitive ("Python" contains "Py" not "py"). To get True, convert to lowercase: print("py".lower() in "Python".lower())

print ("Py" not in "Python")  #  Checking if "Py" is not a substring of "Python" - outputs False because "Py" is indeed a substring of "Python". To get True, check for a different substring: print("py" not in "Python") which will output True because "py" is not a substring of "Python".
print("Py" in "Python")  # Checking if "Py" is a substring of "Python" - outputs True because "Py" is indeed a substring of "Python". To get False, check for a different substring: print("py" in "Python") which will output False because "py" is not a substring of "Python".
msg = f"welcome to {str} programming"  # Using an f-string to include the value of str in the message
print(msg)  # Output: "welcome to Hello programming"

print("Hello world".capitalize())  # Capitalizing the first letter of the string - outputs "Hello world"
print("hello world".title())  # Capitalizing the first letter of each word in the string - outputs "Hello World"
print("   Hello World   ".strip())  # Removing leading and trailing whitespace - outputs "Hello World"
print("Hello World".lstrip())  # Removing leading whitespace - outputs "Hello World"    
print("Hello \nworld") # Including a newline character in the 
# string - outputs: 
# "Hello
# world"
print("Hello\tWorld")  # Including a tab space character in the string - outputs: "Hello    World"

print("welcome to \"datascience\"")  # Escaping double quotes inside a double-quoted string: \" represents a literal double quote character, so this prints 'welcome to "datascience"' 

print('It\'s a nice day')  # Escaping single quotes inside a single-quoted string: \' represents a literal single quote character, so this prints "It's a nice day"

print("C:\\Users\\Alice")  # Escaping backslashes in a file path: \\ represents a literal backslash character, so this prints "C:\Users\Alice"  

# boolean data type in python can have only two values: True or False. It is used to represent the truth value of an expression or condition. Boolean values are often used in conditional statements and loops to control the flow of a program based on certain conditions. For example, you can use a boolean variable to check if a user is logged in or not, and then display different content accordingly. Here's an example:
is_logged_in = True  # A boolean variable indicating whether the user is logged in or not
if is_logged_in:
    print("Welcome back, user!")  # This will be printed if is_logged_in is True
else:
    print("Please log in to continue.")  # This will be printed if is_logged_in is False


#true -- 1
#false -- 0
print(bool(1))  # Output: True
print(bool(0))  # Output: False
flag1 = True
flag2 = False
print(flag1)  # Output: True
print(flag2)  # Output: False
print (flag1 +1) # Output: 2 (True is treated as 1, so 1 + 1 = 2)
print(flag2 +1) # Output: 1 (False is treated as 0, so 0 + 1 = 1)
print(True + False) # Output: 1 (True is treated as 1 and False is treated as 0, so 1 + 0 = 1)
print (True * 5) # Output: 5 (True is treated as 1, so 1 * 5 = 5)
print(False * 5) # Output: 0 (False is treated as 0, so 0 * 5 = 0)



age = 18
if age >= 18:
    print("You are an adult.")  # This will be printed if age is greater than or equal to 18    
else:
    print("You are a minor.")  # This will be printed if age is less than 18

print("Adult" if age >= 18 else "Minor")  # This is a ternary operator that returns "Adult" if age is greater than or equal to 18, otherwise it returns "Minor"



#None is a special data type in Python that represents the absence of a value or a null value. 
# It is often used to indicate that a variable has no value or that a function does not return anything. For example, 
# you can use None to initialize a variable that will later be assigned a value, 
# or to indicate that a function does not return any meaningful result. Here's an example:
#None is often used as a default value for function parameters to indicate that the parameter is optional. For example:

#None --> No value /nothing / "empty value"
# 
x = None  # Initializing a variable with None to indicate that it has no value yet
print(x)  # Output: None""
print(type(x))  # Output: <class 'NoneType'>

my_variable = None  # Initializing a variable with None to indicate that it has no value yet
print(my_variable)  # Output: None
def my_function():
    print("This function does not return anything.")  # This function performs an action but does not return a value



my_numbers = [1, 2, 3, 4, 5]  # A list is a collection of items that can be of different data types. It is ordered and mutable (can be changed). Lists are defined using square brackets [] and items are separated by commas. For example, you can create a list of numbers, a list of strings, or a list of mixed data types. Here's an example:
my_list = [1, "Hello", 3.14, True]  # A list containing different data types: an integer, a string, a float, and a boolean
print(my_list)  # Output: [1, 'Hello', 3.14, True]
print(type(my_list))  # Output: <class 'list'>
print(my_list[0])  # Accessing the first item in the list (Output: 1)
print(my_list[1])  # Accessing the second item in the list (Output: "Hello")
print(my_list[2])  # Accessing the third item in the list (Output: 3.14)
print(my_list[3])  # Accessing the fourth item in the list (Output: True)
print(type(my_list[0]))  # Output: <class 'int'> (the type of the first item in the list)
#modify the list by changing the second item to "World"
my_list[1] = "World"  # Modifying the second item in the list
print(my_list)  # Output: [1, 'World', 3.14, True]

#apply loop on list

#its a collection of items that can be of different data types. It is ordered and mutable (can be changed). Lists are defined using square brackets [] and items are separated by commas. For example, you can create a list of numbers, a list of strings, or a list of mixed data types. Here's an example:
#its ordered and mutable (can be changed). Lists are defined using square brackets [] and items are separated by commas. For example, you can create a list of numbers, a list of strings, or a list of mixed data types. Here's an example:
#collection of elemenets that can be of different data types. It is ordered and mutable (can be changed). Lists are defined using square brackets [] and items are separated by commas. For example, you can create a list of numbers, a list of strings, or a list of mixed data types. Here's an example:
 

#its an Hetrogeneous collection of elements that can be of different data types. It is ordered and mutable (can be changed). Lists are defined using square brackets [] and items are separated by commas. For example, you can create a list of numbers, a list of strings, or a list of mixed data types. Here's an example:

#my_list = [1, "Hello", 3.14, True]  # A
# apply loop on list
for item in my_list:
    print(item)  # This will print each item in the list on a new line
    # hoe to store is as an array in python
    # In Python, you can use the built-in list data type to store an array of elements. Lists are dynamic and can hold elements of different data types. Here's how you can create and use a list to store an array of elements:
my_array = [1, 2, "hra", 4, 5]  # Creating a list to store an array of integers
print(my_array)  # Output: [1, 2, "hra", 4, 5]

result = [] # Creating an empty list to store the results
for item in my_list:
    result.append(item)  # This will add each item from my_list to the result list
print(result)  # Output: [1, "Hello", 3.14, True]


# touple is a collection of items that can be of different data types. 
# It is ordered and immutable (cannot be changed). Tuples are defined using parentheses () and items are separated by commas. For example, you can create a tuple of numbers, a tuple of strings, or a tuple of mixed data types. Here's an example:
my_tuple = (1, "Hello", 3.14, True)  # A
print(my_tuple)  # Output: (1, 'Hello', 3.14, True)
print(type(my_tuple))  # Output: <class 'tuple'>
print(my_tuple[0])  # Accessing the first item in the tuple (Output: 1)
print(my_tuple[1])  # Accessing the second item in the tuple (Output: "Hello")
print(my_tuple[-1])  # Accessing the last item in the tuple (Output: True)\


#dictionary is a collection of key-value pairs that can be of different data types.
#  It is unordered and mutable (can be changed).
#  Dictionaries are defined using curly braces {} and key-value pairs are separated by commas.
#  The keys must be unique and immutable (e.g., strings, numbers, or tuples),
#  while the values can be of any data type. Here's an example: 

my_dict = {"name": "Alice", "age": 25, "is_student": True}  # A dictionary containing key-value pairs of different data types
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'is_student': True}
print(type(my_dict))  # Output: <class 'dict'>  

d1={
   "name":"data science",
   "subject": "GEN AI", 
}
print(d1)  # Output: {'name': 'data science', 'subject': 'GEN AI'}
print(d1["name"])  # Accessing the value associated with the key "name" # Output: "data science"
print(d1["subject"])  # Accessing the value associated with the key "subject" # Output: "GEN AI"
#modify the value associated with the key "name"
d1["name"] = "machine learning"  # Modifying the value associated with the key "name"
print(d1)  # Output: {'name': 'machine learning', 'subject': 'GEN AI'}



#SET is a collection of unique items that can be of different data types. 
# It is unordered and mutable (can be changed).
#  Sets are defined using curly braces {} and items are separated by commas. 
# For example, you can create a set of numbers, a set of strings, or a set of mixed data types. 
# Here's an example:
#duplicate values are not allowed in set and it will automatically remove the duplicate values from the set. For example, if you create a set with duplicate values, it will only keep one instance of each value. Here's an example:

my_set = {1, 2, 3, 4, 5, 2, 3}  # A set with duplicate values
# as order are not maintained in set, the output may not be in the same order as the input. The duplicate values 2 and 3 will be removed, so the output will only contain unique values.

print(my_set)  # Output: {1, 2, 3, 4, 5} (duplicate values are removed)

my_set = {1, "Hello", 3.14, True}  # A set containing different data types: an integer, a string, a float, and a boolean
print(my_set)  # Output: {1, 'Hello', 3.14, True}
print(type(my_set))  # Output: <class 'set'>   

#also cant access items using index as set is unordered collection of items.
#  So we cannot access items in a set using index 
# like my_set[0] or my_set[1].
#  Instead, we can iterate through the set using a loop to access each item.
#  Here's an example:
for item in my_set:
    print(item)  # This will print each item in the set on a new line


    # store it as a list in python
my_array = list(my_set)  # Converting the set to a list so it prints as a list structure
print(my_array)  # Output: [1, 'Hello', 3.14, True]



