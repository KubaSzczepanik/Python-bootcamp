



x = int(input('Podaj pozycje gracza x'))
y = int(input('Podaj pozycje gracza y'))

if x < 10:
    if y < 10:
        print ('lewy górny róg')
    elif y > 90:
        print ("lewy dolny róg")
    else:
        print ('lewa krawędź')
elif x >90:
    if y < 10:
        print ('prawy górny róg')
    elif y > 90:
        print('prawy dolny róg')
    else:
        print ("prawa krawędź")
else:
    if y < 10:
        print ('górna krawędź')
    elif y >90:
        print ('dolna krawędź')
    else:
        print('środek')

# sposób drugi (po amgielksu , żeby nie było problemów z odmianą
if  x < 10:
    pos_x = 'left'
elif x > 90:
    pos_x = 'right'
else:
    pos_x = ''

if  y < 10:
    pos_y = 'top'
elif y > 90:
    pos_y = 'bottom'
else:
    pos_y = ''
  # oba wypełnione
if pos_x and pos_y:  # jeśli w poz. x jest cos i w poz y jest cos, to jestesmy w rogu.
    print (pos_x, pos_y,'corner' )
# tylko jeden z nich wypełniony
elif pos_x or pos_y:
    print(pos_x, pos_y, "edge")
# oba puste
else:
    print ('center')