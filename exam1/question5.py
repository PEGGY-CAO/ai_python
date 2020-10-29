# Use NumPy random-number generation to create an array of twelve random grades in the range 60 through 100,
# then reshape the result into a 3-by-4 array.

# the averages of the grades in each column
# and the averages of the grades in each row.

import numpy as np

array = np.random.randint(60, 101, size=12).reshape(3, 4)
print(array)
print("Calculate the average of all the grades")
print(np.mean(array))
print("the averages of the grades in each column")
print(array.mean(axis=0))
print("the averages of the grades in each row.")
print(array.mean(axis=1))
