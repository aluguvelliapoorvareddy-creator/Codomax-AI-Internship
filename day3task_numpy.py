<<<<<<< HEAD
import numpy as np

# 1. LEARN ARRAYS: Creating 1D and 2D arrays
print("--- 1. NumPy Array Creation ---")
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", array_1d)
print("2D Array:\n", array_2d)
print(f"Data Type: {array_1d.dtype}, Shape: {array_2d.shape}\n")


# 2. INDEXING: Accessing specific elements
print("--- 2. NumPy Indexing ---")
# Get the first element of the 1D array
first_element = array_1d[0]
# Get the element from the 2nd row, 3rd column of the 2D array (index 1, 2)
specific_element = array_2d[1, 2]

print("First element in 1D array:", first_element)
print("Element at row 2, col 3 in 2D array:", specific_element)


# 3. MATHEMATICAL OPERATIONS: Vector math and statistics
print("\n--- 3. Mathematical Operations ---")
# Element-wise operations
added_array = array_1d + 10
squared_array = array_1d ** 2

print("Array + 10:", added_array)
print("Array Squared:", squared_array)

# Basic statistics
array_mean = np.mean(array_1d)
array_sum = np.sum(array_2d)

print("Mean of 1D array:", array_mean)
=======
import numpy as np

# 1. LEARN ARRAYS: Creating 1D and 2D arrays
print("--- 1. NumPy Array Creation ---")
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", array_1d)
print("2D Array:\n", array_2d)
print(f"Data Type: {array_1d.dtype}, Shape: {array_2d.shape}\n")


# 2. INDEXING: Accessing specific elements
print("--- 2. NumPy Indexing ---")
# Get the first element of the 1D array
first_element = array_1d[0]
# Get the element from the 2nd row, 3rd column of the 2D array (index 1, 2)
specific_element = array_2d[1, 2]

print("First element in 1D array:", first_element)
print("Element at row 2, col 3 in 2D array:", specific_element)


# 3. MATHEMATICAL OPERATIONS: Vector math and statistics
print("\n--- 3. Mathematical Operations ---")
# Element-wise operations
added_array = array_1d + 10
squared_array = array_1d ** 2

print("Array + 10:", added_array)
print("Array Squared:", squared_array)

# Basic statistics
array_mean = np.mean(array_1d)
array_sum = np.sum(array_2d)

print("Mean of 1D array:", array_mean)
>>>>>>> 403898d6919eb6d6c784a0b01ccdc66cc693ba9b
print("Sum of all elements in 2D array:", array_sum)