import random

cislo = random.randint(1, 5)
print('Myslím si číslo od 1 do 5. Hádej!')

def zkus():
    while True:
        try:
            tip = int(input('Zadej číslo: '))
            if tip < 1 or tip > 5:
                print('Zadej číslo v rozsahu 1 až 5.')
                continue
            if tip == cislo:
                print(f'Uhádl jsi to správně! Myslel jsem si {cislo}.')
                break
            else:
                print('Špatně, hádej dál.')
        except ValueError:
            print('Zadej prosím platné číslo.')

zkus()