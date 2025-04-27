import random

bonus = 0
previousRoll = None


for i in range (10):
    roll = random.randint(1, 6)
    print(roll)
    if roll == previousRoll:
        bonus += 1
        print('PREMIE')
    previousRoll = roll

print(f'celkovy pocet premii je {bonus}')

# Skoncil jsem na cv 7 lekce 18


