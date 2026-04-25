# oops - Object Oriented Programming System
# OOP is a programming paradigm that uses objects and classes to organize code and data. It allows for the creation of reusable and modular code, making it easier to manage and maintain larger codebases. In OOP, you can define classes that represent real-world entities or concepts, and then create objects (instances) of those classes to work with.
# Key concepts in OOP include:
# 1. Classes: A class is a blueprint for creating objects. It defines the properties
#    (attributes) and behaviors (methods) that the objects created from the class will have.
# class is a collection of objects ,variables and functions that share common properties and behaviors. It serves as a blueprint for creating individual objects (instances) that have the same attributes and methods defined in the class. A class can be thought of as a template or a mold that defines the structure and behavior of the objects created from it. For example, you can define a class called "Car" that has attributes like "make," "model," and "year," and methods like "start_engine" and "stop_engine." Then, you can create multiple instances of the "Car" class, each representing a specific car with its own unique values for the attributes.
# 2. Objects: An object is an instance of a class. It is a specific
#    realization of the class with its own unique data and behavior.
# 3. Inheritance: Inheritance allows a new class (called a subclass or child class) to inherit properties and behaviors from an existing class (called a superclass or parent class). This promotes code reuse and allows for the creation of more specialized classes.
# 4. Encapsulation: Encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on that data into a single unit (class). It also involves restricting access to certain components of an object, which can help prevent unintended interference and misuse of the data.
# 5. Polymorphism: Polymorphism allows objects of different classes to be treated
#    as instances of the same class through a common interface. It enables the use of a single function or method to work with different types of objects, allowing for flexibility and extensibility in code design.


class Test:
    def wish(self): # self (in java self like this method )is a reference to the current instance of the class, and it is used to access the attributes and methods of the class. It is a convention to name this parameter "self", but you can choose any name you like. The self parameter is automatically passed to the method when it is called on an instance of the class.   
        print("Hello, World!")

# Creating an object of the Test class
t = Test()
t.wish()  # Output: Hello, World!   


# exaample -2 
class test2:

    # no - para no return type
    def add1(self):
        a = 10
        b = 20
        c = a + b
        print("The sum is:", c)


        # non para - with return type
    def add2(self):
        a = 10
        b = 20
        c = a + b
        return c
    # para - with no return type
    def add3(self, a, b):
        c = a + b
        print("The sum is:", c)
        # para - with return type
    def add4(self, a, b):
        c = a + b
        return c
    

    
# Creating an object of the test2 class
t2 = test2()
t2.add1()  # Output: The sum is: 30
result = t2.add2()
print("The sum is:", result)  # Output: The sum is: 30
t2.add3(15, 25)  # Output: The sum is: 40
result = t2.add4(15, 25)
print("The sum is:", result)  # Output: The sum is: 40


# example - 3 instance variable and class variable
    # instance variable is a variable that is defined within a class and is associated with an instance of that class. Each instance of the class can have its own unique value for the instance variable. It is typically defined within the __init__ method of the class and is accessed using the self keyword. For example, in the Person class, name and age are instance variables that can have different values for each instance of the Person class.
    # class variable is a variable that is defined within a class and is shared among all instances
    # of that class. It is typically defined outside of any method in the class and is accessed using the class name or the
    #self keyword. For example, in the Person class, if we define a class variable called species, it would be shared among all instances of the Person class and would have the same value for each instance.


   # instance variable 
   # __init__() method  called as constructor it is used to initialize the instance variables of a class. It is called when an object of the class is created and allows you to set the initial values for the instance variables. The self parameter refers to the instance of the class being created, and it allows you to assign values to the instance variables for that specific instance. 
   # it will execute  only once automatically when we create an object of the class and we can pass values to it to initialize the instance variables. For example, in the Person class, we can use the __init__ method to initialize the name and age instance variables for each person object that we create.
   # when ever we create an object of the class the __init__ method will be called automatically and it will initialize the instance variables with the values provided as arguments. This allows us to create multiple instances of the class with different values for the instance variables, while still using the same class definition.

class Test3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# creating an object of the Test3 class
t3 = Test3("John", 25)
print(t3.name)  # Output: John
print(t3.age)   # Output: 25


# example of class variable
class Test4:
    class_variable = "I am a class variable"  # This is a class variable

    def __init__(self, name):
        self.name = name  # This is an instance variable    inside the  constructor we can define instance variable and outside the constructor we can define class variable
                           # you can also define instance variable inside any other method of the class but it is not recommended as it can lead to confusion and make the code harder to understand. It is best practice to define instance variables within the __init__ method, as this clearly indicates that they are associated with each instance of the class and allows for better organization and readability of the code. 

# creating an object of the Test4 class
t4 = Test4("Alice") # here creating an object of the Test4 class as i nedd to access instance variable  for accessing class variable we can access it directly by using class name or by using object reference
# for accessing class variable we can access it directly by using class name or by using object reference
print(Test4.class_variable)  # Output: I am a class variable




#example of class variable  one more way to access class variable is by using object reference
print(t4.class_variable)  # Output: I am a class variable

#example of class variable  one more way to access class variable is by using object reference
t4.class_variable = "I am a modified class variable"  # Modifying the class variable using object reference
print(Test4.class_variable)  # Output: I am a modified class variable


#example of class variable  one more way by using @classmethod decorator
class Test5:
    company = "TCS"  # This is a class variable
    def __init__(self, name):
        self.name = name  # This is an instance variable


    @classmethod
    def change_company(cls, newcompany):
        cls.company = newcompany  # Modifying the class variable using class method

Test5.change_company("Oracle")  # Modifying the class variable using class method
t1 = Test5("Google") # this is related to instance variable but we can access class variable by using object reference
t2= Test5("Microsoft") # this is related to instance variable but we can access class variable by using object reference
print(Test5.company)  # Output: Oracle  
print(t1.company)  # Output: Oracle as this is related to class variable and it is shared among all instances of the class so when we change the value of class variable it will change for all instances of the class
print(t2.company)  # Output: Oracle as this is related to class variable and it is shared among all instances of the class so when we change the value of class variable it will change for all instances of the class



# other example of class and object

class Person:
    def __init__(self, name, age): # __init__ is a special method in Python classes that is called when an object is created. It is used to initialize the attributes of the class with the values provided as arguments. The self parameter refers to the instance of the class being created, and it allows you to set the attributes for that specific instance.
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
# Creating an object of the Person class
person1 = Person("Alice", 30)
person1.display_info()  # Output: Name: Alice, Age: 30



#encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on that data into a single unit (class). It also involves restricting access to certain components of an object, which can help prevent unintended interference and misuse of the data. Encapsulation allows for better organization and modularity in code design, as it keeps related data and behavior together within a class. It also helps to protect the integrity of the data by controlling access to it through methods defined within the class, rather than allowing direct access from outside the class. This promotes better code maintainability and reduces the chances of accidental modifications to the data.
# encapsulation example
# __ is used to declare the private variable in python and it is used to restrict the access of the variable from outside the class. It is a convention to use double underscores before the variable name to indicate that it is a private variable. Private variables can only be accessed within the class and cannot be accessed directly from outside the class. To access or modify the value of a private variable, you can use getter and setter methods within the class. This helps to protect the data and maintain the integrity of the class by preventing unauthorized access or modification of the private variables.
# private variable is a variable that is declared within a class and is not accessible from outside the class. It is typically defined with a double underscore prefix (__) to indicate that it is private. Private variables are used to encapsulate data and restrict access to it, ensuring that it can only be accessed or modified through methods defined within the class. This helps
# private variable , unable to access with class object but we can access it with in the class by using method of the class and we can also access it by using name mangling technique but it is not recommended as it can lead to confusion and make the code harder to understand. It is best practice to access private variables through methods defined within the class, as this clearly indicates that they are intended to be private and allows for better organization and readability of the code.
# private variables are used to encapsulate data and restrict access to it, ensuring that it can only be accessed or modified through methods defined within the class. This helps

class Test6:
    def __init__(self):
        self.__amount = 1000  # Private variable (declare with __)
    def display_amount(self):
        return self.__amount

testobj6 = Test6()
# testobj6.__amount  # This will raise an AttributeError because __amount is a private variable and cannot be accessed directly from outside the class
# so we can access with the help of method of the class best practice to access private variables through methods defined within the class, as this clearly indicates that they are intended to be private and allows for better organization and readability of the code.    )
print(testobj6.display_amount())  # Output: 1000
# we can also access it by using name mangling technique but it is not recommended as it can lead to confusion and make the code harder to understand. It is best practice to access private variables through methods defined within the class, as this clearly indicates that they are intended to be private and allows for better organization and readability of the code.    )
print(testobj6._Test6__amount)  # Output: 1000 (accessing private variable using name mangling technique, but it is not recommended as it can lead to confusion and make the code harder to understand. It is best practice to access private variables through methods defined within the class, as this clearly indicates that they are intended to be private and allows for better organization and readability of the code.    )




class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        return self.__balance
# Creating an object of the BankAccount class
account = BankAccount("123456789", 1000)
account.deposit(500)  # Output: Deposited: 500, New Balance: 1500
account.withdraw(200)  # Output: Withdrew: 200, New Balance: 1300
print(f"Current Balance: {account.get_balance()}")  # Output: Current Balance: 1300


#inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a subclass or child class) to inherit properties and behaviors from an existing class (called a superclass or parent class). This promotes code reuse and allows for the creation of more specialized classes. The subclass can override or extend the functionality of the superclass, allowing for greater flexibility and modularity in code design. Inheritance helps to establish a natural hierarchical relationship between classes, making it easier to organize and manage code.
#inheritance allows a new class (called a subclass or child class) to inherit properties and behaviors from an existing class (called a superclass or parent class). This promotes code reuse and allows for the creation of more specialized classes. The subclass can override or extend the functionality of the superclass, allowing for greater flexibility and modularity in code design. Inheritance helps to establish a natural hierarchical relationship between classes, making it easier to organize and manage code.

# inheritance example
class parent:
    def ptest(self):
        print("This is parent class method.")
class child(parent):
    def ctest(self):
        print("This is child class method.")

# Creating an object of the child class
c = child()
c.ptest()  # Output: This is parent class method. (inherited from parent class)
c.ctest()  # Output: This is child class method. (defined in child class)


#example 02

class Animal:
    def eat(self):
        print("This animal eats food.") 
class Dog(Animal):  # Dog class inherits from Animal class
    def bark(self):
        print("The dog barks.")
# Creating an object of the Dog class
dog = Dog()
dog.eat()  # Output: This animal eats food. (inherited from Animal class)
dog.bark()  # Output: The dog barks. (defined in Dog class)


# example 03
#multilevel inheritance is a type of inheritance in which a class can inherit from another class, which in turn can inherit from another class. This creates a chain of inheritance where each class can access the properties and methods of its parent class as well as its own properties and methods. Multilevel inheritance allows for greater code reuse and promotes a hierarchical relationship between classes, making it easier to organize and manage code.
class parent1:
    def ptest1(self):
        print("This is parent1 class method.")

class chiled1(parent1):
    def ctest1(self):
        print("This is child1 class method.")

class Subchild(chiled1):
    def subchildtest(self):
        print("This is subchild class method.")

# Creating an object of the Subchild class
subchild = Subchild()
subchild.ptest1()  # Output: This is parent1 class method. (inherited from parent1 class)
subchild.ctest1()  # Output: This is child1 class method. (inherited from chiled1 class)
subchild.subchildtest()  # Output: This is subchild class method. (defined in Subchild class)


#example of multiple inheritance is a type of inheritance in which a class can inherit
#from more than one parent class. This allows the child class to access properties and methods from multiple parent classes, promoting code reuse and flexibility in design. However, it can also lead to ambiguity if there are conflicting attributes or methods in the parent classes, so it is important to use multiple inheritance carefully and consider the potential for conflicts when designing your class hierarchy. 

class parent2:
    def ptest2(self):
        print("This is parent2 class method.")
class parent3:
    def ptest3(self):
        print("This is parent3 class method.")
class childd(parent2, parent3):
    def ctest(self):
        print("This is child class method.")

# Creating an object of the childd class
childobj = childd()
childobj.ptest2()  # Output: This is parent2 class method. (inherited from parent2 class)
childobj.ptest3()  # Output: This is parent3 class method. (inherited from parent3 class)
childobj.ctest()   # Output: This is child class method. (defined in childd class)



#polimorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as instances of the same class through a common interface. It enables the use of a single function or method to work with different types of objects, allowing for flexibility and extensibility in code design. Polymorphism can be achieved through method overriding, where a subclass provides a specific implementation of a method that is already defined in its superclass, or through
#method overloading, where multiple methods with the same name but different parameters are defined within a class. Polymorphism promotes code reuse and allows for more dynamic and adaptable code, as it enables objects of different classes to be used interchangeably while still maintaining their unique behaviors.   
#polimorphism behave like many
# method overloading -does not supper in python
# method overriding

#method overriding is a feature in object-oriented programming (OOP) that allows a subclass to provide a specific implementation of a method that is already defined in its superclass. When a method in a subclass has the same name and signature as a method in its superclass, the method in the subclass overrides the method in the superclass. This allows the subclass to provide its own behavior for that method while still maintaining the same interface. Method overriding promotes code reuse and allows for more dynamic and adaptable code, as it enables subclasses to customize or extend the behavior of methods defined in their superclasses without changing the original implementation.
class Parent:
    def db_connect(self):
        print("Connecting to the database in the parent class.")

class Child(Parent):
    def db_connect(self):
        print("Connecting to the database in the child class.")

# Creating an object of the Child class
childobj = Child() # creating an object of the Child class , its overriding the db_connect method of the Parent class
childobj.db_connect()

# parentobj = Parent() # creating an object of the Parent class
# parentobj.db_connect()


# method overloading does not exist in Python in the traditional sense as it does in some other programming languages like Java or C++. In Python, you cannot define multiple methods with the same name but different parameters within a class. However, you can achieve similar functionality by using default arguments or variable-length arguments in a single method definition. This allows you to create a method that can handle different numbers of arguments or different types of arguments, effectively simulating method overloading.   

# Simulating method overloading using default arguments

class addition:
    def add(self, a, b=0, c=0):
        return a + b + c

# Creating an object of the addition class
addobj = addition()
result1 = addobj.add(10, 20)  # This will call the add method with two parameters and return 30
result2 = addobj.add(10, 20, 30)  # This will call the add method with three parameters and return 60
print(result1)  # Output: 30
print(result2)  # Output: 60




class Test7:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c): # this add method is overriden here so if we call add method with two parameters it will raise a TypeError because the add method with two parameters has been overridden by the add method with three parameters
        return a + b + c
# Creating an object of the Test7 class
test7 = Test7()
# The following line will raise a TypeError because the add method with two parameters has been overridden by the add method with three parameters
# result = test7.add(10, 20)  # This will raise a TypeError because the add method with two parameters has been overridden by the add method with three parameters
result = test7.add(10, 20, 30)  # This will call the add method with three parameters and return 60
print(result)  # Output: 60

# this is demonstrating that method overloading does not exist in Python in the traditional sense as it does in some other programming languages like Java or C++.
#  In Python, you cannot define multiple methods with the same name but different parameters within a class.
#  However, you can achieve similar functionality by using default arguments or variable-length arguments in a single method definition. This allows you to create a method that can handle different numbers of arguments or different types of arguments, effectively simulating method overloading.
class Test8:
    def addi(self , *args):
        print(sum(args))
# Creating an object of the Test8 class
test8obj = Test8()
test8obj.addi(10)  # This will call the addi method with one parameter and return 10
test8obj.addi(10, 20)  # This will call the addi method with two parameters and return 30
test8obj.addi(10, 20, 30)  # This will call the addi method with three parameters and return 60 

print(result)  # Output: 30 


# example -  thia is also a methoed overloading but it is not recommended as it can lead to confusion and make the code harder to understand.
#  for  best practice to use default arguments or variable-length arguments in a single method definition to achieve similar functionality, as this allows for better organization and readability of the code.
class ttest:
    def add(self, num1=None,num2=None,num3=None):
            if num1 and num2 and num3:
                print(num1 + num2 + num3)
            elif num1  and num2 :
                print(num1 + num2)
            elif num1:
                print(num1)
            else: 
                print("No numbers to add")

obj = ttest()
obj.add(10)  # Output: 10
obj.add(10, 20)  # Output: 30
obj.add(10, 20, 30)  # Output: 60
obj.add()  # Output: No numbers to add



# example 
# predefinned functions in pythons always start and end with double underscores (__) are called dunder methods or magic methods. These methods are special methods that have a specific meaning and behavior in Python. They are used to define the behavior of objects when certain operations are performed on them, such as addition, subtraction, string representation, etc. For example, the __add__ method is used to define the behavior of the + operator for a class, allowing you to specify how two objects of that class should be added together. By implementing these dunder methods in your classes, you can customize the behavior of your objects and make them work seamlessly with built-in Python operations. 
class test9:
    def __init__(self, num1): # constructor to initialize the name attribute of the test9 class. The __init__ method is a special method in Python classes that is called when an object of the class is created. It is used to initialize the attributes of the class with the values provided as arguments. The self parameter refers to the instance of the class being created, and it allows you to set the attributes for that specific instance. In this example, the __init__ method takes a name parameter and assigns it to the name attribute of the class, allowing each instance of test9 to have its own unique name.
        self.num1 = num1
    
    def __add__(self, num2): # predefined method in python for operator overloading it is used to overload the + operator for the class test9. When we use the + operator with two objects of the test9 class, it will call the __add__ method and pass the other object as an argument. In this example, the __add__ method concatenates the name attributes of both objects and returns the result.
        return (self.num1 + num2.num1) # this will concatenate the name attributes of both objects and return the result

obj1 = test9(10)
obj2 = test9(20)
result = obj1 + obj2  # This will call the __add__ method and concatenate the numbers of obj1 and obj2
print(result)  # Output: 30


# example of __str__ method is a predefined method in Python that is used to define the string representation of an object. When you print an object or convert it to a string, the __str__ method is called to determine how the object should be represented as a string. By implementing the __str__ method in your class, you can customize the way your objects are displayed when printed or converted to strings, making it easier to understand and debug your code. In this example, the __str__ method returns a custom string representation of the object, which will be displayed when we print the object of class A.
# dunder methods or magic methods are special methods in Python that have a specific meaning and behavior. They are always defined with double underscores (__) at the beginning and end of their names. These methods allow you to define how your objects should behave in certain situations, such as when they are printed, compared, or used in arithmetic operations. For example, the __str__ method is a dunder method that defines the string representation of an object, which is what gets displayed when you print the object. By implementing dunder methods in your classes, you can customize the behavior of your objects and make them work seamlessly with built-in Python operations.

class A:
  #  pass # The pass statement is a placeholder that does nothing. It is used when you want to define a class or a function but don't want to implement any functionality yet. In this example, the class A is defined with the pass statement, which means it doesn't have any attributes or methods. You can create an object of this class, but it won't have any specific behavior or properties until you add them later.   
    def __str__(self):
        return "This is a custom string representation of the object."
objA = A()
print(objA)  # Output: This is a custom string representation of the object.





# abstraction 
# 
from abc import ABC, abstractmethod # whehere what is abc and abstractmethod in python
# ABC stands for Abstract Base Class, and it is a module in Python's standard library that provides a way to define abstract base classes. An abstract base class is a class that cannot be instantiated and is meant to be subclassed by other classes. It serves as a blueprint for other classes, defining a common interface and behavior that the subclasses must implement.
# The abstractmethod decorator is used to indicate that a method in an abstract base class is an    
class  Business(ABC):
    @abstractmethod
    def start_business(self):
        pass
class  firend_Business(Business):
    def start_business(self):
        print("Friend's business has started.")
# Creating an object of the firend_Business class
friend_business = firend_Business()
friend_business.start_business()  # Output: Friend's business has started.



#example - - chiled class constructor is calling parent class constructor
class Parent(ABC):
    def __init__(self , param1):
        self.param1 = param1

class Child(Parent):
    def __init__(self, param1, param2):
        super().__init__(param1)  # Call the constructor of the Parent class to initialize param1
        self.param2 = param2  # Initialize param2 in the Child class

# Creating an object of the Child class
child_obj = Child(200, 100)
print(child_obj.param1)  # Output: 200
print(child_obj.param2)  # Output: 100


# static method is a method that belongs to a class rather than an instance of the class. It is defined using the @staticmethod decorator and does not require access to any instance-specific data or methods. Static methods can be called on the class itself without needing to create an instance of the class. They are typically used for utility functions that perform a specific task and do not rely on the state of the object. For example, you can define a static method to calculate the area of a circle given its radius, and this method can be called directly on the class without needing to create an object of the class.   
# static method won't use self parameter because it does not require access to any instance-specific data or methods. Static methods are defined using the @staticmethod decorator and can be called on the class itself without needing to create an instance of the class. They are typically used for utility functions that perform a specific task and do not rely on the state of the object. For example, you can define a static method to calculate the area of a circle given its radius, and this method can be called directly on the class without needing to create an object of the class.   
# static method won't use class method won't use cls parameter because it does not require access to any class-specific data or methods. Class methods are defined using the @classmethod decorator and can be called on the class itself without needing to create an instance of the class. They are typically used for factory methods that create instances of the class or for methods that operate on class-level data. For example, you can define a class method to create a new instance of a class with specific attributes, and this method can be called directly on the class without needing to create an object of the class.
# where to declare static method -- inside the class 
# with the help of @staticmethod decorator but outside the constructor and other methods of the class. Static methods are defined using the @staticmethod decorator and can be called on the class itself without needing to create an instance of the class. They are typically used for utility functions that perform a specific task and do not rely on the state of the object. For example, you can define a static method to calculate the area of a circle given its radius, and this method can be called directly on the class without needing to create an object of the class.    
# we will call with the help of class name directly without creating an object of the class because static methods belong to the class rather than an instance of the class. Static methods are defined using the @staticmethod decorator and can be called on the class itself without needing to create an instance of the class. They are typically used for utility functions that perform a specific task and do not rely on the state of the object. For example, you can define a static method to calculate the area of a circle given its radius, and this method can be called directly on the class without needing to create an object of the class.    

# utility methods (geenral purpose methods ) are methods that perform a specific task and do not rely on the state of the object. They are typically defined as static methods using the @staticmethod decorator and can be called directly on the class without needing to create an instance of the class. Utility methods are often used for common operations or calculations that are related to the class but do not require access to instance-specific data or methods. For example, you can define a utility method to calculate the area of a circle given its radius, and this method can be called directly on the class without needing to create an object of the class.         


# example of static method and utility method

class Test10:

    @staticmethod
    def greet():
        print("Hello, welcome to static methods!")

# Calling the static method directly on the class without creating an instance
Test10.greet()  # Output: Hello, welcome to static methods!


# example
class MathUtils:
    @staticmethod
    def calculate_area_of_circle(radius):
        import math
        return math.pi * radius ** 2

# Calling the utility method directly on the class without creating an instance
area = MathUtils.calculate_area_of_circle(5)  # Output: 78.53981633974483
print(area)


class MathUtils:
    @staticmethod
    def square(num1):
        return num1 ** 2

# Calling the utility method directly on the class without creating an instance
result = MathUtils.square(5)  # Output: 25
print(result)   



# example
class abc :
    #class level variable
    company = "TCS"
    #constructor
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable
        
        # instance method
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Company: {abc.company}")
        #class method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company  # Modifying the class variable using class method
        # static method
    @staticmethod
    def isMajor(age):
        return age >= 18
# Creating an object of the abc class
person1 = abc("Alice", 30)  # calling instance method using object of the abc class and passing the name and age as arguments to the constructor to initialize the instance variables
person1.display_info()  # Output: Name: Alice, Age: 30, Company: TCS , calling the instance method to display the information of the person1 object, which includes the name, age, and company (which is a class variable shared among all instances of the class)
abc.change_company("Oracle")  # Modifying the class variable using class method
person1.display_info()  # Output: Name: Alice, Age: 30, Company: Oracle
print(abc.isMajor(20))  # Output: True , calling the static method directly on the class without creating an instance   
print(abc.isMajor(15))  # Output: False , calling the static method directly on the class without creating an instance




