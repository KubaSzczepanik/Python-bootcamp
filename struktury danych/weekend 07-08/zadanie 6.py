# TODO: używać ctr+alt+L - w celu zachowania zgodności z PEP-8

liczby = [1, 2, 3, 4, 5, 6]

print(liczby)

indeks_min = None  # w sumie lepiej pisac none
indeks_max = None

for index in range(len(liczby)):
    if index == 0:
        indeks_max = index
        indeks_min = index
    else:
        if liczby[index] > liczby[indeks_max]:
            indeks_max = index
        if liczby[index] < liczby[indeks_min]:
            indeks_min = index

print(indeks_min, indeks_max)

# nie stopsujemy nazw zmiennych takich jak słowa kluczowe w pythonie
# warto poszukać słow kluczowych w pythonie
# hint: w pycharmie może sie podswietlic na niebiesko
# TODO : poczytac

min = liczby[indeks_min]
max = liczby[indeks_max]

liczby[indeks_max] = min
liczby[indeks_min] = max

print(liczby)

