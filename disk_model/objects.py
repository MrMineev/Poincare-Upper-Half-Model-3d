import math
from operator import rshift
from re import A
import numpy as np

def get_dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def points_between(a, b, num_points):
    # Ensure a and b are numpy arrays
    a = np.array(a)
    b = np.array(b)
    
    # Generate intermediate points
    t = np.linspace(0, 1, num_points)[:, np.newaxis]
    intermediate_points = a + t * (b - a)
    
    return intermediate_points

class PoincarePoint:
    def __init__(self, x, y, z, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.z = z

    def euclid_convert(self):
        return np.array([self.x, self.y, self.z])

    def gen_points(self):
        return [self.x], [self.y], [self.z]

class PoincareLine:
    NUM = 10 ** 3 

    def __init__(self, x1, y1, x2, y2, color=(0, 0, 0)):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    def get_center(self):
        center = [(self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2]
        radius = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) / 2
        return (center, radius)

    def info(self):
        print("== INFO ==")
        print(f"< {self.x1}, {self.y1} >")
        print(f"< {self.x2}, {self.y2} >")
        print("==  END ==")

    def gen_points(self):
        center, radius = self.get_center()

        points = points_between([self.x1, self.y1], [self.x2, self.y2], self.NUM)

        x, y, z = [], [], []

        for point in points:
            d = get_dist(center[0], center[1], point[0], point[1])
            z_value = math.sqrt(max(radius ** 2 - d ** 2, 0))

            x.append(point[0])
            y.append(point[1])
            z.append(z_value)

        return x, y, z 

class PoincareSphere:
    NUM = 10 ** 3 

    def __init__(self, center, r, color=(0, 0, 0)):
        self.center = center
        self.radius = r 
        self.color = color

    def gen_points(self):
        phi = np.random.uniform(0, 2 * np.pi, self.NUM)
        cos_theta = np.random.uniform(-1, 1, self.NUM)
        theta = np.arccos(cos_theta)
        
        x = self.center[0] + self.radius * np.sin(theta) * np.cos(phi)
        y = self.center[1] + self.radius * np.sin(theta) * np.sin(phi)
        z = self.center[2] + self.radius * np.cos(theta)

        return x, y, z



