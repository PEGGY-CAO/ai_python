import numpy as np

class Question_3:
    array = np.random.randint(60, 101, size=12).reshape(3, 4)

    def printAll(self):
        print(self.array)
        print("Calculate the average of all the grades")
        print(np.mean(self.array))
        print("the averages of the grades in each column")
        print(self.array.mean(axis=0))
        print("the averages of the grades in each row.")
        print(self.array.mean(axis=1))


example = Question_3()
example.printAll()
