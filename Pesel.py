# Wprowadzamy ile peseli pacjentow chcemy podać
number_Of_IDs = int(input())

# Tworzymy pętle która umożliwi nam podanie odpowiedniej ilości peseli oraz przejście i obliczenienie każdego z nich czy jest prawidłowy
while number_Of_IDs > 0:

    # Pobieramy od użytkownika pesel dla każdego podanego pacjenta
    id = input()

    # Tworzymy listę która umożliwi nam podzielenie peselu na pojedyncze cyfry
    list = []

    # Iterujemy pesel cyfra po cyfrze i zapisujemy każdą cyfrę do listy na odzielnym indeksie, konwertujemy od razu do int'a w celu dodania
    for n in id:
        list.append(int(n))

    # Wykonujemy obliczenia na cyfrach z peselu przypisanych do indeksów zgodnie z zadaniem
    id_sum = list[0] * 1 + list[1] * 3 + list[2] * 7 + list[3] * 9 + list[4] * 1 + list[5] * 3 + list[6] * 7 + list[
        7] * 9 + list[8] * 1 + list[9] * 3 + list[10] * 1

    # Sprawdzamy czy suma dodanych liczb jest większa od zera jeżeli nie pesel nie jest prawdziwy
    if (id_sum > 0):
        # Jeżeli suma jest większa od zera sprawdzamy czy ostatnia cyfra z sumy jest równa 0 poprzeez wyznaczenie reszty z dzielenie przez 10
        if (id_sum % 10 == 0):
            print("D")
        # Jeżeli reszta z dzielenie jest różna od zera pesel jest nieprawdziwy
        else:
            print("N")
    else:
        print("N")
    # Odejmujemy liczbę jako że jeden pesel już sprawdziliśmy
    number_Of_IDs -= 1