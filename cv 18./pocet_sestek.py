import random

count_six = 0
count_other = 0

for i in range(10):
    roll = random.randint(1, 6)
    print(roll)  
    if roll == 6:
        count_six += 1
    else:
        count_other += 1

print(f"\nŠestka padla {count_six}x, jiné číslo padlo {count_other}x.")