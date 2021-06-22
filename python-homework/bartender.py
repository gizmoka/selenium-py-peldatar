# selenium-py/001-python-alapok-1
# 28. feladat: Vezérlési szerkezetek gyakorlása.

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


