import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_hyperbolic(ball):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    camera, objects = ball.get_objects()

    for obj in objects:
        x, y, z = obj.gen_points()
        ax.plot(x, y, z, color='b', alpha=0.6)

    x, y, z = camera.get_point().gen_points()
    ax.scatter(x, y, z, color='r', s=100)

    for obj in camera.get_view():
        x, y, z = obj.gen_points()
        ax.plot(x, y, z, color='y', alpha=0.4)

    ax.set_box_aspect([1,1,1])
    ax.set_xlim3d([0, 10])
    ax.set_ylim3d([0, 10])
    ax.set_zlim3d([0, 10])

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.legend()

    plt.show()

