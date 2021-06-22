# selenium-py/001-python-alapok-1
# 16. feladat: Python Adatok és változók feladat. 2. alfeladat.

# Az autód 7 litert fogyaszt országúton és 9-et városban.
# A hévízi üdülésedre 170 kilómétert utazol országúton és 35-öt városban.
# Mennyit fogyaszt az autód csak oda? És oda-vissza?
# Mennyibe kerül a teljes út, ha 350 Ft a benzin?
# Oldd meg ezt feladatot úgy, hogy nem előre megadott értékekkel (országúti fogyasztás, városi fogyasztás, országúton megtett út, városban megtett út, benzin ára) dolgozol,
# hanem a felhasználótól kéred ezeket be.
# Ahol szükséges, ne feledd konvertálni az értékeket!



# Mennyit fogyaszt az autód csak oda? És oda-vissza?
consumption_total_1_way = 7 + 7*70/100 + 9*35/100
consumption_total_return = 2 * consumption_total_1_way
print(consumption_total_1_way)
print(consumption_total_return)



# Mennyibe kerül a teljes út, ha 350 Ft a benzin?
total_cost = 350 * consumption_total_return
print(f"A teljes út oda-vissza {int(total_cost)} Forintba kerül.")

# Oldd meg ezt feladatot úgy, hogy nem előre megadott értékekkel (országúti fogyasztás, városi fogyasztás, országúton megtett út, városban megtett út, benzin ára) dolgozol,
# hanem a felhasználótól kéred ezeket be.

orszaguti_fogyasztas = int(input("Mennyi volt az országúti fogyasztás oda-vissza? "))
varosi_fogyasztas = int(input("Mennyi volt a városi fogyasztás oda-vissza? "))
orszaguton_megtett_ut = int(input("Hány kilométert tett meg országúton oda-vissza? "))
varosban_megtett_ut = int(input("Hány kilométert tett meg a városban oda-vissza? "))
teljes_fogyasztas = int(orszaguti_fogyasztas*orszaguton_megtett_ut/100 + varosi_fogyasztas*varosban_megtett_ut/100)
benzin_ara = int(input("Mennyibe kerül 1 liter benzin? "))
teljes_ut_ara = benzin_ara * teljes_fogyasztas
print(f"A teljes út ára összesen {int(teljes_ut_ara)} Forintba került.")