#Podajemy ile liczb chcemy sprawdzić
number_Of_digits = int(input())

#Funkcja do sprawdzania czy podana liczba jest pierwsza
def czy_pierwsza(digit_to_check):
    #Liczby 1 lub mniejsze nie są pierwszymi - nie ma sensu ich sprawdzać
    if digit_to_check <= 1:
        return "NIE"
    #Sprawdzamy podzielność liczby od 2 do połowy podanej przez użytkownika liczby, +1 dlatego że range(4) to max 3 itd
    for x in range(2, int(digit_to_check/2)+1):
        if digit_to_check % x == 0:
            return "NIE"
    #Jeżeli liczba nie była podzielna przez liczby z range() jest pierwszą
    return "TAK"

#Pętla która uruchomi nam funkcję tyle raz ile liczb chcemy sprawdzić
for i in range(number_Of_digits):
    #Uruchamiamy funkację "czy_pierwsza" z zmienną podaną przez użytkownika, na koniec wyświetlamy wynik
    print(czy_pierwsza(int(input())))