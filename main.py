meme_dict = {
            "cringe": "Sesuatu yang sangat aneh atau memalukan",
            "lol": "Tanggapan umum terhadap sesuatu yang lucu",
            "rofl": "tanggapan terhadap lelucon",
            "sheesh": "sedikit ketidaksetujuan",
            "creepy": "menakutkan, tidak menyenangkan",
            "aggro": "untuk menjadi agresif/marah",
            }
print("Selamat datang!")
for i in range(5): 
    word = input("Ketik kata yang tidak Kamu mengerti: ").lower().strip()
    if word in meme_dict.keys():
        # Apa yang harus kita lakukan jika kata itu ditemukan?
        print(meme_dict[word])
    else:
        print("kata tidak ditemukan")
        # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
print("Senang bisa membantu")
