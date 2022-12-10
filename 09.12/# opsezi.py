# opsezi

x = 10   #globalna

def poruka():
    print("hello")
    print(x)
    a = 15 # lokalni opseg ne vidi se

def proba():
    global y
    y=15
    print(x)

poruka()
proba()
print(y)