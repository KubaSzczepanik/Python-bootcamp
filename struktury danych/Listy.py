# lista to struktura podobna do krotki, ale moge ją modyfikować

lista= [1,2,3,4,5,6,7]

print(len(lista))
print(lista[0])
print(lista[-1])
print(lista[::2])  #od poczatku co konca co dwa miejsca

lista.append ('ala')  # dodaje na koniec
print(lista)

lista.insert(3,'kot')
print (lista)

lista.insert(100, 'tu byłem Tony Halik')
print(lista)

# pierwszy ujemny znak jest przedostatnim

print(lista.count(1))  # zwraca ile razy na mojej liscie wystepuje 1

lista[3] = 'tu był element czwarty'
print(lista)

lista[3:7] = []
print(lista)
