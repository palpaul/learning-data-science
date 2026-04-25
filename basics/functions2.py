# #example 
# def db_donn(username, password,dbname):
#     """This function takes username, password and dbname as input and returns a connection string."""
#     if dbname == "mysql":
#         if username == "root" and password == "password":
#             return "Connection to MySQL database successful!"
#         elif dbname == "postgresql":
#             if username == "admin" and password == "admin123":
#                 return "Connection to PostgreSQL database successful!"
#             else:
#                 return "Invalid username or password for PostgreSQL database."
#     else:
#         return "Unsupported database type."
    
# # Example usage:
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# dbname = input("Enter the database name (mysql/postgresql): ")
# connection_result = db_donn(username, password, dbname)
# print(connection_result)



def  fun_one(num1=2, num2=3):
    """This function takes two numbers as input and returns their sum. If no numbers are provided, it uses default values."""
    result = num1 + num2
    print(result)

fun_one()  # Output: 5
fun_one(5, 10)  # Output: 15

#fun_one(None,100)  # Output: TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

#example
def func_two(*parameters):
#     """This function takes a variable number of parameters and prints them."""
    for param in parameters:
        print(param)
func_two(1, 2, 3)  # Output: 1 2 3
func_two("Hello", "World")  # Output: Hello World   
    

#example variable number of parameters with return type
def sum_all(*numbers):
    """This function takes a variable number of numbers as input and returns their sum."""
    total = 0
    for num in numbers:
        total += num
    return total    
result = sum_all(1, 2, 3, 4, 5)
print(result)  # Output: 15

#example variable number of parameters without loop with return type
def fun__nums(*nums): # we can pass any number of arguments to this function
    """This function takes a variable number of numbers as input and returns their sum."""
    return sum(nums)
fun__nums(1, 2, 3, 4, 5)  # Output: 15
fun__nums() # Output: 0
fun__nums(10, 20)  # Output: 30



