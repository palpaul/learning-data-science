# lambda functions in Python
# a function that can be defined without a name and can be used in a single line of code. It is often used for short, simple operations that can be defined in a single line of code. The syntax for a lambda function is as follows:
# lambda arguments: expression
#how to declare a lambda function
# Here's an example of a lambda function that takes two numbers as input and returns their sum:

# A lambda function is a small anonymous function that can take any number of arguments but can only have one expression. It is defined using the lambda keyword. Lambda functions are often used for short, simple operations that can be defined in a single line of code.
# lambda is a keyword in Python that is used to create lambda (anonymous) functions, which are functions that do not have a name. Lambda functions are often used for short, simple operations that can be defined in a single line of code. They are commonly used in situations where a function is required as an argument to another function, such as in the case of sorting or filtering data. Lambda functions can take any number of arguments but can only have one expression, which is evaluated and returned when the function is called.


add = lambda x, y: x + y
result = add(5, 10)
print(result)  # Output: 15
# Here's another example of a lambda function that takes a string as input and returns its length:
length = lambda s: len(s)
result = length("Hello, World!")
print(result)  # Output: 13

#example of lambda function  of square of a number
square = lambda num : num * num
result = square(5)
print(result)  # Output: 25 

#example of lambda function with if-else statement
check = lambda x: "Even" if x % 2 == 0 else "Odd"
result = check(10)
print(result)  # Output: Even
result = check(7)
print(result)  # Output: Odd


#example of lambda function with multiple arguments
max_num = lambda a, b, c: max(a, b, c)
result = max_num(5, 10, 3)
print(result)  # Output: 10

# map function
# map function is a built-in function in Python that takes a function and an iterable as input and applies the function to each item in the iterable, returning a new iterable (usually a map object) with the results. The syntax for the map function is as follows:
# map(function, iterable)
#map function used to manipulate each item in the iterable and return a new iterable with the results. It is often used in combination with lambda functions to perform simple operations on each item in the iterable. For example, you can use the map function to square each number in a list like this:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
# In this example, we used the map function to apply a lambda function that squares each number in the `numbers` list. The result is a new list called `squared_numbers` that contains the squared values of the original numbers.

# example of map function with multiple arguments
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
summed_numbers = list(map(lambda x, y: x + y, numbers1, numbers2))
print(summed_numbers)  # Output: [5, 7, 9]
# In this example, we used the map function to apply a lambda function that takes two arguments (x and y) and returns their sum. The map function applies this lambda function to each pair of items from the `numbers1` and `numbers2` lists, resulting in a new list called `summed_numbers` that contains the sums of the corresponding items from the original lists.   

# example of map function with if-else statement
numbers = [1, 2, 3, 4, 5]
even_odd = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", numbers))
print(even_odd)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']
# In this example, we used the map function to apply a lambda function that checks if each number in the `numbers` list is even or odd. The result is a new list called `even_odd` that contains the corresponding labels for each number.

#filter function
# filter is readymade function in Python that is used to filter items from an iterable based on a specified condition. It takes a function and an iterable as input and returns a new iterable (usually a filter object) containing only the items from the original iterable for which the function returns True. The syntax for the filter function is as follows:
# filter function is a built-in function in Python that takes a function and an iterable as input and returns a new iterable (usually a filter object) containing only the items from the original iterable for which the function returns True. The syntax for the filter function is as follows:
# filter(function, iterable)
# The filter function is used to filter items from an iterable based on a specified condition. It is often used in combination with lambda functions to perform simple filtering operations on each item in the iterable. For example, you can use the filter function to get only the even numbers from a list like this:
# example -
# filter is used  to apply  condition to filter out items from an iterable. For example, you can use the filter function to get only the even numbers from a list like this:

print("filter function example:")

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
# In this example, we used the filter function to apply a lambda function that checks if each number in the `numbers` list is even. The result is a new list called `even_numbers` that contains only the even numbers from the original list.




numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
# In this example, we used the filter function to apply a lambda function that checks if each number in the `numbers` list is even. The result is a new list called `even_numbers` that contains only the even numbers from the original list.

# example of filter function with multiple arguments
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
filtered_numbers = list(filter(lambda xy: xy[0] + xy[1] > 7, zip(numbers1, numbers2)))
print(filtered_numbers)  # Output: [(3, 6)]
# In this example, we used the filter function to apply a lambda function that takes a tuple of (x, y) pairs from zip() 
# and checks if their sum is greater than 7. The filter function applies this lambda function to each pair of items from the 
# `numbers1` and `numbers2` lists, resulting in a list of tuples where the sum is greater than 7.




# example
multiply = lambda num1: (lambda num2: num1 * num2)
result = multiply(5)(10)
print(result)  # Output: 50
# In this example, we defined a lambda function `multiply` that takes one argument `num1` and returns another lambda function that takes a second argument `num2` and multiplies it with `num1`. We then called the `multiply` function with the first argument (5) and immediately called the returned lambda function with the second argument (10), resulting in the multiplication of 5 and 10, which gives us 50.


# list-  [] , tuple- () , set- {} , dictionary- {}

# how to represent a list in Python
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
# In this example, we created a list called `my_list` that contains the numbers 1 through 5. We then printed the list, which outputs the entire list as shown.
# example of list with different data types
my_list = [1, "Hello", 3.14, True]  
print(my_list)  # Output: [1, 'Hello', 3.14, True]
# In this example, we created a list called `my_list` that contains different data types
#, including an integer (1), a string ("Hello"), a float (3.14), and a boolean (True). We then printed the list, which outputs the entire list with all the different data types as shown.

#sorted() - is a predefined function in Python that is used to sort the elements of an iterable (such as a list, tuple, or string) in a specific order. The sorted() function takes an iterable as input and returns a new sorted list. The syntax for the sorted() function is as follows:
# sorted(iterable, key=None, reverse=False)
stds = [("Alice", 25),
         ("Bob", 30),
        ("Charlie", 20)
        ]
sorted_stds = sorted(stds, key=lambda x: x[1]) # In this example, we used the sorted() function to sort the list of tuples `stds` based on the second element of each tuple (the age) using a lambda function as the key. The lambda function takes a tuple `x` as input and returns the second element `x[1]`, which is used as the sorting key. The result is a new list called `sorted_stds` that contains the tuples sorted by age in ascending order.
print(sorted_stds)  # Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]


sorted_stds = sorted(stds, key=lambda x: x[1], reverse=True) #  here reverse=True indicates descending order.
print(sorted_stds)  # Output: [('Bob', 30), ('Alice', 25), ('Charlie', 20)]

# max() is a built-in function in Python that is used to find the maximum value from a given set of values or an iterable. The syntax for the max() function is as follows:
# max(iterable, *[, key, default])  
# used to find the maximum( highest) value from a list of numbers. For example:
numbers = [1, 2, 3, 4, 5]
max_number = max(numbers)
print(max_number)  # Output: 5
# In this example, we used the max() function to find the maximum value from the `numbers` list. The result is stored in the variable `max_number`, which is then printed, giving us the output of 5, which is the largest number in the list.

# useing max() function with a lambda function as the key to find the maximum value based on a specific criterion. For example, if we have a list of tuples representing students and their ages, we can use the max() function to find the student with the maximum age like this:
students = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
oldest_student = max(students, key=lambda x: x[1])
print(oldest_student)  # Output: ('Bob', 30)
# In this example, we used the max() function to find the maximum value from the `students` list based on the second element of each tuple (the age) using a lambda function as the key. The lambda function takes a tuple `x` as input and returns the second element `x[1]`, which is used as the criterion for finding the maximum value. The result is stored in the variable `oldest_student`, which is then printed, giving us the output of ('Bob', 30), which is the student with the maximum age in the list.



# 
func =  lambda x: "High" if x > 80 else ("Medium" if x > 50 else "Low")
print(func(60))  # Output: Medium

 

# touple example
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
# In this example, we created a tuple called `my_tuple` that contains the numbers 1 through 5. We then printed the tuple, which outputs the entire tuple as shown.
# example of tuple with different data types
my_tuple = (1, "Hello", 3.14, True)
print(my_tuple)  # Output: (1, 'Hello', 3.14, True)
# In this example, we created a tuple called `my_tuple` that contains different data types, including an integer (1), a string ("Hello"), a float (3.14), and a boolean (True). We then printed the tuple, which outputs the entire tuple with all the different data types as shown.

# dieeferen between list and tuple
# 1. Mutability: Lists are mutable, meaning you can modify their contents (add, remove, or change elements), while tuples are immutable, meaning once they are created, their contents cannot be changed.
# 2. Syntax: Lists are defined using square brackets [] while tuples are defined using parentheses ().
# 3. Performance: Tuples are generally faster than lists because they are immutable and have a smaller memory footprint. Lists, being mutable, require more memory and processing time for operations that modify their contents.
# 4. Use Cases: Lists are typically used when you need a collection of items that may change over time, while tuples are used when you want to create a collection of items that should not be modified, such as coordinates, fixed data, or when you want to use them as keys in a dictionary. 


# similar expalme for both and so i can differentiate between them
# List example
my_list = [1, 2, 3]
print("List before modification:", my_list)  # Output: List before modification: [1, 2, 3]
my_list[0] = 10 
print("List after modification:", my_list)  # Output: List after modification: [10, 2, 3]
# Tuple example
my_tuple = (1, 2, 3)
print("Tuple before modification:", my_tuple)  # Output: Tuple before modification: (1, 2, 3)
try:
    my_tuple[0] = 10  # This will raise a TypeError because tuples are immutable
except TypeError as e:
    print("Error:", e)  # Output: Error: 'tuple' object does not support item assignment





# example of dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
# In this example, we created a dictionary called `my_dict` that contains key-value pairs
#   
# , where the keys are "name", "age", and "city", and the corresponding values are "Alice", 25, and "New York". We then printed the dictionary, which outputs the entire dictionary as shown.
# example of dictionary with different data types

my_dict = {"name": "Alice", "age": 25, "is_student": True, "hobbies": ["reading", "traveling"]}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'is_student': True, 'hobbies': ['reading', 'traveling']}
# In this example, we created a dictionary called `my_dict` that contains key-value pairs
# with different data types, including a string ("Alice"), an integer (25), a boolean (True), and a list (["reading", "traveling"]). We then printed the dictionary, which outputs the entire dictionary with all the different data types as shown.


# how to reporesent a dictionary in Python in **kwargs
print("Dictionary example with **kwargs: means keyword arguments")
def student (** data):
    print(data)

student(name="Alice", marks=85, grade="A")

# with **kwargs with  for loop example
#** will create  a dicttionary internally and we can access the key and value using for loop
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
my_function(name="Alice", age=25, city="New York")
# In this example, we defined a function called `my_function` that takes keyword arguments using `**kwargs`. The function iterates through the key-value pairs in `kwargs` and prints them in a formatted string. We then called the function with some keyword arguments (name, age, and city), which results in the output of each key and its corresponding value as shown.

