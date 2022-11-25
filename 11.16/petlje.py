# pozicija_automobila = 0
# pozicija_cilja = 10

# pozicija_automobila += 2
# print(pozicija_automobila == pozicija_cilja)

# # pet puta ponovimo i dobili bi smo true

# for sledeci in ['marko', 'milos', 'marija', 'sofija', 'milorad']:
#     print('Hello', sledeci)

# print('prva sljedeca linija...')

# for broj in [1, 2, 3, 4, 5]:
#     print('ovo je broj:', broj)


# for broj in range(1, 10, 2):
#     print('stampanje broja:', broj)

# for broj in range(50):
#     print('stampanje broja:', broj)

# for broj in range(100, 0, -1):
#     print('stampanje broja:', broj)

# pozicija_automobila = 0
# pozicija_cilja = 10

# # for kretanje in range (5):
# #     pozicija_automobila += 2
# #     print(pozicija_automobila == pozicija_cilja)

# for trenutna_pozicija in range (pozicija_cilja + 1):
#     pozicija_automobila = trenutna_pozicija
#     print(pozicija_automobila == pozicija_cilja)

# start_date = 1941
# end_date = 1968

# for godina in range(start_date, end_date, 5):
#     print('svaka peta godina je: ', godina)

# for zvezda in range(100):
#     print('*', end="")

# print()

# print('1\t2\t3')
# print('*******************')
# zeljeni_broj = int(input('unesite zeljeni broj: '))
# for brojac in range(1, zeljeni_broj+1):
#     print(brojac*1, end='\t')
#     print(brojac*2, end='\t')
#     print(brojac*3)


# for x in range(5):
#     for y in range(3):
#         print('ovo je x:', x, 'ovo je y:', y)


# for x in range(6):
#     for y in range(6):
#         print('*', end= " ")
#     print()


for x in range(6):
    for y in range(6):
        if x == y:
            print('*', end= " ")
        else:
            print('#', end = " ")
    print()

# napisano ternarno
for x in range(6):
    for y in range(6):
        print('*' if x == y else '#')
    print()


x = 10
y = 5

for x in range(10):
    for y in range(5):
        if x == 0 or x == 9 or y == 0 or y == 9:
            print('#', end = " ")
        else:
            print(' ', end = ' ')


