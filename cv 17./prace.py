pocet_hodin = int(input("Zadejte počet hodin: ")) 

if pocet_hodin < 10:
    print('Vydelas si', pocet_hodin * 80,'kc')
else:
    print('Vydelas si', pocet_hodin * 100,'kc')