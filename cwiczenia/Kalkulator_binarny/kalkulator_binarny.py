print("Kalkulator binarny\n")
print("Autor: Marcin Brzeziński")
a = ""
b = ""
dzialanie = ""
while a != 1 and a != 0:
    a = input("Podaj pierwszą liczbę binarną! (0 lub 1)")
    if a.isdigit():
        a = int(a)
        if a != 1 and a != 0:
            print("Błąd XX002. To nie jest wartość binarna.")
    else:
        print("Błąd XX001. To nie jest wartość binarna.")
while b != 1 and b != 0:
    b = input("Podaj drugą liczbę binarną! (0 lub 1)")
    if b.isdigit():
        b = int(b)
        if b != 1 and b != 0:
            print("Błąd XX002. To nie jest wartość binarna.")
    else:
        print("Błąd XX001. To nie jest wartość binarna.")
while dzialanie != 1 and dzialanie != 2 and dzialanie != 3:
    dzialanie = input("Wybierz operację logiczną do wykonania:\n 1 = AND\n 2 = OR\n 3 = XOR\n")
    if dzialanie == "1":
        print(a and b)
    elif dzialanie == "2":
        print(a or b)
    elif dzialanie == "3":
        print(a ^ b)
    break
