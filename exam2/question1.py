import numpy as np

import pandas as pd

class Question_1:
    temps = np.random.randint(60, 100, 5)
    temperatures = pd.Series(temps)

    def printAll(self):
        print(self.temperatures)
        print("Lowest temperature: ", min(self.temps))
        print("Highest temperature: ",max(self.temps))
        print("Average temperature: ",np.mean(self.temps))
        print("Other descriptive statistics: ")
        print("Median temperature: ", np.median(self.temps))
        print("Standard deviation (or variance): ", np.var(self.temps))

example = Question_1()
example.printAll()


