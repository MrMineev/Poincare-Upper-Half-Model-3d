from disk_model.poincare import BallModel 
from disk_model.objects import PoincareLine, PoincareSphere, PoincarePoint
from camera import PoincareCamera
from visual import plot_hyperbolic
from tools import get_line_through_point
import math
import numpy as np

ball = BallModel()

ball.add_object(PoincareSphere([3, 3, 5], 2))

camera = PoincareCamera(PoincarePoint(4, 3, 2))

ball.set_camera(camera)

plot_hyperbolic(ball)



