
zestaw = []

liczba = input('podaj liczbe:')
while liczba != '' and len(zestaw) <10:
    zestaw.append (int(liczba))
    liczba = input('podaj liczbę: ')

print (f'średnia to {sum (zestaw) / len }')

