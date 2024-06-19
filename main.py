from disk_model.poincare import DiskModel
from disk_model.objects import PoincareLine, PoincareSphere
from visual import plot_hyperbolic
import math
import numpy as np

poincare_line = PoincareSphere(np.array([4, 4, 4]), 2)

plot_hyperbolic(poincare_line)



