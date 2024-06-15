#Tworzymy nieskończoną pętle która będzie się wykonywać do pojawienia się jakiegoś błędu np. brak podania danych
while True:
    # Kod jest otoczony w blok try-except, który służy do przechwytywania i obsługi wyjątków (błędów), które mogą wystąpić podczas wykonywania.
    try:
        #Pobieramy od użytkownika wyraz który mamy obrócić
        word = input()
        #Wyświetlamy listę od końca do początku - pierwsze dwa parametry obecne w word[::-1] reprezentują początek i koniec listy
        print(word[::-1])
    except:
        break