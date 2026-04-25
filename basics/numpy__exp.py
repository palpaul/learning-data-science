#numpy 
# reference - https://numpy.org/doc/stable/user/quickstart.html

#numpay is a poowerful python library
#numerical python
#used to perform numerical operations on large datasets
#vnumpy built on top of c language and fortran so it is very fast and efficient
#import numpy as np

# numpy is a powerful library for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.
# Here are some key features of NumPy:  
# 1. Array Creation: NumPy allows you to create arrays of various shapes and sizes, including 1D, 2D, and higher-dimensional arrays.
# 2. Mathematical Operations: NumPy provides a wide range of mathematical functions that can be applied to arrays, such as addition, subtraction, multiplication, division, and more complex operations like trigonometric functions and linear algebra.
# 3. Broadcasting: NumPy supports broadcasting, which allows you to perform operations on arrays of different shapes and sizes without the need for explicit loops.
# 4. Performance: NumPy is optimized for performance and can handle large datasets efficiently, making it a popular choice for scientific computing and data analysis.
# 5. Integration: NumPy integrates well with other libraries in the Python ecosystem, such as SciPy, Matplotlib, and Pandas, making it a fundamental tool for data science and machine learning.
# To use NumPy, you need to install it first using pip: 
# pip install numpy
# Once installed, you can import it in your Python code and start using its functionalities. Here's a simple example of how to create a NumPy array and perform some basic operations:


import numpy as np

# Create a 1D NumPy array
list = np.array([1, 2, 3, 4, 5]) 
print(list)  # Output: [1 2 3 4 5]
print(type(list))  # Output: <class 'numpy.ndarray'>
print(list.shape)  # Output: (5,) , the shape of the array is (5,) which means it has 5 elements in one dimension
print(list.dtype)  # Output: int64 (or int32 depending on your system)   
print(list.ndim)  # Output: 1, the number of dimensions of the array is 1


# Create a 2D NumPy array
list2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(list2)  # Output: [[1 2 3] [4 5 6] [7 8 9]]
print(type(list2))  # Output: <class 'numpy.ndarray'>
print(list2.shape)  # Output: (3, 3), the shape of the array is (3, 3) which means it has 3 rows and 3 columns
print(list2.dtype)  # Output: int64 (or int32 depending on your system)
print(list2.ndim)  # Output: 2, the number of dimensions of the array is 2

# what is np.zeros here ? 
# The `np.zeros` function in NumPy is used to create a new array of a specified shape and type, filled with zeros. The function takes a tuple as an argument that defines the shape of the array. 
# For example, `np.zeros((2, 3))` creates a 2D array with 2 rows and 3 columns, where all the elements are initialized to zero. This can be useful when you need to create an array to store results or when you want to initialize an array before filling it with specific values. 
print(np.zeros((2, 3)))  # Output: [[0. 0. 0.] [0. 0. 0.]], creates a 2D array of zeros with shape (2, 3) 
print(np.ones((2, 3)))   # Output: [[1. 1. 1.] [1. 1. 1.]], creates a 2D array of ones with shape (2, 3)
print(np.full((2, 3), 7))  # Output: [[7 7 7] [7 7 7]], creates a 2D array filled with the value 7 with shape (2, 3)
print(np.eye(3))  # Output: [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]], creates a 2D identity matrix of size 3x3    
print(np.arange(0, 10, 2))  # Output: [0 2 4 6 8], creates a 1D array with values from 0 to 9 with a step of 2  
print(np.linspace(0, 1, 5))  # Output: [0.  0.25 0.5  0.75 1.], creates a 1D array with 5 evenly spaced values between 0 and 1  


list1 = np.array([1, 2, 3, 4, 5])
print(list1[0])  # Output: 1, accessing the first element of the array
print(list1[1:4])  # here index 1 will include and index 4 will exclude Output: [2 3 4], accessing a slice of the array from index 1 to index 3 (4 is exclusive)
print(list1[-1])  #  - index start with -1 from the end Output: 5, accessing the last element of the array
print(list1[::2])  # Output: [1 3 5], accessing every second element of the array starting from the first element   
print(list1[::-1])  # Output: [5 4 3 2 1], accessing the array in reverse order
print(list1[1:])  # here index 1 to end Output: [2 3 4 5], accessing the array from index 1 to the end of the array
print(list1[:3])  # Output: [1 2 3], accessing the array from the beginning to index 2 (3 is exclusive) 

# in simple if index end  with : means till the end 
# in simple if index start with : means from the beginning  and end index excluded for example list1[:3] means from the beginning to index 2 (3 is exclusive) and list1[1:] means from index 1 to the end of the array
# istarting index means its included , and ending index means its excluded


# example of 2D array slicing
list2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(list2[0, 0])  # Output: 1, accessing the element in the first row and first column
print(list2[1, 2])  # Output: 6, accessing the element in the second row and third column
print(list2[0:2, 1:3])  # Output: [[2 3] [5 6]], accessing a slice of the array from the first two rows and the last two columns
print(list2[:, 0])  # Output: [1 4 7], accessing all the elements in the first column
print(list2[1, :])  # Output: [4 5 6], accessing all the elements in the second row
print(list2[::2, ::2])  # Output: [[1 3] [7 9]], accessing every second element in both dimensions starting from the first element



#example 
list3 = np.array([1, 2, 3,4,5])
print(list3 + 10)  # Output: [11 12 13 14 15], adding 10 to each element of the array
print(list3 * 2)  # Output: [ 2  4  6  8 10], multiplying each element of the array by 2
print(list3 - 1)  # Output: [0 1 2 3 4], subtracting 1 from each element of the array
print(list3 / 2)  # Output: [0.5 1. 1.5 2.  2.5], dividing each element of the array by 2
print(list3 ** 2)  # Output: [ 1  4  9 16 25], raising each element of the array to the power of 2
print(np.sqrt(list3))  # Output: [1.         1.41421356 1.73205081 2.         2.23606798], calculating the square root of each element in the array
print(np.sin(list3))  # Output: [ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427], calculating the sine of each element in the array
print(np.cos(list3))  # Output: [ 0.54030231 -0.41614684 -0.9899925  -0.65364362  0.28366219], calculating the cosine of each element in the array
print(np.exp(list3))  # Output: [  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ], calculating the exponential of each element in the array    
print(np.log(list3))  # Output: [0.         0.69314718 1.09861229 1.38629436 1.60943791], calculating the natural logarithm of each element in the array
print(np.min(list3))  # Output: 1, finding the minimum value in the array
print(np.max(list3))  # Output: 5, finding the maximum value in the array
print(np.mean(list3))  # Output: 3.0, calculating the mean (average) of the elements in the array
print(np.median(list3))  # Output: 3.0, calculating the median  of the elements in the array
print(np.std(list3))  # Output: 1.4142135623730951, calculating the standard deviation of the elements in the array 
print(np.sum(list3))  # Output: 15, calculating the sum of all the elements in the array


#example
list4 = np.array([1, 2, 3])
list5 = np.array([[10], [20], [30]])
print(list4 + list5)  # Output: [[11 12 13] [21 22 23] [31 32 33]], adding two arrays element-wise using broadcasting
print(list4 * list5)  # Output: [[10 20 30] [20 40 60] [30 60 90]], multiplying two arrays element-wise using broadcasting  
                 


#example of array manipulation
list6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(list6.T)  # Output: [[1 4 7] [2 5 8] [3 6 9]], transposing the array (swapping rows and columns)
print(list6.flatten())  # Output: [1 2 3 4 5 6 7 8 9], flattening the array into a 1D array
print(list6.reshape(9, 1))  # Output: [[1] [2   ] [3] [4] [5] [6] [7] [8] [9]], reshaping the array into a 9x1 array
print(list6.reshape(1, 9))  # Output: [[1 2 3 4 5 6 7 8 9]], reshaping the array into a 1x9 array
print(list6.reshape(3, 3))  # Output: [[1 2 3] [4 5 6] [7 8 9]], reshaping the array back to its original shape (3x3)

#exampple of array concatenation
list7 = np.array([1, 2, 3]) 
list8 = np.array([4, 5, 6])
print(np.concatenate((list7, list8)))  # Output: [1 2 3 4 5 6], concatenating two arrays along the first axis
list9 = np.array([[1, 2], [3, 4]])  
list10 = np.array([[5, 6], [7, 8]])
print(np.concatenate((list9, list10), axis=0))  # Output: [[1 2] [3 4] [5 6] [7 8]], concatenating two 2D arrays along the first axis (rows)
print(np.concatenate((list9, list10), axis=1))  # Output: [[1 2 5 6] [3 4 7 8]], concatenating two 2D arrays along the second axis (columns)



#example of array splitting

list11 = np.array([1, 2, 3, 4, 5, 6])
print(np.split(list11, 3))  # Output: [array([1, 2]), array([3, 4]), array([5, 6])], splitting the array into 3 equal parts
list12 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(np.split(list12, 2, axis=0))  # Output: [array([[1, 2], [3, 4]]), array([[5, 6], [7, 8]])], splitting the 2D array into 2 equal parts along the first axis (rows)
print(np.split(list12, 2, axis=1))  # Output: [array([[1], [3], [5], [7]]), array([[2], [4], [6], [8]])], splitting the 2D array into 2 equal parts along the second axis (columns)



                  
#example of array sorting
list13 = np.array([3, 1, 4, 1, 5, 9])
print(np.sort(list13))  # Output: [1 1 3 4 5 9], sorting the array in ascending order
print(np.argsort(list13))  # Output: [1 3 0 2 4 5], returning the indices that would sort the array
list14 = np.array([[3, 1], [4, 1], [5, 9]])
print(np.sort(list14, axis=0))  # Output: [[3 1]    [4 1] [5 9]], sorting the 2D array along the first axis (rows)
print(np.sort(list14, axis=1))  # Output: [[1 3] [1 4] [5 9]], sorting the 2D array along the second axis (columns) 



#example of array filtering
list15 = np.array([1, 2, 3, 4, 5])
print(list15[list15 > 3])  # Output: [4 5], filtering the array to include only elements greater than 3
list16 = np.array([[1, 2], [3, 4], [5, 6]]) 
print(list16[list16 > 3])  # Output: [4 5 6], filtering the 2D array to include only elements greater than 3


#example of random number generation
print(np.random.rand(5))  # Output: [0.12345678 0.23456789 0.34567890 0.45678901 0.56789012], generating an array of 5 random numbers between 0 and 1
print(np.random.randint(0, 10, size=5))  # Output: [0 1 2 3 4], generating an array of 5 random integers between 0 and 9
print(np.random.normal(0, 1, size=5))  # Output: [-0.12345678 0.23456789 -0.34567890 0.45678901 -0.56789012], generating an array of 5 random numbers from a normal distribution with mean 0 and standard deviation 1
print("Random number generation:")
print(np.random.rand(2,2))  # Output: [[0.12345678 0.23456789] [0.34567890 0.45678901]], generating a 2D array of random numbers between 0 and 1 with shape (2, 2) 

print(np.random.randint(0, 10, size=(2, 3)))  # Output: [[0 1 2] [3 4 5]], generating a 2D array of random integers between 0 and 9 with shape (2, 3) means 2 rows and 3 columns
print(np.random.normal(0, 1, size=(2, 2)))  # Output: [[-0.12345678 0.23456789] [-0.34567890 0.45678901]], generating a 2D array of random numbers from a normal distribution with mean 0 and standard deviation 1 with shape (2, 2)



np.random.seed(0)  # Setting a random seed for reproducibility every time you run the code, it will generate the same random numbers
print(np.random.rand(5))  # Output: [0.54881351 0.71518937 0.60276338 0.54488318 0.4236548 ], generating the same array of random numbers each time the code is run due to the fixed random seed


# explain the full function - creates a 3x3 NumPy array (3 rows, 3 columns)
#  filled entirely with the value 100. The first argument (3,3) specifies the shape (dimensions) of the array, 
# and the second argument 100 is the fill value.

print(np.full((3,3),100))

#example
#print(list1[list1>30]) uses boolean indexing to filter the array. It first evaluates list1 > 30, which creates a boolean array [False, False, False, True, True] (True where elements > 30). Then list1[...] selects only the elements corresponding to True positions.

list1 = np.array([10,20,30,40,50])
print(list1[list1>30]) # Output: [40 50]

#example-
list2 = np.array([[1, 2,3], [4, 5, 6]])
print(np.sum(list2, axis=0))  # Output: [5 7 9],collumn wise sum summing the elements of the array along the first axis (columns)
print(np.sum(list2, axis=1))  # Output: [6 15], row wise sum summing the elements of the array along the second axis (rows)


#example of reshaping an array
print("example of reshaping an array:")
list3 = np.arange(6)  # creates a 1D array with values from 0 to 5

# The `reshape()` method in NumPy is used to change the shape of an array without changing its data. It takes a tuple as an argument that specifies the new shape of the array. The total number of elements in the new shape must be the same as the total number of elements in the original array.
#reshape convert 1D array to multi dimensional array and vice versa
print(list3.reshape(2, 3))  # Output: - 2 rows and 3 columns -- [[0 1 2] [3 4 5]], reshaping the 1D array into a 2D array with 2 rows and 3 columns
print(list3.reshape(3, 2))  # Output: - 3 rows and 2 columns -- [[0 1] [2 3] [4 5]], reshaping the 1D array into a 2D array with 3 rows and 2 columns 

# The `flatten()` method in NumPy is used to convert a multi-dimensional array into a 1D array. It takes all the elements of the original array and arranges them in a single dimension. This can be useful when you want to simplify the structure of an array or when you need to perform operations that require a 1D array.
list4 =list3.flatten()  # Output: [0 1 2 3 4 5], flattening the array back to a 1D array
print(list4)

list5 = np.array([1,2])
print(list5.reshape(-1,1))  # Output: [[1] [2]], 
#reshaping the 1D array into a 2D array with an automatically determined number of rows and 1 column 
# (the -1 tells NumPy to calculate the appropriate number of rows based on the total number of elements and the specified number of columns  )

#example of transposing an array
print("example of transposing an array:")   
list5 = np.array([[1, 2, 3], [4, 5, 6]])
print(list5.T)  # Output: [[1 4] [2 5] [3 6]], transposing the array (swapping rows and columns)

#example of vertical and horizontal stacking of arrays
print("example of vertical and horizontal stacking of arrays:")
list6 = np.array([1, 2])
list7 = np.array([5, 6])
print(np.vstack((list6, list7)))  # Output: [[1 2] [5 6]], vertically stacking the two arrays (stacking them on top of each other)
print(np.hstack((list6, list7)))  # Output: [1 2 5 6], horizontally stacking the two arrays (stacking them side by side)    

#example of array splitting
print("example of array splitting:")
list8 = np.array([1, 2, 3, 4, 5, 6])
print(np.split(list8, 3))  # Output: [array([1, 2]), array([3, 4]), array([5, 6])], splitting the array into 3 equal parts
newlist = np.split(list8, 3) #
print(newlist[0]) # Output: [1 2], accessing the first part of the split array

list9 = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(np.split(list9, 2, axis=0))  # Output: [array([[1, 2], [3, 4]]), array([[5, 6], [7, 8]])], splitting the 2D array into 2 equal parts along the first axis (rows)
print(np.split(list9, 2, axis=1))  # Output: [array([[1], [3], [5], [7]]), array([[2], [4], [6], [8]])], splitting the 2D array into 2 equal parts along the second axis (columns)  

#example of Reference copy
print("example of Reference copy:")
list10 = np.array([1, 2, 3])
list11 = list10  # This creates a reference copy, both list10 and list11 point to the same array in memory
list11[0] = 10  # Modifying list11 will also modify list10
print(f"list10: {list10}")  # Output: [10 2 3]
print(f"list11: {list11}")  # Output: [10 2 3]
#example of Deep copy
print("example of Deep copy:")
list12 = np.array([1, 2, 3])
list13 = list12.copy()  # This creates a deep copy, list13 is a new array in memory
list13[0] = 10  # Modifying list13 will not affect list12
print(f"list12: {list12}")  # Output: [1 2 3]
print(f"list13: {list13}")  # Output: [10 2 3]

#example of boolean indexing
print("example of boolean indexing:")
list14 = np.array([1, 2, 3, 4, 5])
print(list14[list14 > 3])  # Output: [4 5], filtering the array to include only elements greater than 3
list15 = np.array([[1, 2], [3, 4], [5, 6]])
print(list15[list15 > 3])  # Output: [4 5 6], filtering the 2D array to include only elements greater than 3    

#example of dot product of two arrays
print("example of dot product of two arrays:")
list16 = np.array([[1, 2], [3, 4]]) 
list17 = np.array([[5, 6], [7, 8]])
print(np.dot(list16, list17))  # Output: [[19 22] [43 50]], calculating the dot product of two 2D arrays (matrix multiplication)

#example of transpose 
print("example of transpose:")
list18 = np.array([[1, 2, 3], [4, 5, 6]])   
print(list18.T)  # Output: [[1 4] [2 5] [3 6]], transposing the array (swapping rows and columns)   

