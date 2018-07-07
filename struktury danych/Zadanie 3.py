lista = [1,-2,3,4,-5,0,6,-7,8]

dod =0
ujm= 0
zera=0

for el in lista:
    if el > 0:
        dod += 1
    elif el <0:
        ujm +=1
    else:
        zera +=1

print (f'dodatnich: {dod}, ujemnych')
