# pozicija_automobila = 10
# cilj = 100
# gorivo = 120
# while pozicija_automobila < cilj:
#     print('do cilja imate: ', cilj - pozicija_automobila)
#     pozicija_automobila += 10
#     gorivo -= 5
#     if gorivo < 40:
#             break
            
# print('dopunite gorivo')

# for i in ['marko', 'milos', 'marija', 'sofija', 'milorad']:
#     print('Hello', i)

# for broj in [1, 2, 3, 4, 5]:
#     print('ovo je broj:', broj)

# for broj in range(10, 1, -1):
#     print('stampanje broja:', broj)

# for broj in range(15):
#     print('stampanje broja:', broj)

# pozicija_automobila = 0
# pozicija_cilja = 10

# # for kretanje in range(5):
# #     pozicija_automobila += 2
# #     print(pozicija_automobila == pozicija_cilja)

# for trenutna_pozicija in range(pozicija_cilja + 1):
#     pozicija_automobila = trenutna_pozicija
#     print(pozicija_automobila == pozicija_cilja)


# start_date = 1941
# end_date = 2000

# for godina in range(start_date, end_date, 5):
#     print('svaka peta godina je: ', godina)

# for zvezda in range(15):
#     print('*', end="")

# print()

# print('1    2    3')
# print('*******************')
# zeljeni_broj = int(input('unesite zeljeni broj: '))
# for brojac in range(1, zeljeni_broj+5):
#     print(brojac*1, end='\t')
#     print(brojac*2, end='\t')
#     print(brojac*3)

# for x in range(5):
#     for y in range(3):
#         print('ovo je x:', x, 'ovo je y:', y)

for x in range(6):
    for y in range(6):
        if (x==0 and y==5) or (x==1 and y==4) or (x==2 and y==3) or (x==3 and y==2) or (x==4 and y==1) or (x==5 and y==0):
            print('*', end= " ")
        else:
            print('#', end = " ")
    print()

# a = 5
# b = 7
# zbir = a+b
# razlika = a-b
# print('broj je:', a+b)
# print('razlika je: {1} zbir je: {0}'.format(zbir, razlika))

# for x in range(6):
#     for y in range(6):
#         print('*' if x == y else '#')
#     print()


