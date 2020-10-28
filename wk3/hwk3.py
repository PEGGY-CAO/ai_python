import numpy as np

import pandas as pd

temps = np.random.randint(60, 101, 6)

temperatures = pd.Series(temps)

# 1. Displaying the data
print(temps)
print(temperatures)

# 2. Displaying the minimum value
print("minimum value: ", min(temps))

# 3.	Displaying the maximum value
print("maximum value: ",max(temps))

# 4.	Displaying the mean
print("mean value: ",np.mean(temps))

