# How to import numpy
import numpy as np

# How to check the version of the numpy package
print('numpy:', np.__version__)
# Checking the available methods
print(dir(np))

python_list = [1, 2, 3, 4, 5]

# Checking data types
print('Type:', type(python_list))  # <class 'list'>
#
print(python_list)  # [1, 2, 3, 4, 5]

two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Creating Numpy(Numerical Python) array from python list

numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))  # <class 'numpy.ndarray'>
print(numpy_array_from_list)  # array([1, 2, 3, 4, 5])

#Creating float numpy arrays
python_list_one = [1, 2, 3, 6, 9]
numpy_array_list_one = np.array(python_list_one, dtype=float)
print(numpy_array_list_one)

#Creating boolean numpy arrays
python_list_two = [1, -1, 0, 0]
numpy_array_bool = np.array(python_list_two, dtype=bool)
print(numpy_array_bool)

#Creating multidimensional array using numpy
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_array =  np.array(two_dimensional_list)
print(type(numpy_two_dimensional_array))
print(numpy_two_dimensional_array)

#Converting numpy array to list
np_to_list = numpy_array_list_one.tolist()
two_dimensional_np_to_list = numpy_two_dimensional_array.tolist()
print(two_dimensional_np_to_list)
print(np_to_list)

#Creating numpy array from tuple
python_tuple = (1, 2, 3, 4, 5)
np_from_tuple = np.array(python_tuple)
print(type(np_from_tuple))
print(np_from_tuple)

#Shape of numpy array
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_array)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_array.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
                                [4, 5, 6, 7],
                                [8, 9, 10, 11]])
print(three_by_four_array.shape)
