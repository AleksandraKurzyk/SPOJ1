#Podajemy ile liczb chcemy sprawdzić
number_Of_digits = int(input())


#Pętla która uruchomi nam funkcję tyle raz ile liczb chcemy sprawdzić
for i in range(number_Of_digits):

    #Pobieramy od użytkownika linię która zawiera dwie liczby rozdzielone spacją, której się pozbywamy
    input_uzytkownika = input().split()

    #Interesuje nas tylko liczba jedności z podstawy
    podstawa = int(input_uzytkownika[0]) % 10
    wykladnik = int(input_uzytkownika[1])

    #Liczba podnieśiona do 0 potęgi = 1 dlatego musimy to sprawdzić
    if(wykladnik > 0):
        #Dowolna liczba podniesiona do potęgi ma w pewnym momencie (maksymalnie przy 4 potędze) powtarzające się liczby jedności
        # 2 4 8 1_6 3_2 6_4 12_8 jak widzimy nie musimy mnożyć prez cały nasz wykładnik który maksymalnie może wynosić 1 000 000 000

         #Sprawdzamy czy liczba jest podzielna przez 4 jeżeli tak ustawiamy najgorszy wariant i musimy liczbę mnożyć cztery razy
        if (wykladnik % 4 == 0):
            wykladnik = 4
        else:
            #W innym wypadku patrzymy ile reszta z dzieleni w celu określenia ile razy musimy pomnożyć liczbę
            wykladnik = wykladnik % 4

        #Potęgujemy naszą podstawę przez nasz wykładnik na samym końcu wyciągamy liczbę jedności obliczając resztę z dzielenia przez 10
        # '**' operator potęgi
        print((podstawa ** wykladnik)%10)
    else:
        print(1)

