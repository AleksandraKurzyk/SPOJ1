# Tworzymy zmienną która przechowa wynik dodawania
suma = 0

# Tworzymy pętle która wykona się tylko 3 razy
for n in range(3):
    # Dodajemy do naszej sumy liczbę wpisaną przez użytkownika
    suma = suma + int(input())
# Po zakończeniu pętli wypisujemy wynik
print(suma)