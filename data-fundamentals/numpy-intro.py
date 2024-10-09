"""
    NumPy: Numerica Python
        Alternative to Python List: Numpy Array
        Calculations over entire arrays
        Easy and fast    
"""

import numpy as np

heights = [1.73, 1.68, 1.71, 1.89, 1.79]
weights = [65.4, 59.2, 63.6, 88.4, 68.7]

np_heights = np.array(heights)
np_weights = np.array(weights)

# This operation is not possible using the standard python list. To do this in ordinary python you would have to iterate over through the list.
bmi = np_weights/(np_heights ** 2) 

# NOTE
"""
    Numpy array must contain only one datatype
    Numpy array comes with its own methods, which behaves differently from the regular python array methods
    Subsetting (using the square bracket notation on lists or arrays) works exactly the same with both lists and arrays. 
    i.e heights[2:5] will produce the same result as np_heights[2:5]
"""
print(f"The BMI for the individuals wit the respective weight and height is: {bmi}")
print("The data type for np_weights is: ", type(np_weights))

# Subsetting
# Indexing
print("The BMI for the second person is: ", bmi[1])

print(bmi > 23) # Print an array of booleans for the values greater than 23

print(bmi[bmi > 23]) # Print an array with bmi values greater than 23


# 2D NumPy Arrays 
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

print(type(np_weight)) # print <class 'numpy.ndarray'> the ndarray stands for n-dimensional array

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], [65.4, 59.2, 63.6, 88.4, 68.7]])

print("To view the shape of a numpy array: ", np_2d.shape)

# Subsetting
print(np_2d[0]) # array([[1.73, 1.68, 1.71, 1.89, 1.79])
print(np_2d[0][2]) # 1.71
print(np_2d[0, 2]) # 1.71
print(np_2d[:, 1:3]) # ":" means take all rows "1:3" means start from the second column but stop at the forth column and do not include the forth column. array([[ 1.68,  1.71],  [59.2 , 63.6 ]])
print(np_2d[1, :]) # Take the second row and print everything in it. array([65.4, 59.2, 63.6, 88.4, 68.7])