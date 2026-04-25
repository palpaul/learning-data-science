# Initial dictionary
# keys - int, float, string, tuple (immutable) allowed
# keys - list, dict, set (mutable) not allowed
# values - any data type allowed
# dictionaries are unordered, mutable, and indexed collections of key-value pairs.
# Dictionaries are defined using curly braces {} and consist of key-value pairs separated by colons (:). Each key is unique within a dictionary, and it is used to access the corresponding value. Values can be of any data type, including other dictionaries, lists, or even functions. Dictionaries are commonly used for storing and retrieving data in a structured way, making them a fundamental data structure in Python programming.  
# Example of a dictionary
student = {
    "name": "Amit",
    "age": 22,
    "course": "Data Science",
    "marks": 85
}

print("Original dictionary:")
print(student)
print()

# 1. Access elements
print("Access elements:")
print("Name:", student["name"])
print("Age:", student["age"])
print()

# 2. Add / Update elements
student["city"] = "Delhi"      # adding new key
student["marks"] = 90          # updating existing key

print("After adding/updating:")
print(student)
print()

# 3. Delete element using del
del student["course"]

print("After deleting 'course':")
print(student)
print()

# 4. pop() - remove specific key
removed_value = student.pop("age")

print("After pop('age'):")
print("Removed value:", removed_value)
print(student)
print()

# 5. popitem() - removes last inserted item
last_item = student.popitem()

print("After popitem():")
print("Removed item:", last_item)
print(student)
print()

print("Iterating through dictionary:")
for k in student:
    print(k, ":", student[k])
for v in student.values():
    print(v)
for k, v in student.items():
    print(k, ":", v)        


# 6. clear() - remove all items
student.clear()

print("After clear():")
print(student)



#example - 2 
import copy

# Original dictionary
student = {
    "name": "Amit",
    "age": 22,
    "marks": [80, 85, 90]
}

# ---------------------------
# 1. Reference Copy
# ---------------------------
ref_copy = student   # same memory (no new object)

ref_copy["name"] = "Ravi"        # changes original too
ref_copy["marks"][0] = 100       # changes inside list also affects original

print("After Reference Copy:")
print("Original:", student)
print("Reference Copy:", ref_copy)
print()

# Reset original for clear understanding
student = {
    "name": "Amit",
    "age": 22,
    "marks": [80, 85, 90]
}

# ---------------------------
# 2. Shallow Copy - what it is and how it works
# ---------------------------  
#Simple why:

#🔴 Reference copy (=) → both variables point to the same memory, so anything you change affects both.
#🟡 Shallow copy (.copy()) → creates a new outer object, but inner objects (like lists inside dict) are still shared to save memory, so changes inside them affect both.
    #💡 In short:
#Reference = same thing
#Shallow = new box, but same items inside some parts
# ---------------------------
shallow_copy = student.copy()    # new outer dict, but inner objects shared

shallow_copy["name"] = "Neha"    # only affects copy
shallow_copy["marks"][1] = 999   # affects both (shared list)

print("After Shallow Copy:")
print("Original:", student)
print("Shallow Copy:", shallow_copy)


print("Dictionary with different valid immutable keys")
my_dict = {
    1: "hello",         
    3.14: "welcome",
    3.14:"bye", 
    "str1":"python",
     (1,2):"Dict",  # tuple key (immutable)
    True:"Hi",
    None:"None value",
    (10,20):"Hello" #"Tuple key2"
           
}

print(my_dict)  # print full dictionary

# Accessing values using keys
print(my_dict[1])       
print(my_dict[3.14])    
print(my_dict[(1, 2)])   



print("character frequency counting in a string")

str = "apple"

# Method 1: if-else approach (manual checking)
freq1 = {}
for ch in str:
    if ch in freq1:
        freq1[ch] += 1   # increase if already exists
    else:
        freq1[ch] = 1     # first time seen

print("if-else method:", freq1)

# Method 2: get() approach (shortcut)
freq2 = {}
for ch in str:
    freq2[ch] = freq2.get(ch, 0) + 1   # auto 0 if missing, then +1

print("get() method:", freq2)