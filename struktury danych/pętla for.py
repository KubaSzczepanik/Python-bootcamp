lista = [1,2,3,4,5,6,7,8]

for element in lista:    # dla kazdego elementu na liscie.../ to bedzei najczestsza metoda
    print(element)

tupla = ('ala', 'ma', 3, 'koty', 'które', 'ją', 'nienawidzą')

for element in tupla:
    print(element)


    # enumerate - bierze z listy i zwraca element i mowi ktory to element z kolei

for nr, element in enumerate(tupla):
    print (nr, element)

print('====== range(10) =======')  # to jest przerywnik
for i in range(10):
    print(1)

print('========range(len(tupla) ==========')
for i in range( len (tupla)):
    print(i,tupla[i])


print('========range(1,len(tupla),2) ==========')
for i in range (1,len(tupla),2):
    print(i, tupla[i])


