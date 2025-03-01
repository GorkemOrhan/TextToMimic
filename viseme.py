def text_to_viseme(text):
    viseme = []
    for letter in text.lower():
        if letter in "aeo":
            viseme.append("open")
        elif letter in "mbp":
            viseme.append("close")
        else:
            viseme.append("neutral")
    return viseme

if __name__ == "__main__":
    ornek_text = "Merhaba"
    sonuc = text_to_viseme(ornek_text)
    print(f"text: {ornek_text}")
    print(f"Viseme dizisi: {sonuc}")
