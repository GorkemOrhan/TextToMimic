import numpy as np
import matplotlib.pyplot as plt

def get_mouth_shape(state):
    """
    Verilen duruma göre ağız kontrol noktalarını döndürür.
    Kontrol noktaları: [sol_kose, sag_kose, ust_orta, alt_orta]
    """
    mouth_shapes = {
        "notr": np.array([[1, 1], [3, 1], [2, 1.5], [2, 0.5]]),
        "acik": np.array([[1, 1], [3, 1], [2, 1.7], [2, 0.3]]),   # Ağız daha açık
        "kapali": np.array([[1, 1], [3, 1], [2, 1.4], [2, 0.6]]),  # Ağız daha kapalı
    }
    return mouth_shapes.get(state, mouth_shapes["notr"])

def plot_mouth(shape, title="Mouth Shape"):
    """
    Verilen ağız şeklini basit bir çizim olarak plot eder.
    """
    shape = np.array(shape)
    # Noktaları, ağızın çevresinde bir poligon oluşturacak şekilde sırala:
    # Sol köşe -> Üst orta -> Sağ köşe -> Alt orta -> Sol köşe (kapatmak için)
    x = [shape[0][0], shape[2][0], shape[1][0], shape[3][0], shape[0][0]]
    y = [shape[0][1], shape[2][1], shape[1][1], shape[3][1], shape[0][1]]
    
    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlim(0, 4)
    plt.ylim(0, 2)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Test edelim:
if __name__ == "__main__":
    for state in ["notr", "acik", "kapali"]:
        shape = get_mouth_shape(state)
        plot_mouth(shape, title=f"Mouth Shape for '{state}' state")
