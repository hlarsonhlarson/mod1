import numpy as np
import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.point = np.array([[x, 0, 0], [0, y, 0], [0, 0, z]])

    def transforming_point(self, alpha):
        x_rotation_matrix = np.array([[1, 0, 0], [0, math.cos(alpha), -math.sin(alpha)], [0, math.sin(alpha), math.cos(alpha)]])
        y_rotation_matrix = np.array([[math.cos(alpha), 0, math.sin(alpha)], [0, 1, 0], [-math.sin(alpha), 0, math.cos(alpha)]])
        z_rotation_matrix = np.array([[math.cos(alpha), -math.sin(alpha), 0], [math.sin(alpha), math.cos(alpha), 0], [0, 0, 1]])
        self.point = np.dot(self.point, x_rotation_matrix)
        self.point = np.dot(self.point, y_rotation_matrix)
        self.point = np.dot(self.point, z_rotation_matrix)
        self.x = self.point[0][0]
        self.y = self.point[1][1]
        self.z = self.point[2][2]
