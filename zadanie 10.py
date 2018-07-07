liczba1 = int(input("podaj pierwsza liczbe"))
liczba2 = int(input("podaj druga liczbe"))
znak = input (" podaj znak")
if znak == '-':
    print ( liczba1 - liczba2)
elif znak =='+':
    print ( liczba1 + liczba2)
elif znak == '*':
    print ( liczba1 * liczba2)
elif znak =='/':
    if liczba2 == 0:
        print('nie wolno dzielic przez 0')
        exit(1)

    print( liczba1 / liczba2)

else:
    exit('nieznana operacja')




