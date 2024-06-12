# Deklaracja zmiennej która będzie przychowywać wynik naszego dodawania
suma = 0

# Kod jest otoczony w blok try-except, który służy do przechwytywania i obsługi wyjątków (błędów), które mogą wystąpić podczas wykonywania.
try:
    # Toworzymy nieskończoną pętle która umożliwi nam dodawanie w nieskończoność liczb do obliczania sumy
    while True:
        # Przypisujemy do zmiennej 'suma' jej starą wartość + wartość wpisaną przez użytkownika
        suma = suma + int(input())
        # Wyświetlamy zmienną suma
        print(suma)
# W przypadku nie podania przez użytkownika żadnego znaku podnoszony jest bład
except EOFError:
    pass