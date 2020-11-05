import numpy as np


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.point = np.array([[x, 0, 0], [0, y, 0], [0, 0, z]])
