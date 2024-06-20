from disk_model.objects import PoincareLine, PoincarePoint, get_dist_vec_3d
import numpy as np
import matplotlib.pyplot as plt

def get_line_through_point(p, dir):
    center_vec = np.array([dir[0], dir[1], -(dir[0] ** 2 + dir[1] ** 2) / dir[2]])
    q = p + center_vec

    x = ( -p[2] * (q[0] - p[0]) ) / ( q[2] - p[2] ) + p[0]
    y = ( -p[2] * (q[1] - p[1]) ) / ( q[2] - p[2] ) + p[1]

    center = np.array([x, y])
    radius = get_dist_vec_3d(np.array(p), np.array([x, y, 0]))

    diff = (np.array([p[0], p[1]]) - center)
    diff = diff / np.sqrt(diff.dot(diff))

    A = center + radius * diff
    B = center - radius * diff
    
    return PoincareLine(A[0], A[1], B[0], B[1])

def get_world_view(ball, camera):
    views = camera.get_view()
    camera_view = {}
    datax, datay, colors = [], [], []
    for view in views:
        color = np.array(ball.get_color(view)) / 255

        camera_view[(view.x1, view.y1)] = color
        datax.append(view.x2)
        datay.append(view.y2)
        colors.append(color)

    plt.scatter(datax, datay, c=colors, s=20)
    plt.show()

    return camera_view





