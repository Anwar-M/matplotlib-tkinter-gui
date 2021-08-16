import numpy as np

class Model():
 
    def __init__(self):
        self.xpoint = 100
        self.ypoint = 100
        self.res = None
 
    def calculate(self):
        x = np.linspace(-6.3, 6.3, self.xpoint)
        # z = np.cos(x**2*y**3)
        y = np.cos(x)
        self.res = {"x": x, "y": y}