import random # biblioteka


gracz_x = random.randrange (1,11)
gracz_y = random.randrange (1,11)

skarb_x = random.randrange(1,11)
skarb_y = random.randrange(1,11)


print (f'debug: gracz {gracz_x}, {gracz_y}')
print(f'debug: skarb {skarb_x}, {skarb_y}')

krok = input('''
Szukasz skarbu na planszy 10x10
Podaj w którą stronę idziesz:
[l]ewo
[p]rawo
[g]ora
[d]ol
wyjdziesz poza planszę to zginiesz!
''')

print(krok)



while True:
    # continue przerywa biezacy obrot petli i wraca do naglowka while
    #break wychodzi całkowicie z pętli

    print(f' twoja pozycja to {gracz_x} , {gracz_y}')

    odl_przed = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    krok= input ()
    if krok =='l':
        gracz_x -=1
    if krok =='p':
        gracz_x +=1
    if krok == 'g':
        gracz_y -=1
    if krok == 'd':
        gracz_y +=1
    else:    # jesli co innego wpisze zle , to ignoruje
        continue


    zamglenie = random.randrange(1,6)
    if zamglenie > 1:



        odl_po = abs ( gracz_x - skarb_x) + abs( gracz_y - skarb_y)
        if  odl_przed > odl_po:
            print('ciepło')
        else:
            print ('zimno')
            odl_przed = odl_po


    if skarb_x == gracz_x and skarb_y == gracz_y:
        print( 'brawo! skarb jest twoj!')
        break

    if gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
        print ('jestes trupem')
        break

    if odl_przed > odl_po:
        print('ciepło')
    else:
        print('zimno')
    # w podstawowej wersji to koniec













