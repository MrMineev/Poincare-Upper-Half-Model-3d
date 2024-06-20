import numpy as np

class BallModel:
    def __init__(self):
        self.objects = []
        self.camera = None

    def add_object(self, obj):
        self.objects.append(obj)

    def set_camera(self, obj):
        self.camera = obj

    def get_objects(self):
        return self.camera, self.objects


