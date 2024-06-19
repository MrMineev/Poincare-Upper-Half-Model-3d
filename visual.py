import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_hyperbolic(obj):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x, y, z = obj.gen_points()

    ax.plot(x, y, z, label='Circle through A and B')

    ax.set_box_aspect([1,1,1])
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.legend()
    plt.show()

