import datetime
print("Program obliczający ilość dni od urodzenia")
print("Autor: Marcin Brzeziński")
a = datetime.date.today()
print("Dziś jest ", a)
date_entry = input("Podaj datę urodzenia w formacie RRRR-MM-DD \n")
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
print ("Od urodzenia minęło",(a-date1).days,"dni")
