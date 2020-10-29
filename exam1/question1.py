# Use the NumPy’s random number generation to create an array of five random integers that represent
# summertime temperatures in the range 60–100, then perform the following tasks:
#
# a. Convert the array into the Series named temperatures and display it.
#
# b. Determine the lowest, highest and average temperatures.
#
# c. Produce descriptive statistics for the Series.

import numpy as np

import pandas as pd

temps = np.random.randint(60, 100, 5)

temperatures = pd.Series(temps)
print(temperatures)
print("Lowest temperature: ", min(temps))
print("Highest temperature: ",max(temps))
print("Average temperature: ",np.mean(temps))
print("Other descriptive statistics: ")
print("Median temperature: ", np.median(temps))
print("Standard deviation (or variance): ", np.var(temps))
