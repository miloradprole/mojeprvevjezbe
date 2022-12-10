tekst1 = "3,9,13,4,42"
lista1 = tekst1.split(",")
print(f"Razdvojeni elementi split metodom po parametru ',' {lista1}")

lista2 = [str(int(x)**2) for x in lista1]
print(f"String lista kvadriranih elemenata glasi: {lista2}")

lista3 = ",".join(lista2)
print(f"Spojeni kvadrirani elementi u jedan string, {lista3}")

