#explain functions in python
#In Python, a function is a reusable block of code that performs a specific task. Functions allow you to break down your code into smaller, more manageable pieces, making it easier to read and maintain. You can define a function using the `def` keyword, followed by the function name and parentheses. Inside the parentheses, you can specify parameters that the function can accept as input. The body of the function is indented below the definition line.

#function - business logic block of statement
#reuse the business logic
# def is the keyword , used to declare the function
# function name - should be meaningful and follow the naming conventions (lowercase letters and underscores)    
# parameters - variables that are defined in the function definition and can be used within the function to perform operations. They act as placeholders for the values that will be passed to the function when it is called.  
# docstring - a string literal that appears as the first statement in a function definition. It is used to document the purpose and behavior of the function. Docstrings are enclosed in triple quotes (""" """) and can span multiple lines. They provide a convenient way to describe what the function does, its parameters, and its return value. This documentation can be accessed using the `help()` function or by using the `.__doc__` attribute of the function.

#Here's a simple example of a function that takes two numbers as input and returns  their sum:
def add_numbers(a, b):
    """This function takes two numbers and returns their sum."""
    return a + b
# You can call the function and pass arguments to it like this:
result = add_numbers(5, 3)
print(result)  # Output: 8



def multiply_numbers(a, b):
    """This function takes two numbers and returns their multiplication."""
    return a * b
result = multiply_numbers(5, 3)
print(result)  # Output: 15

# In this example, we defined a function called `add_numbers` that takes two parameters `a` and `b`, and returns their sum. We also defined another function called `multiply_numbers` that takes the same parameters and returns their product. We then called both functions with the arguments `5` and `3`, and printed the results.

# example - 
def func_one():
    """This function prints a message."""
    
    pass # The pass statement is a placeholder that does nothing. It is used when you want to define a function but haven't implemented it yet. You can replace the pass statement with the actual code to perform the desired task.
func_one()  # Output: Hello, this is func_one!



def func_two():
    """This function prints a message."""
    print("Hello, this is func_two!")
func_two()  # Output: Hello, this is func_two!

#what is indentation in python
# In Python, indentation refers to the whitespace at the beginning of a line of code. It
#is used to define the scope of loops, functions, and other code blocks. Proper indentation is crucial in Python, as it indicates which statements belong to which blocks of code. For example, in a function definition, the body of the function must be indented to indicate that it is part of the function. If the indentation is not consistent, it can lead to syntax errors or unexpected behavior in your code.
# Here's an example of a function with proper indentation:
def greet(name):
    """This function takes a name as input and prints a greeting message."""
    print(f"Hello, {name}!")
greet("Alice")  # Output: Hello, Alice!
# In this example, the body of the `greet` function is indented, indicating that it belongs to the function. If we were to remove the indentation, we would get a syntax error.

def addTwoNumbers():
    nm1= 2
    nm2= 3
    return nm1 + nm2
result = addTwoNumbers()
print(result)  # Output: 5

#take the user input and add two numbers
def addition():
    """This function takes two numbers as input and returns their sum."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    return result
sum_result = addition()
print(f"The sum of the two numbers is: {sum_result}")


# function with no parameters - no return type
def greet():
    """This function prints a greeting message."""
    print("Hello, welcome to Python functions!")
greet()  # Output: Hello, welcome to Python functions!

#funnction with no parameters - with return type
def get_greeting():
    """This function returns a greeting message."""
    return "Hello, welcome to Python functions!"
greeting_message = get_greeting()
print(greeting_message)  # Output: Hello, welcome to Python functions!


#function with parameters - no return type
def greet_person(name):
    """This function takes a name as input and prints a greeting message."""
    print(f"Hello, {name}! Welcome to Python functions!")
greet_person("Alice")  # Output: Hello, Alice! Welcome to Python functions!

#function with parameters - with return type
def get_greeting_for_person(name):
    """This function takes a name as input and returns a greeting message."""
    return f"Hello, {name}! Welcome to Python functions!"   
greeting_message = get_greeting_for_person("Alice")
print(greeting_message)  # Output: Hello, Alice! Welcome to Python functions!




