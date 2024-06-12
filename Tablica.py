# Przyjmujemy od użytkownika linię tekstu i tworzymy z niego listę stringów
input_uzytkownika = input().split()

# Zamieniamy listę stringów na listę integerów poprzez pętle na każdym elemencie tablicy i zamianę go w int'a
liczby = [int(n) for n in input_uzytkownika]

# Odwracamy kolejność listy
liczby.reverse()

# Wyświetlamy każdy element listy łączac je spacjami
for n in liczby:
    print(n, end=" ")