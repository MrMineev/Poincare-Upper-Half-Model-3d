from disk_model.objects import PoincareLine, PoincarePoint
import numpy as np

def get_dist_vec_3d(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

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




