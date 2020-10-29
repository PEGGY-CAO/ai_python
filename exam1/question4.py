# Use NumPy function arange to create an array of 20 even integers from 2 through 40,
# then reshape the result into a 4-by-5 array.

import numpy as np

array = np.arange(2, 41, 2).reshape(4, 5)
print(array)
