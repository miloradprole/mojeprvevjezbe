# f = lambda x, y: x * y  # lambda funkcija
# a=f(55,12)
# print(a)

# # map funkcija:
# x = [1,2,3,4]
# y = [2,4,6,8]
# z = [-1,-2,-3]
# print(list(map(lambda a,b,c:a+b+c, x,y,z)))

# #filter funkcija:

# def filter_func(x): 
#     if x % 2: 
#         return True 

#     else: 
#         return False



# numbers= list(range(0,10)) 

# print(list(filter(filter_func, numbers))) 

# print(list(filter(lambda x: x % 2, numbers)))


# # Vežba

# # Napisati lambda funkciju koja prima argument x i vraća njegov kvadrat i rezultat ispisati na ekranu.

# # Rešenje

# x = 5
 
# result = lambda n: n**2
# print(result(x))

# # Sortiranje funkcija:

# s = "String"
# print(sorted(s, key=lambda x: x))


#Vežba

#Koristeći lambda funkciju, datu listu čiji su uređeni parovi n-torke ('city_name', postal_code) sortirati po poštanskom broju; rezultat smestiti u listu i ispisati na ekranu.


# cities =[("New York",10001),
#        ("Paris",75000), 
#        ("Moscow", 101000),
#        ("Tokyo",100000)]

# cities =[("New York",10001), 
 
#        ("Paris",75000),  
 
#        ("Moscow", 101000), 
 
#        ("Tokyo",100000)] 
 
# cities = sorted(cities, key=lambda x: x[1]) 
# print(cities)

result = lambda: 5