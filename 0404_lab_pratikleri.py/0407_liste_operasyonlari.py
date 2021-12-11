"""
#list-swap
listem = [3, 6, 8, 9, 4]
temp = listem[1]
listem[1] = listem[2]
listem[2] = temp
print(listem)

"""

#slice
"""
miniMiniBirler = ["buse", "büşra", "ömer", "ender", "selin",]
print(miniMiniBirler)
print("="*50)
for i in miniMiniBirler:
    print(i, end=" ")
print("=*50")
print(miniMiniBirler[3])"""
"""
print(miniMiniBirler[0:3])
print[miniMiniBirler[1:3]]
isim = " ender barış"
ad = isim[0:5]
print(ad)
soyad1= isim[6:12]
soyad2 = isim[6:]
ad1 = isim[:5]"""

isim = "ender barış"
"""adSoyad = isim[:]
sonKarakter = isim[-1]
print(sonKarakter)"""

"""
#print(isim[::-1]) #sondan başa doğru
print(isim[1:])
print(isim[1:9])
print(isim[1:9:2])"""


miniMiniBirler = ["0buse", "1ender", "2büşra", "3ömer", "4enderr", "5selin", "6ece", "7ege"]
print(miniMiniBirler[1:])
print(miniMiniBirler[1:7])
print(miniMiniBirler[1:7:2])
url = " www.azizbektas.gov"
print(url[-3:])
if not url[-3:]=="com" and not url[-3]=="gov":
    print("hatalı url")
else:
    print("hatalı url, edu olmalı")