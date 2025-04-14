class Patsient:
    def __init__(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus

class Haigla:
    def patsiendideKuuvamine(patsiendiList):
        for index,elem in enumerate(patsiendiList):
            print("ID: ", index,"Nimi: ",elem.nimi, "V anus: ", elem.vanus)


Patsient1 = Patsient("Bogdan sosu za vodu", 0.00000000000000000000000000001)
Patsient2 = Patsient("Marko", 42)
Patsient3 = Patsient("Nikita Buket", 8)
Patsient4 = Patsient("Irina Merkulova", 362869238692)
Patsient5 = Patsient("Golavach Lena", 12)
Patsient6 = Patsient("GOD", 19106930180603810682068208609510)
Patsient7 = Patsient("Obladaet", 52)
patsiendiList = [Patsient1, Patsient2, Patsient3, Patsient4, Patsient5, Patsient6, Patsient7]

haigla = Haigla()
haigla.patsiendideKuuvamine()