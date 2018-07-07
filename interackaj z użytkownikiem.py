#
#
# imie = input ('wpisz swoje imie: ')
#
# print( 'witaj', imie)
#
# wiek = int (input ('ile masz lat?'))
#
# print(' za dawa lata bedziesz miał(a):, wiek +2')
#
# # operatory porównania< > <= >= == !=   takie znaki mozna
# if wiek >= 18:
#     print('zapraszam na piwo!')
# else:
#     print('zapraszamy na cole')

miasto_A = input ('podaj nazwe miasta poczatkowego')
miasto_B = input ('podaj nazwe miasta koncowego')
dystans = float( input ("podaj dystans"))
cena_paliwa = float (input ("podaj cene paliwa"))
spalanie = float (input (' ile spalasz paliwa na 100km?'))

print (f' koszt przejazdu {miasto_A}-{miasto_B} wynosi {round(dystans * cena_paliwa * spalanie/100)}PLN')




