# #kljuc : vrednost, 

# osoba_recnik = {"ime": "Sofija", "godine": 25, "plava": True}
# print(osoba_recnik)
# print(osoba_recnik["ime"])


# for i in osoba_recnik:
#     print(osoba_recnik[i])

# for (kljuc, vrednost) in osoba_recnik.items():
#     print("ovo je kljuc:", kljuc)
#     print("ovo je vrednost:" , vrednost)

# osoba2 = {}

# osoba2["ime"] = "Marija"

# print(osoba2)

# osoba2["ime"] = "Sofija"
# print(osoba2)

# del osoba2["ime"]

# print(osoba2)


# poruke = {"en": "hello", "sr" = "zdravo", "de": "hallo"}

# jezik = input("unesite jezik:")

# if jezik == "en" or jezik == "sr" or jezik == "de":
#     print(poruke[jezik])
# else:
#     print("nemamo ovaj prevod")

# poruke = {"en": "hello", "sr": "zdravo", "de": "hallo"}

# for (jezik, prevod) in poruke.items():
#     if jezik == "en":
#         print(f"ENGLESKI: {prevod}")
#     elif jezik == "de":
#         print(f"Njemacki: {prevod}")
#     else:
#         print(f"srpski: {prevod}")


# selekcija = {"drzava": "Srbija", "broj_pobeda": 0, "boje_dresova": ["crvena", "bela"], "brojevi_igraca": [9, 5, 12, 25]}




# for (kljuc, vrednost) in selekcija.items():
#     print("kljuc:", kljuc)
#     print("vrednost:", vrednost)
#     if kljuc == "boje_dresova":
#         for boja in vrednost:
#             print("boja je:", boja)
#     elif kljuc == "brojevi_igraca":
#         for broj in vrednost:
#             print(f"igrac broj, {broj}")
#     else:
#         print(f"{kljuc}:{vrednost}")    

automobil = {"marka": "citroen", "model": "c3", "boje": ["crvena", "bela", "crna"], "alu_felne": False, "godiste": 2017, "kubikaza": 1.6}

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


# automobili = {"BG-123": { "marka": "citroen", "model": "c3", "kubikaza": 1.6, "boje": ["crvena", "bela", "crna"]},"BG-451": {"marka": "opel", "model":"astra","kubikaza": 2.0,"boje": ["plava", "zelena"]}},

# for (reg, detalji) in automobili.items():
#     for(kljuc, vrednost) in detalji.items():
#         print(f"{kljuc} : {vrednost}")
# print("***********************************")


# SETOVI: PODACI SE NE MOGU PONAVLJATI ALI REDOSLJED NIJE BITAN:

# boje_u_ponudi = {"bela", "plava", "crvena"}
# print(boje_u_ponudi)

# boje_u_ponudi.add("zuta")
# boje_u_ponudi.remove("bela")

# print(boje_u_ponudi)

# for boja in boje_u_ponudi:
#     print(boja)



 






    




