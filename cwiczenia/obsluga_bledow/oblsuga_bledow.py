try:
    print(str(5) + '5')
except TypeError:
    print("Niezdefiniowany operator")
else:
    print("Program działa poprawnie")
finally:
    # np. można zamknąć plik (niezależnie czy wystąpi wyjątek czy nie)
    print("To się wykona zawsze\n")

try:
    1 / 0
except ZeroDivisionError as err:  # as err zapisuje info o bledzie do zmiennej 'err'
    print("Dzielenie przez zero!")
    print(err)
else:
    print("Program działa poprawnie")
finally:
    # np. można zamknąć plik (niezależnie czy wystąpi wyjątek czy nie)
    print("To się wykona zawsze\n")

try:
    1 / 0
    5 + '5'
except (TypeError, ZeroDivisionError) as err:  # Dwa wyjątki jednocześnie
    print("Dzielenie przez zero!")
    print(err)
else:
    print("Program działa poprawnie")
finally:
    # np. można zamknąć plik (niezależnie czy wystąpi wyjątek czy nie)
    print("To się wykona zawsze\n")

try:

    raise TypeError  # Rzucamy wyjątek

except (TypeError, ZeroDivisionError) as err:
    print("Dzielenie przez zero!")
    print(err)
    print("Rzucony błąd")
else:
    print("Program działa poprawnie")
finally:
    # np. można zamknąć plik (niezależnie czy wystąpi wyjątek czy nie)
    print("To się wykona zawsze\n")


class Nasz_wyjatek(Exception):
    def __init__(self, s):
        print(s)
        print("Jestem w klasie wyjątku")


try:

    raise Nasz_wyjatek("Ala ma kota")  # Rzucamy wyjątek

except Nasz_wyjatek:
    print("Rzucony błąd")
else:
    print("Program działa poprawnie")
finally:
    # np. można zamknąć plik (niezależnie czy wystąpi wyjątek czy nie)
    print("To się wykona zawsze")
