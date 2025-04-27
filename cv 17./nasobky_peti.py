cisla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in cisla:
    if i * i < 5 * i:
        print(i * i, 'je mensi nez', 5 * i)
    elif i * i == 5 * i:
        print (i * i, 'je rovno', 5 * i)
    else:
        print(i * i, 'je vetsi nez', 5 * i)