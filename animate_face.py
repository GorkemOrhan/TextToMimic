import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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

# ---------- Animasyonu Yüz Fotoğrafı Üzerinde Gösterme ----------
def animate_viseme_on_face(face_image_path, metin, frames_per_transition=20):
    """
    Yüz fotoğrafı üzerinde, verilen metne göre ağız animasyonunu oluşturur.
    """
    # Yüz fotoğrafını yükle
    img = mpimg.imread(face_image_path)
    
    # Bu örnekte, ağız bölgesini temsil etmek için bir "mouth box" belirleyeceğiz.
    # (x_min, y_min, x_max, y_max) şeklinde; bu değerler kullandığın fotoğrafa göre ayarlanmalı.
    mouth_box = [539, 436, 669, 484]  # Bu örnek koordinatlar, denemeler yaparak ayarlayabilirsin.
    
    viseme_seq = metin_to_viseme(metin)
    print("Üretilen viseme dizisi:", viseme_seq)
    
    plt.ion()
    fig, ax = plt.subplots()
    
    # Her ardışık iki viseme arasında geçiş animasyonu
    for i in range(len(viseme_seq) - 1):
        shape_start = get_mouth_shape(viseme_seq[i])
        shape_end = get_mouth_shape(viseme_seq[i+1])
        for t in np.linspace(0, 1, frames_per_transition):
            shape_interp = interpolate_shapes(shape_start, shape_end, t)
            
            # Şimdi, bu ağız şekli koordinatlarını mouth_box boyutlarına dönüştürelim.
            x_min, y_min, x_max, y_max = mouth_box
            transformed_shape = []
            for point in shape_interp:
                x, y = point
                # x için: [1, 3] aralığından mouth_box'un x aralığına dönüşüm
                x_mapped = x_min + ((x - 1) / (3 - 1)) * (x_max - x_min)
                # y için: yaklaşık [0.3, 1.7] aralığından mouth_box'un y aralığına dönüşüm
                y_mapped = y_min + ((y - 0.3) / (1.7 - 0.3)) * (y_max - y_min)
                transformed_shape.append([x_mapped, y_mapped])
            transformed_shape = np.array(transformed_shape)
            
            # Dönüştürülmüş koordinatları kullanarak poligon oluştur
            poly_x = [transformed_shape[0,0], transformed_shape[2,0], transformed_shape[1,0], transformed_shape[3,0], transformed_shape[0,0]]
            poly_y = [transformed_shape[0,1], transformed_shape[2,1], transformed_shape[1,1], transformed_shape[3,1], transformed_shape[0,1]]
            
            # Görüntüyü ve ağız şeklinin overlay'ini çiz
            ax.clear()
            ax.imshow(img)
            ax.plot(poly_x, poly_y, marker='o', color='red')
            ax.set_title(f"Geçiş: {viseme_seq[i]} -> {viseme_seq[i+1]} (t = {t:.2f})")
            plt.pause(0.1)
    
    plt.ioff()
    plt.show()

# ---------- Uygulama ----------
if __name__ == "__main__":
    face_image_path = "face.jpg"  # Yüz fotoğrafının dosya yolunu buraya gir.
    metin = "Merhaba"
    animate_viseme_on_face(face_image_path, metin)
