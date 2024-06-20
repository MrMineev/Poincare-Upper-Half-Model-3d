import numpy as np

class BallModel:
    def __init__(self):
        self.objects = []
        self.camera = None
        self.background_color = (3, 78, 252)

    def add_object(self, obj):
        self.objects.append(obj)

    def set_camera(self, obj):
        self.camera = obj

    def get_objects(self):
        return self.camera, self.objects

    def get_color(self, line):
        for obj in self.objects:
            res, _ = obj.is_intersect(line)
            if res == True:
                return obj.color
        return self.background_color


