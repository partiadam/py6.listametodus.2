'''
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre! 
A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, és a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!
'''

from random import randint

veletlen = []
masiklista = []

for szam in range(10):
    szam = randint(1, 3)
    masiklista.append(szam)
    veletlen.append(szam)
print(veletlen)

beker = int(input('Szám (1-3): '))
for szam in masiklista:
    if beker == szam:
        veletlen.remove(szam)
print(veletlen) 


    

