# Given the following dictionary;
# temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82], 'Thu': [75, 97], 'Fri': [62, 79]}
#
# perform the following tasks:

import pandas as pd

temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82], 'Thu': [75, 97], 'Fri': [62, 79]}
# a. Convert the dictionary into the DataFrame named temperatures with Low and High
# as the indices, then display the DataFrame.
temperatures = pd.DataFrame(temps, index=['Low', 'High'])
print("question a")
print(temperatures)
# b. Use the column names to select only the columns for Mon through Wed.
subDF = temperatures[['Mon', 'Tue', 'Wed']]
print("\nquestion b")
print(subDF)
# c. Use the row index Low to select only the low temperatures for each day.
lowIndex = temperatures.loc['Low']
print("\nquestion c")
print(lowIndex)
# d. Set the floating-point precision to 2, then calculate the average temperature for each day.
print("\nquestion d")
meanTemp = temperatures.mean()
pd.options.display.float_format = '{:,.2f}'.format
print(meanTemp)
# e. Calculate the average low and high temperatures.
print("\nquestion e")
averageLowHigh = temperatures.mean(axis = 1)
print(averageLowHigh)
