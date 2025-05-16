import random

def stesti(n):
    pocitadlo = 0
    for i in range(n):
        cislo = random.randint(1, 6)
        if cislo == 6:
            pocitadlo += 1
    print(f'Pravdepodobnost vyhry pri {n} hodech: {pocitadlo / n}')

stesti(10)
stesti(100)
stesti(1000)
