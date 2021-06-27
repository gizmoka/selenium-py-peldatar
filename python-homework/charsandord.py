# # selenium-py/001-python-alapok-1
# # 22 Feladat: Python for ciklus gyakorlása.
#
# Írj programot, ami kiírja a kisbetűket, és melléjük az karakter kódjukat!
# A kiírás több oszlopos legyen, és legfeljebb 10 soros.
# Minta:
#  a 97 f 102 .....
#  b 98 g 103
#  c 99 h 104
#  d 100 i 105
#  e 101 j 106
#
# A megoldashoz használd a beépített ord() es chr() függvényeket.
#
#
# # saját megoldás - egyelőre félig kész

# Kocka megoldása
def check_alpha(counter):
    if chr(counter).isalpha():
        return chr(counter)
    else:
        return ""

def check_last_column(counter):
    if chr(counter).isalpha():
        return counter
    else:
        return ""

counter = 97
for i in range(10):
    print(chr(counter), counter,
          chr(counter + 10), counter + 10,
          check_alpha(counter + 20), check_last_column(counter + 20))
    counter += 1
