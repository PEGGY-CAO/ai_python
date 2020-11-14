import numpy as np

class Question_3:
    array = np.arange(2, 41, 2).reshape(4, 5)

    def printAll(self):
        print(self.array)


example = Question_3()
example.printAll()
