"""ad = "aziz"
for i in ad:
    print(i)"""

#geleneksek for
"""liste = []
for i in range(1, 9):
    liste.append(i)
print(liste)"""

#in-line for
"""
liste=[i for i in range(1,9)]
liste2=[i*i for i in range(1, 9) if i>5]
print(liste2)
"""
# region ornek
"""
Haftanın 1. Günü Pazartesi  Haftanın 2. Günü Salı ...
"""
haftaninGunleri = ["", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

liste = [f"Haftanın {i}. Günü {haftaninGunleri[i]}" for i in range(1, 8) if i<=3]
print(liste)