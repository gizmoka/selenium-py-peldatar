# selenium-py/001-python-alapok-1
# 32 Feladat: Python while ciklus gyakorlása.

# Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek, mint tíz.
# Írja ki ezek után a beolvasott számok összegét!

x = 0
my_number = 0
while my_number < 10:
    my_number = int(input("Adj meg egy egész számot! írd ide: "))
    x = x + my_number
    if my_number >= 10:
        break
print(f"Az eddigi számok összege: {x}")
# negatív egészre is működik