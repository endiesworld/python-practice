import numpy as np

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
"""
random.normal(loc=0.0, scale=1.0, size=None)
Draw random samples from a normal (Gaussian) distribution. 
The probability density function of the normal distribution. Is often called the bell curve because of its characteristic shape
Parameters:
    loc:
    float or array_like of floats
    Mean (“centre”) of the distribution.

    scale:
    float or array_like of floats
    Standard deviation (spread or “width”) of the distribution. Must be non-negative.

    size:
    int or tuple of ints, optional
    Output shape. If the given shape is, e.g., (m, n, k), then m * n * k samples are drawn. If size is None (default), a single value is returned if loc and scale are both scalars. Otherwise, np.broadcast(loc, scale).size samples are drawn.

Returns:
    out:
    ndarray or scalar
    Drawn samples from the parameterized normal distribution.

"""

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height, weight))

# Print out the mean of np_height_in
avg = np.mean(height)
print("Average: " , str(avg))

# Print out the median of np_height_in
med = np.median(height)
print("Median: ", str(med))

# # Print out the standard deviation on height. Replace 'None'
stddev = np.std(height)
print("Standard Deviation: " + str(stddev))