# selenium-py/001-python-alapok-1
# 37 Feladat: Python függvények gyakorlása.

# Szökőév?
# Készíts függvényt, amelyik adott évszámról eldönti, hogy az szökőév-e.
# Szökőév minden negyedik, nem szökőév minden századik, mégis az minden 400-adik.
# (2000-ben ezért volt szökőév.)
# A függvény visszatérési értéke legyen logikai típusú!
# Tipp( % maradekos osztas operátor)
# Írj programot, amelyik a felhasználótól évszámokat kér, és mindegyikre kiírja, hogy szökőév-e!
# Használd az előbb megírt függvényt!
# Például: ? 2005 Nem szökőév. ? 2000 Szökőév. ? 1980 Szökőév. ? 1900 Nem szökőév.

# saját megoldás 1
input_year = int(input("Give me a year you want to check if it is a leap year or not. "))
if input_year % 400 == 0:
    print("leap year")
else:
    if input_year % 4 ==0 and input_year % 100 != 0:
        print("leap year")
    else:
        print("not a leap year")

# saját megoldás 2 (visszatérési érték: logikai változó)
input_year = int(input("Give me a year you want to check if it is a leap year or not. "))
if input_year % 400 == 0:
    print(True)
else:
    if input_year % 4 ==0 and input_year % 100 != 0:
        print("True")
    else:
        print("False")


# függvénnyel:
def checkYear(year):
    import calendar
    return (calendar.isleap(year))

year = int(input("please give a year: "))
if (checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")
# source: https://www.geeksforgeeks.org/program-check-given-year-leap-year/

# 4. megoldás

year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
# source: https://www.javatpoint.com/python-check-leap-year

# Válaszok:
# 2005: Nem szökőév.
# 2000 Szökőév.
# 1980 Szökőév.
# 1900 Nem szökőév.

# Ez alapján: https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
# The following years are not leap years: 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600
# The following years are leap years: 1600, 2000, 2400
