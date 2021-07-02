# selenium-py/003-python-alapok-2/010 Feladat: Python lista gyakorlása

# Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig,
# amíg a felhasználó nullát nem ad be!
# A program az összes értéket tárolja egy listában,
# majd írja ki a képernyőre a lista elemeit fordított sorrendben!
# A megoldást egy fordito.py nevű file-ban kell beadnod.

my_list = []
user_input = ()
while user_input != 0:
    user_input = int(input("Enter a positive integer: "))
    my_list.append(user_input)
for element in my_list[::-1]:
    print(element)
# print(my_list[::-1]) - listaként adja vissza a fordított sorrendet
