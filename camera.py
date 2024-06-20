from disk_model.objects import PoincarePoint
from tools import get_line_through_point
import numpy as np

class PoincareCamera:
    VIEW_X, VIEW_Y = 1.4, 1.4
    EPS = 1 / 30 

    def __init__(self, p, dir=np.array([1, 1, 1])):
        self.p = p
        self.dir = dir
        self.camera_view = []

    def make_view_lines(self):
        self.camera_view = []
        for x in np.arange(-self.VIEW_X, self.VIEW_X, self.EPS):
            for y in np.arange(-self.VIEW_Y, self.VIEW_Y, self.EPS):
                pos = self.dir + np.array([x, y, np.sqrt(self.VIEW_X ** 2 - x ** 2 - y ** 2)])
                self.camera_view.append(get_line_through_point(self.p.euclid_convert(), pos))

    def get_point(self):
        return self.p

    def get_view(self):
        self.make_view_lines()
        return self.camera_view

