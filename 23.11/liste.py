osoba = ['sofija', 25, 'plava', False]

for x in range(len(osoba)):
    print(osoba[x])

for osobina in osoba:
    print(osobina)


voce_i_povrce = ['jabuka', 'beli luk', 'crni luk', 'banana', 'mandarina', 'lubenica', 'krastavac']

for stavka in voce_i_povrce:
    print(stavka)

for i in range(len(voce_i_povrce)):
    print('na indeksu i ', i, 'nalazi se', voce_i_povrce[i])

for indeks, vrednost in enumerate(voce_i_povrce):
    print('indeks', indeks, 'stavka', vrednost)

    #tri varijante iteracije kroz listu


    automobili = ['citroen', 'bmw', 'opel', 'kia', 'yugo']

    for pozicija, auto in enumerate(automobili):
        if pozicija == 1:
            print('kupujem')
            break
        print('pozicija:', pozicija, 'auto', auto)


for pozicija, auto in enumerate(automobili):
        if len(auto) == 3:
            print(auto)

automobili.append("mercedes")
automobili[2] = "opel corsa"
print(automobili)
automobili[3] = 'kia sportage'
print(automobili)

del automobili[3]
print(automobili)

automobili.remove('bmw')
print(automobili)
automobili.pop(0)
print(automobili)

automobili.clear()
print(automobili)
print(len(automobili))


automobili = ['citroen', 'bmw', 'opel', 'kia', 'yugo', 'peugeot', 'audi']

automobili_akcija = []

for i in range(len(automobili)):
    if i==1 or i==2 or i==3:
        automobili_akcija.append(automobili[i])

print(automobili_akcija)

automobili_akcija = automobili[1:4]
print(automobili_akcija)

broj = [2, 5, 6, 9, 18, 22, 45, 69, 113]
parni = []
neparni = []

for cifra in broj:
    if cifra % 2 == 0:
        parni.append(cifra)
    else:
        neparni.append(cifra)

print(parni, neparni)

#ternarno napisano


broj = [2, 5, 6, 9, 18, 22, 45, 69, 113]
parni = []
neparni = []

for cifra in broj:
    parni.append(cifra) if cifra % 2 == 0 else neparni.append(cifra)
        

print(parni, neparni)
