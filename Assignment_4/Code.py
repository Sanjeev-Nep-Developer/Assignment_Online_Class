import numpy as np

# 1) Task 1
import numpy as np
print(np.__version__)

# 2) Task 2


# A) Create a 1D NumPy array from a Python list of numbers: [1, 2, 3, 4, 5].
# 1D Numpy Array
first_array = np.array([1, 2, 3, 4, 5])
print(first_array)
print(first_array.ndim)


# B) Create a 2D NumPy array of shape (3x3) using the numbers from 1 to 9.
# 2D Numpy Array
second_array = np.arange(1, 10).reshape(3, 3)
print(second_array)


# C) Generate an array of 10 evenly spaced values between 0 and 5.
# 10 Evenly spaced Values between 0 and 5
third_array = np.linspace(0, 5, 10)
print(third_array)


# 3) Task 3:


# A) Access the element in the second row, third column of the 2D array you created above.
arr = np.arange(1, 17).reshape(2, 8)
print(arr)
print(arr[1, 2])
print(arr[1][2])


# B) Slice the first two rows and the first two columns from the same array.
print(arr[:2, :2])


# C) Modify the value in the last row and first column to 100.
arr[-1][0] = 100
print(arr)


# 4) Task 4

# A) Find the shape, size, and data type of the 2D array.
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array.shape)
print(array.size)
print(type(array))

# B) Change the 1D array into a 2D array of shape (5,1).
array2 = np.arange(5)
print(array2.size)
print(array2.ndim)
array3 = array2.reshape(5, 1)
print(array3)
print(array3.ndim)


# C) Flatten a multi-dimensional array back into a 1D array.
array4 = array3.flatten()
print(array4)
print(array4.ndim)

# 5) Task 5


# A) Add 5 to every element in the 1D array.
first_array = np.array([10, 20, 30, 40, 50, 60])
first_array += 5
print(first_array)


# B) Multiply the 2D array by 3.
second_array = np.array([[10, 20, 30], [40, 50, 60]])
print(second_array * 2)


# C) Perform matrix multiplication between the following two arrays:
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# result = A @ B
result = np.dot(A, B)
print(result)


# 6)  Task 6:

# A) Create a 3x3 matrix of ones and a 1D array of length 3.
first_matrix = np.ones((3, 3))
print(first_matrix)
second_array = np.arange(3)
print(second_array)
print(len(second_array))


# B) Add the 1D array to each row of the matrix using broadcasting.

result = np.add(first_matrix, second_array)
print(result)
