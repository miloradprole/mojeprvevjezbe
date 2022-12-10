

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

def calculator(a, b, o):
    if o == "+":
        print(a+b)
        return a+b
    elif o == "-":
        print(a-b)
        return a-b
    elif o == "*":
        print(a*b)
        return a*b
    elif o == "/":
        if b == 0:
            print("nije dozvoljeno djeliti sa 0")
        else:
            print(a/b)
            return a/b
    else:
        print("provjerite racunsku operaciju")

calculator (26, 33, '*')

