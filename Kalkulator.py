#Kod jest otoczony w blok try-except, który służy do przechwytywania i obsługi wyjątków (błędów), które mogą wystąpić podczas wykonywania.
try:
    while True:
        # Pobieramy od użytkownika linię która zawiera dwie liczby oraz znak określający operacje matematyczną rozdzielone spacją - usuwamy od razu spacje
        input_uztkownika = input().split()

        #Jako że znak operacji matematycznej jest podawany jako pierwszy wyszukujemy go na zerowym indeksie listy
        #Po wykryciu odpowiedniej operacji matematycznej wykonujemy ją na 1 i 2 liczbie podanej przez użytkownika
        if input_uztkownika[0] == "+":
            print(int(input_uztkownika[1]) + int(input_uztkownika[2]))
        elif input_uztkownika[0] == "-":
            print(int(input_uztkownika[1]) - int(input_uztkownika[2]))
        elif input_uztkownika[0] == "*":
            print(int(input_uztkownika[1]) * int(input_uztkownika[2]))
        elif input_uztkownika[0] == "/":
            #W tym przypadku dodatkowo konwertujemy wynik do inta w celu odcięcia liczby po przecinku
            print(int(int(input_uztkownika[1]) / int(input_uztkownika[2])))
        else:
            print(int(input_uztkownika[1]) % int(input_uztkownika[2]))

#W przypadku nie podania przez użytkownika żadnego znaku podnoszony jest bład
except EOFError:
    pass
