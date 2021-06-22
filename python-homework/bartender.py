# selenium-py/001-python-alapok-1
# 28. feladat: Vezérlési szerkezetek gyakorlása.

# Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik.
# Kétféle italt ismerünk: sör és kóla.
# Ha a felhasználó kiskorú, és sört kér, akkor közöld vele, hogy sajnos nem adhatsz neki.
# Ha a felhasználó 60 feletti, és kólát kér, akkor közöld vele, hogy a koffein megemelheti a vérnyomását.
# Ha ismeretlen italt adott meg, akkor írd ki, hogy csak sört és kólát tudunk adni.
# Minden más esetben szolgáld ki. (Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon,a kólája.")

age = int(input("Életkorod? "))
drink = input("Mit iszol? ")
if age < 18 and drink == "sör":
    print("Sajnos kiskorűaknak nem szolgálhatunk fel sört.")
elif age > 60 and drink == "kóla":
    print("A koffein nagyon megemelheti a pulzusod.")
elif drink == "sör":
    print("Parancsolj, a söröd.")
elif drink == "kóla":
    print("Parancsolj, a kólád.")
else:
    print("2 féle italt tudunk felszolgálni: sört vagy kólát.")


