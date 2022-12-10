# tekst1 = "3,9,13,4,42"
# tekst2 = tekst1.split(',')
# # print(tekst2)



# for i in range(0, len(tekst2)):
#     tekst2[i] = int(tekst2[i])
    
# print(f"pretvoreni string u intiger lista: {tekst2}")

# l = [3, 9, 13, 4, 42]

# for i in l:
#     print(i**2,end=",")

# l2 = [9, 81, 169, 16, 1764]

# for y in range(0, len(l2)):
#     l2[y] = str(l2[y])

# print(f"kvadrirani elementi liste pretvoreni u string: {l2}")

# l3 = ['9', '81', '169', '16', '1764']



tekst1 = "3,9,13,4,42"
lista1 = tekst1.split(",")
print(f"Razdvojeni elementi split metodom po parametru ',' {lista1}")


lista2 = [str(int(x)**2) for x in lista1]
print(f"String lista kvadriranih elemenata glasi: {lista2}")

lista3 = ",".join(lista2)
print(f"Spojeni kvadrirani elementi u jedan string, {lista3}")




