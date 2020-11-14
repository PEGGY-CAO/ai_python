import numpy as np

class Question_3:
    array = np.array([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10],
           [11, 12, 13, 14, 15]])

    def printAll(self):
        print("question a")
        print(self.array[1])

        print("\nquestion b")
        print(self.array[[0, 2]])

        print("\nquestion c")
        print(self.array[:,1:4])


example = Question_3()
example.printAll()
