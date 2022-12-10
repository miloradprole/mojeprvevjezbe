
class Automobil:
    marka = ""
    model = ""
    godiste = 0
    alu_felne = False

    broj_tockova = 4 # staticko svojstvo, zajednicko za sve

    #metode unutar klase:

    def vozi(self):
        print("auto je u pokretu")
        print(self.model)

    def postavi_felne(self):
        if self.alu_felne == True:
            print("imate vec alu felne")
        else:
            self.alu_felne = True
            print("postavljene su alu felne")

auto1 = Automobil()     # objekat / instanca - instanciranje klase
auto1.marka = "citroen"
auto1.model = "c4"
auto1.godiste = 2014
auto1.alu_felne = False
print(auto1.marka, auto1.marka, auto1.godiste, auto1.alu_felne)

print(Automobil.broj_tockova) # svakom statickom svojstvu se moze pristupiti na ovakakav nacin

auto1.vozi()

auto1.postavi_felne() #metoda koju sam ja napravio


slova = "AbcD"
slova = str()

slova.upper()
slova.lower()  # metoda stringa ugradjena