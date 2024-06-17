#Zmienna która śledzi ile razy powtórzyla się liczba 42
how_Many = 0

#Zmienna sprawdzająca czy poprzednia liczba nie była liczbą 42
diffrent = 0

while True:
    #Pobieramy liczbę od użytkownika
    digit = int(input())

    #Jeżeli liczba podaba przez użytkownika to 42 a poprzednia liczba była różna od 42 dodajemy 1 do ilości wystąpień liczby 42
    if(digit == 42 and diffrent == 1):
        how_Many +=1

    #Jeżeli liczba jest różna od 42 zmień zmienną "diffrent" na 1
    if(digit != 42):
        diffrent = 1

    # Jeżeli liczba jest równa 42 zmień zmienną "diffrent" na 0
    else:
        diffrent = 0

    #Wyświetl liczbę podaną przez użytkownika
    print(digit)

    #Jeżeli liczba 42 pojawiła się trzy razy zgodnie z założeniami zadania kończymy program
    if (how_Many == 3):
        break

