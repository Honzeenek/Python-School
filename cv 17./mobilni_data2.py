spotreba = int(input('Kolik jste spotrebovali dat?'))

if spotreba <= 10:
    cena = spotreba * 1
else:
    cena = 10 + (spotreba - 10) * 3

print(f'Za {spotreba} MB zaplatite {cena} Kc')
