
#napisz program oblicz. srednia wartosc temp w danym tygodniu na podst temp wprowadzonych przez uzytk.


ile_dni = 7
nr_dnia =1 # pierwsza wartosc z jaka chce wejsc do petli / ustawienbie zmiennej sterujacej
suma_temp = 0 # suma od ktorej zaczynam zbierac temp
while nr_dnia <= 7:

    temp = int(input('podaj temperature dnia {nr_dnia}:'))
    suma_temp = temp + suma_temp
    nr_dnia = nr_dnia + 1

srednia_temp = suma_temp / ile_dni
print (f' średnia temp w tym tygodniu wyniosla {nr_dnia}:')




