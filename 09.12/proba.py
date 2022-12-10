# # import car
# from car import *

# auto1 = Automobil()

# print(auto1.model, auto1.marka, auto1.alu_felne, auto1.godiste)

class Automobil:
    broj_tockova = 4

    def __init__(self, marka, model, godiste, alu_felne):
        print("pravim automobil")
        self.marka = marka
        self.model = model
        self.godiste = godiste
        self.alu_felne = alu_felne

a = Automobil("citroen", "c4", 2014, False)

a.marka


#osoba
#ime, prezime, godine

class Osoba:

    def __init__(self, ime, prezime, godine):
        print("osoba je ovog opisa:")
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

o = Osoba("Midad", "Sobic", 55)

o2 = Osoba("Dule", "Peretinov", 69)
print(o2.ime)



        