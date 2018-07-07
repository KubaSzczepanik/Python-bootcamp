


komunikat = 'podaj kolejną liczbę lub wpisz [koniec]:'
res = input(komunikat)

# najpierw obsłuż wyjątkowe sytuacje
if res =="koniec":
    exit('Nie podałeś żadnych liczb')

liczba = int (res)
min = liczba
max = liczba

while True:
    res = input (komunikat)
    if res == 'koniec':
        break # wychodzi z petli / wcięcia w odpowidnich miejscach są ważne

    liczba = int (res)
    if liczba > max:
        max = liczba
    if liczba < min:
        min = liczba

print(f' najwieksza z podanych liczb to {max}')
print ( f' najmniejsza z podanych licz to {min}')