try:
    uchwyt_pliku = open('plik.txt', 'e')
except FileNotFoundError:
    print("Plik nie istnieje")
else:
    print(uchwyt_pliku.read())
