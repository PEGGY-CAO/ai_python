# Given the following array:
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15]])
# write statements to perform the following tasks:
#
# a. Select the second row.
#
# b. Select the first and third rows.
#
# c. Select the middle three columns.
import numpy as np

array = np.array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15]])
print("question a")
print(array[1])

print("\nquestion b")
print(array[[0, 2]])

print("\nquestion c")
print(array[:,1:4])
