def metin_to_viseme(metin):
    viseme = []
    for harf in metin.lower():
        if harf in "aeo":
            viseme.append("acik")
        elif harf in "mbp":
            viseme.append("kapali")
        else:
            viseme.append("notr")
    return viseme

if __name__ == "__main__":
    ornek_metin = "Merhaba"
    sonuc = metin_to_viseme(ornek_metin)
    print(f"Metin: {ornek_metin}")
    print(f"Viseme dizisi: {sonuc}")

