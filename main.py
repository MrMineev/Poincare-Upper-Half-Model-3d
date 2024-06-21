from disk_model.poincare import BallModel 
from disk_model.objects import PoincareLine, PoincareSphere, PoincarePoint
from camera import PoincareCamera
from visual import plot_hyperbolic
from tools import get_line_through_point, get_world_view
import math
import numpy as np

ball = BallModel()

ball.add_object(PoincareSphere([6, 6, 4], 1))
ball.add_object(PoincareSphere([5, 6, 3], 1, color=(34, 255, 0)))

camera = PoincareCamera(PoincarePoint(4, 3, 2), EPS=1/20)

ball.set_camera(camera)

plot_hyperbolic(ball, show_camera_view=False)

pixels = get_world_view(ball, camera)

print(pixels)



