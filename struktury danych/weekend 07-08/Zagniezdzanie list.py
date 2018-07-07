

# 1. listy w liscie

x = [[1,2,3], [4,5,6]]

a = [1,2,3]
b = [4,5,6]

x = [a,b]

print (x[0] [2])
# spodziewamy sie : 3

print(len(x))
# spodziewamy sie : 2

assert x[0][2] == 3
assert len(x) == 2  # to jest do testowanisa to assert

c = a
c = c.append(6)

assert a == [1, 2, 3, 6]

d = b.copy()

d.append(7)



assert d == [4, 5, 6, 7]

assert b == [4, 5, 6]



print(x)



# korzystamy z wbudowanej dla list metody copy - by utworzyć płytką kopię

# shallow copy obiektu x - płytka czyli jesli wewnątrz są jakieś referencje,

# to one nie sa kopiowna - nadal wskazuja na stary obiekt



y = x.copy()

print(y)



assert not x is y

assert y[0] == [1, 2, 3, 6]



y[0].append(7)

assert a == [1, 2, 3, 6, 7]

assert y == [[1, 2, 3, 6, 7], [4, 5, 6]]

assert x == [[1, 2, 3, 6, 7], [4, 5, 6]]



# Skorzystamy z deepcopy by kopiować rekurencyjnie - czyli także to co zagnieżdzone

# to się nazywa deepcopy, kopia głęboka

import copy



z = copy.deepcopy(x)

assert z == [[1, 2, 3, 6, 7], [4, 5, 6]]

assert not z is x



z[0].append(8)

assert z == [[1, 2, 3, 6, 7, 8], [4, 5, 6]]

assert x == [[1, 2, 3, 6, 7], [4, 5, 6]]


