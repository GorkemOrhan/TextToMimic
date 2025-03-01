import numpy as np
import matplotlib.pyplot as plt
import mouth_shape as ms
def interpolate_shapes(shape1, shape2, t):
    """
    shape1 ile shape2 arasında t (0 ile 1 arasında) oranında lineer interpolasyon yapar.
    """
    shape1 = np.array(shape1)
    shape2 = np.array(shape2)
    return (1 - t) * shape1 + t * shape2

# Örnek: 'notr' -> 'acik' geçişi
if __name__ == "__main__":
    shape_start = ms.get_mouth_shape("notr")
    shape_end = ms.get_mouth_shape("acik")
    
    plt.ion()  # interactive mode açıyoruz
    fig, ax = plt.subplots()
    
    for t in np.linspace(0, 1, 20):
        shape_interp = interpolate_shapes(shape_start, shape_end, t)
        x = [shape_interp[0][0], shape_interp[2][0], shape_interp[1][0], shape_interp[3][0], shape_interp[0][0]]
        y = [shape_interp[0][1], shape_interp[2][1], shape_interp[1][1], shape_interp[3][1], shape_interp[0][1]]
        ax.clear()
        ax.plot(x, y, marker='o')
        ax.set_title(f"Interpolation (t = {t:.2f})")
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 2)
        ax.set_aspect('equal', adjustable='box')
        plt.pause(0.1)
    
    plt.ioff()
    plt.show()
