import numpy as np
import matplotlib.pyplot as plt

# ---------- Metin -> Viseme Dönüşümü Modülü ----------
def metin_to_viseme(metin):
    """
    Verilen metindeki harflere göre basit bir viseme dizisi oluşturur.
    - Sesli harfler (a, e, o) için 'acik'
    - m, b, p gibi harfler için 'kapali'
    - Diğer harfler için 'notr'
    """
    viseme = []
    for harf in metin.lower():
        if harf in "aeo":
            viseme.append("acik")
        elif harf in "mbp":
            viseme.append("kapali")
        else:
            viseme.append("notr")
    return viseme

# ---------- Ağız Şekli ve Deformasyon Modülü ----------
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

def interpolate_shapes(shape1, shape2, t):
    """
    shape1 ile shape2 arasında t (0 ile 1 arasında) oranında lineer interpolasyon yapar.
    """
    shape1 = np.array(shape1)
    shape2 = np.array(shape2)
    return (1 - t) * shape1 + t * shape2

# ---------- Animasyon Modülü ----------
def animate_viseme_sequence(metin, frames_per_transition=20):
    """
    Verilen metni alır, harf bazında viseme dizisi üretir ve her iki ardışık viseme arasında 
    interpolasyon yaparak animasyonu oluşturur.
    """
    viseme_seq = metin_to_viseme(metin)
    print("Üretilen viseme dizisi:", viseme_seq)
    
    plt.ion()  # Interactive mode aç
    fig, ax = plt.subplots()
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 2)
    ax.set_aspect('equal', adjustable='box')
    
    # Her ardışık iki viseme arasında geçiş animasyonu
    for i in range(len(viseme_seq) - 1):
        shape_start = get_mouth_shape(viseme_seq[i])
        shape_end = get_mouth_shape(viseme_seq[i+1])
        for t in np.linspace(0, 1, frames_per_transition):
            shape_interp = interpolate_shapes(shape_start, shape_end, t)
            # Ağızı oluşturacak noktaları belirle:
            x = [shape_interp[0][0], shape_interp[2][0], shape_interp[1][0], shape_interp[3][0], shape_interp[0][0]]
            y = [shape_interp[0][1], shape_interp[2][1], shape_interp[1][1], shape_interp[3][1], shape_interp[0][1]]
            ax.clear()
            ax.plot(x, y, marker='o')
            ax.set_xlim(0, 4)
            ax.set_ylim(0, 2)
            ax.set_aspect('equal', adjustable='box')
            ax.set_title(f"Geçiş: {viseme_seq[i]} -> {viseme_seq[i+1]} (t = {t:.2f})")
            plt.pause(0.1)
    
    plt.ioff()
    plt.show()

# ---------- Uygulama ----------
if __name__ == "__main__":
    text_input = "Merhaba"
    animate_viseme_sequence(text_input)
