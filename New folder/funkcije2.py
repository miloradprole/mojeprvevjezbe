# def digitron(broj1, broj2, operacija):
#     if operacija == "+":
#         print(broj1 + broj2)
#         return broj1 + broj2
#     elif operacija == "-":
#         print(broj1 - broj2)
#         return broj1 - broj2
#     elif operacija == "*":
#         print(broj1 * broj2)
#         return broj1 * broj2
#     elif operacija == "/":
#         print(broj1 / broj2)
#         return broj1 / broj2
#     else:
#         print("odaberite operaciju")

# rezultat = digitron (10, 10, "+")
# print(rezultat)
# rezultat_oduzimanja = digitron(10, 5, "-")
# print(rezultat_oduzimanja)


# ime = input("unesite ime:")
# prezime = input("unesite prezime:")
# godina = input("unesite godinu 21, 22, 23:")
# korisnicko_ime = ""

# def kreiraj_kor_ime(ime, prezime, godina):
#     kor_ime = f"ita.{godina},{ime.lower()},{prezime.lower()}"
#     return kor_ime

# korisnicko_ime = kreiraj_kor_ime(ime, prezime, godina)

# print("prikupljeni podaci o korisniku")
# print(ime, prezime, godina)




# def menjacnica(euro):
#     dinari = euro * 117
#     return dinari

# dobijeni_dinari = menjacnica(int(input("unesite vrednost u eurima:  ")))
# print("rezultat: ", dobijeni_dinari)


# def registracija(licna_karta, cist_auto, saobracajna):
#     if cist_auto == False or licna_karta == False or saobracajna == False:
#         return "neuspesno dodjite opet"
#     else:
#         return "uspesno"

# print(registracija(True, True, False))

# moj licni primjer:
# def bankomat(stanje, iznos):
#     if stanje >= iznos:
#         return stanje - iznos

# podizanje = bankomat(500, 100)
# print(f"novo stanje je: {podizanje}")


# primjer profesorice sa predavanja:

# def bankomat(stanje, zeljeni_iznos):
#     if stanje >= zeljeni_iznos:
#         return f"uspesno, novo stanje je {stanje - zeljeni_iznos}"
#     else:
#         "neuspesno"

# rezultat = bankomat(500, 100)
# print(rezultat)
# print(bankomat(500, 100))


#primjer kada ne znamo koliko cemo imati ulaznih parametara (proizvoljan broj parametara jedna zvjezdica je za tuple, dvije za rjecnik):

# def registracija(*dokumenti):
#     print("doneli ste dokumenta:")
#     print(dokumenti)
#     print(dokumenti[0])
#     print(type(dokumenti))

# registracija("vozacka dozvola", "obavio tehnicki pregled", "licna karta")


# def upis(**podaci):
#     print("uneli ste podatke")
#     print(podaci)
#     print(podaci["ime"])

# upis(ime="milorad", prezime="prole", ustanova="ita")


#funkcija u funkciji:

# def skolovanje(predavac_predaje):
#     print("skolska godina je u toku")
#     print("ucionica a22")
#     predavac_predaje()

# def predavac_vm():
#     print("uvod u mreze")
#     print("dansa radimo novu temu")
#     print("dali ste igrali lol")

# def predavac_al():
#     print("opet imamo predavanje sredom")
#     print("radimo funkcije")

# def predavac_vn():
#     print("krecemo sa html i css")

# skolovanje(predavac_vm)    


# def priprema_obroka(spremanje):
#     print("dolazak u kuhinju")
#     print("perem ruke")
#     spremanje()

# def dorucak():
#     print("idem po burek")
#     print("to je to od kuvanja")

# def rucak():
#     print("pohovanje")
#     print("restovani krompir")

# def vecera():
#     print("tunjevina salata")
#     print("sladoled")

# priprema_obroka(vecera)


#lambda funkcija:

# res = lambda a, b: a+b
# res(5, 10)

#rekurzivna funkcija poziva samu sebe:

# def tajmer(sekunde):
#     print(sekunde)
#     sekunde -= 1
#     if sekunde > 0:
#         tajmer(sekunde)

# tajmer(10)

# dekoratori njima mjenjamo ponasanje fje:

# def provera(funkcija):
#     def unutrasnja_funkcija(a, b):
#         if b == 0:
#             print("nije dozvoljeno deljenje sa nulom")
#             return
#         funkcija(a, b)
#     return unutrasnja_funkcija


# manki provera
# def deljenje (a, b):
#     print(a/b)

# deljenje(10, 0)


#generatori:

def brojevi():
    yield 1
    yield 2
    yield 3

dobijeni_broj = brojevi()
print(dobijeni_broj)
print(next(dobijeni_broj))
print(next(dobijeni_broj))
print(next(dobijeni_broj))

for broj in brojevi():
    print(broj)