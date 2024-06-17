#Podajemy ile testów chcemy przeprowadzić
number_Of_digits = int(input())

#Pętla która uruchomi nam funkcję tyle raz ile testów chcemy przeprowadzić
for i in range(number_Of_digits):
    #Deklarujemy zmienną do przechowywania wyniku i ją zerujemy
    suma = 0
    #Wpisujemy ile liczb zostanie podanych
    how_many_digits = input()
    #Pobieramy od użytkownika linię zawierającą X liczb i "pozbywamy" się spacji - wrzucamy same liczby do listy
    list_Of_Digits = input().split()

    #Przechodzimy przez listę i dodajemy każdą liczbę w niej zawertą do naszej sumy
    for n in list_Of_Digits:
        suma += int(n)

    #Wyświetlamy wynik dodawania
    print(suma)
