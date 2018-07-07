
# .Tupla. lub .krotka. to struktura, ktora przechowuje wiecej niz 1 wartosc na raz


zmienna = (1,2,3,4)
print(zmienna)

a = ('ala', 'ma', 'kota')
b = ('ala', 'ma', 3.5 ,'koty', 5,6,7,8)

print (a,b)

print(len(a)) # ile masz elementów (od lengh)
print(a[1])  # najpierw nazwa zmiennej, potem jest element zmiennej w []

i=0
while a <= len(b):
    print (b[i])


print(b[1:3]) #
print(b[1:]) # od granicy 1 do końca
print(b[1:3])
print(b[1:6:2])
print(b[::2]) # wyswietl od poczatku do konca co dwie pozycje
print(b[:-1]) # wez wszyst
print(b[1:-1]) #  podaj od poczatku do konca bez krancow


