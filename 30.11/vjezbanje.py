# kljuc : vrednost, 

# osoba_recnik = {"ime": "Sofija", "godine": 25, "plava": True}
# print(osoba_recnik)
# print(osoba_recnik["ime"])

# for karakteristike in osoba_recnik:
#     print(osoba_recnik[karakteristike])


# for (kljuc, vrednost) in osoba_recnik.items():
#     print("ovo je kljuc:", kljuc)
#     print("ovo je vrednost:" , vrednost)

# osoba2 = {}

# osoba2["ime"] = "Marija"
# osoba2["godine"] = 35
# print(osoba2)

# osoba2["ime"] = "Sofija"
# print(osoba2)

# del osoba2["ime"]

# print(osoba2)

# poruke = {"en": "hello", "sr": "zdravo", "de": "hallo"}

# jezik = input("unesite jezik:")

# if jezik == "en" or jezik == "sr" or jezik == "de":
#     print(poruke[jezik])
# else:
#     print("nemamo ovaj prevod")




# poruke = {"en": "hello", "sr": "zdravo", "de": "hallo"}

# for (jezik, prevod) in poruke.items():
#     if jezik == "en":
#         print(f"{jezik} : {prevod}")
#     elif jezik == "sr":
#         print(f"{jezik} : {prevod}")
#     else:
#         print(f"{jezik} : {prevod}")

# poruke = {"en": "hello", "sr": "zdravo", "de": "hallo"}

# for (jezik, prevod) in poruke.items():
#     if jezik == "en":
#         print(f"Engleski: {prevod}")
#     elif jezik == "sr":
#         print(f"Srpski: {prevod}")
#     else:
#         print(f"Njemacki: {prevod}")

# selekcija = {
#     "drzava": "Srbija", 
#     "broj_pobeda": 0, 
#     "boje_dresova": ["crvena", "bela", "crna"], 
#     "brojevi_igraca": [9, 5, 12, 25]}



# for (kljuc, vrednost) in selekcija.items():
#     # print("kljuc: ", kljuc)
#     # print("vrednost: ", vrednost)
#     if kljuc == "boje_dresova":
#         for boje in vrednost:
#             print(f"boja dresa je: {boje}")
#     elif kljuc == "brojevi igraca":
#         for broj in vrednost:
#             print(f"brojevi igraca: {broj}")
#     else:
#         print(f"{kljuc}, {vrednost}")

# automobil = {"marka": "citroen", "model": "c3", "boje": ["crvena", "bela", "crna"], "alu_felne": False, "godiste": 2017, "kubikaza": 1.6}

# for (kljuc, vrednost) in automobil.items():
#     if kljuc == "marka":
#         print(f"marka automobila je: {vrednost}")
#     elif kljuc == "model":
#         print(f"model je: {vrednost}")
#     elif kljuc == "boje":
#         for boje in vrednost:
#             print(f"boja je: {boje}")
#     elif kljuc == "alu_felne":
#         if vrednost:
#             print("ima fele")
#         else:
#             print("nema fela")
#     elif kljuc == "godiste":
#         print()


# automobil = {
#     "marka": "citroen", 
#     "model": "c3", 
#     "boje": ["crvena", "bela", "crna"], 
#     "alu_felne": False, 
#     "godiste": 2017, 
#     "kubikaza": 1.6
# }

# for (kljuc, vrednost) in automobil.items():
#     if kljuc == "marka":
#         print(f"Marka je: {vrednost}")
#     elif kljuc == "c3":
#         print(f"Model je: {vrednost}")
#     elif kljuc == "boje":
#         for boje in vrednost:
#             print(f"boja je: {boje}")
#     elif kljuc == "alu_felne":
#         if vrednost:
#             print("ima feluge :)")
#         else:
#             print("nema feluge :(")
#     elif kljuc == "kubikaza":
#         print(f"zapremina motora je {vrednost} litara")


# automobili = {
#     "BG-123": { 
#     "marka": "citroen", 
#     "model": "c3", 
#     "kubikaza": 1.6, 
#     "boje": ["crvena", "bela", "crna"]
#     },
    
#     "BG-451": {
#     "marka": "opel", 
#     "model":"astra", 
#     "kubikaza": 2.0, 
#     "boje": ["plava", "zelena", "zuta"]
#     },
    
#     "BG-987": {
#     "marka": "audi", 
#     "model":"A8", 
#     "kubikaza": 3.0, 
#     "boje": ["plava", "zelena", "zuta"]
#     },
# }

# for (reg, detalji) in automobili.items():
#     # print(f"registracija je: {reg}")
#     # print(f"detalji automobila su: {detalji}")
#     for (automobil, karakteristike) in detalji.items():
#         print(f"{automobil} : {karakteristike}")
#     if automobil == "boje":
#         for boja in karakteristike:
#             print(f"boja automobila je: {boja}")

# kursevi = {"PPF" : {"naziv": "python fundamentals", "semestar": 1}, "OOP" : {"naziv" : "python object oriented", "semestar" : 1}}

# for (idkursa, detalji) in kursevi.items():
#     # print(idkursa, detalji)
#     for (k, v) in detalji.items():
#         print(k, v)

# def ispisi_poruke():
#     print("cao")
#     print("danasnji datum je 02.12")
#     print("predavanje pajton")

# ispisi_poruke()

# def pozdravna_poruka(ime):
#     print(f"hello, {ime}")

# pozdravna_poruka("sofija")
# pozdravna_poruka("Marija")

# def prikazi_informacije(ime="", poeni=0):
#     print(f"student {ime}, poeni {poeni}")

# prikazi_informacije("midad", 80)

# prikazi_informacije("midad")

# prikazi_informacije()

# def saberi(a=0, b=0):
#     print(a+b)
# #dole u fju mozemo definisati koji je koji clan
# saberi(b = 20, a = 10)

# def calculator(a, b, o):
#     if o == "+":
#         print(a+b)
#         return a+b
#     elif o == "-":
#         print(a-b)
#         return a-b
#     elif o == "*":
#         print(a*b)
#         return a*b
#     elif o == "/":
#         if b == 0:
#             print("nije dozvoljeno djeliti sa 0")
#         else:
#             print(a/b)
#             return a/b
#     else:
#         print("provjerite racunsku operaciju")

# calculator (int(input("unesite prvi broj")), int(input("unesite drugi broj")), input("unesite racunsku operaciju +, -, *, /"))

# kurs = "python"
# # print(kurs[0])
# # print(kurs[1])
# # print(kurs[3])

# for x in range(6):
#     print("na poziciji:", x, kurs[x])


# proizvodi  = ['telefon', 'tv', 'laptop']
# cena = [100, 200, 300]

# for i in range(len(proizvodi)):
#     print(proizvodi[i], cena[i])

# automobili = ["audi", "bmw", "yugo", "citroen", "kia" "peugeot"]

# for i in range(len(automobili)):
#     if i==3:
#         print('to je taj auto:', automobili[i])

proizvodi=[["iphone 11", "samsung s22", "XIAOMI x3"], ["mackbook", "acer", "del"], ["ipad", "samsung galaxy tab", "xiaomi tablet"]]

# telefoni = ["iphone 11", "samsung s22", "XIAOMI x3"]

# laptopovi = ["mackbook", "acer", "del"]

# tableti = ["ipad", "samsung galaxy tab", "xiaomi tablet"]

# print(proizvodi[0][0])
# print(proizvodi[1][1])

# proizvodi = [telefoni, laptopovi, tableti]

# for kategorija in proizvodi:
#     for stavka in kategorija:
#         print(stavka)

# for i in range(len(proizvodi)):
#     print(proizvodi[i])
#     for j in range(len(proizvodi[i])):
#         print(proizvodi[i][j])

    
