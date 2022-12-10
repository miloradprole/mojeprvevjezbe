class Osoba:
    ime = ""
    prezime = ""
    godine = 0

osoba1 = Osoba()
print(osoba1.godine)
osoba1.ime = "Midad"
osoba1.prezime = "Sobic"
osoba1.godine = 25

print(osoba1.ime, osoba1.prezime, osoba1.godine)

osoba2 = Osoba()
osoba2.ime = "Dule"
osoba2.prezime = "Peretinov"
osoba2.godine = 50

print(osoba2.ime, osoba2.prezime, osoba2.godine)

prisutni = [osoba1, osoba2]

for o in prisutni:
    print(f"Ime: {o.ime}")
    print(f"Prezime: {o.prezime}")