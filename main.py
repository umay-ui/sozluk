kelimeler = {
    "piton" : "zehirsiz bir yılan türü",
    "laboratuvar" : "deney yapılan yer",
    "sefa" : "keyif"
}

while True:
    kelime = input("bir kelime girin")
    if kelime in list(kelimeler.keys()):
        print(kelimeler[kelime])
    else:
        anlami = input("anlamını girin")
        kelimeler[kelime] = anlami
        print(kelime, "sözlüğe eklendi")