# #dekoratori, iteratori i generatori:

# def first_function():
#     print('first_function')
# def second_function():
#     print('second function')
# first_function()
# second_function()



# def change_to_second_function(func): 
#     return second_function 
 
# def first_function(): 
#     print('first_function') 
 
# def second_function(): 
#     print('second function') 
 
# first_function = change_to_second_function(first_function)
# first_function()


# def second_function():
#     print('second function')
 
# def change_to_second_function(func):
#     return second_function
 
# @change_to_second_function
# def first_function():
#     print('first_function')
 
# first_function()


# def all_caps(s):
#     return s.upper()
# print(all_caps('new york'))

# def decorator(func): 
#     # Lokalna (ugnežđena) funkcija 
#     def inner_function(l): 
#        return [func(el) for el in l] 
#     return inner_function 
  
# @decorator
# def all_caps(s): 
#     return s.upper() 
  
# cities= ['london', 'moscow', 'new york'] 
# print(all_caps(cities))



# Imamo osnovnu funkciju operations(a,b) koja prima dva argumenta i ispisuje njihove vrednosti. Potrebno je ovu funkciju dekorisati sa dve funkcije: addition, u kojoj ćemo sabrati ova dva broja, i subtraction, u kojoj ćemo oduzeti ova dva broja. Izgled funkcije operations(a,b) je:


# def operations(a,b):
#       print("Passed numbers are: {} i {}".format(a,b))


# def addition(func):
#     def wrapper_function(a,b):
#         print("Subtraction result is {}".format(a+b))
#         return func(a,b)

#     return wrapper_function



# def subtraction(func): 
#     def wrapper_function(a,b): 
#         print("Subtraction result is {}".format(a-b)) 
#         return func(a,b) 

#     return wrapper_function 



# @addition 
# @subtraction 
# def operations(a,b): 
#     print("Passed numbers are: {} i {}".format(a,b)) 



# operations(9, 15)


#ITERATORI:

# cities = ["new york", "london", "moscow"]
# cities_iterator = iter(cities)
# print(next(cities_iterator))
# print(next(cities_iterator))
# print(next(cities_iterator))
# print(next(cities_iterator))

# brojevi = [2, 6, 7, 33, 895, 74]
# iterabilni_brojevi = iter(brojevi)
# print(next(iterabilni_brojevi))
# print(next(iterabilni_brojevi))
# print(next(iterabilni_brojevi))
# print(next(iterabilni_brojevi))
# print(next(iterabilni_brojevi))
# print(next(iterabilni_brojevi))
# print(next(iterabilni_brojevi))


#iter i next kod while petlje:

# cities = ["new york", "london", "moscow"] 
# cities_iterator = iter(cities) 
  
# while cities_iterator: 
#     try: 
#         print(next(cities_iterator)) 
  
#     except StopIteration: 
#         break

# GENERATORI:

# def even_numbers(a):
#     for x in range(a):
#         if x % 2==0:
#             yield x
# for e in even_numbers(10):
#     print(e,end=', ')

# def func():
#     i = 10
#     while i > 0:
#         yield i
#         i -= 1
# for i in func(): print(i, end=' ')


# Napisati generatorsku funkciju koja ispisuje sve elemente deljive sa 3 od 1 do 50.

def div(a):
    for x in range(a):
        if x % 3==0:
            yield x

for e in div(50):
    print(e,end=', ')