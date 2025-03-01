import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("face.jpg")
plt.imshow(img)

# Burada figür hâlâ açıkken, 2 noktaya tıklayacağız.
coords = plt.ginput(2)  # Fareyle iki farklı noktaya tıkla.
print(coords)

# Tıklama işlemi bitince (genelde pencereyi kapattığında),
# fonksiyon geri döner ve koordinatları ekrana yazar.
plt.show()
