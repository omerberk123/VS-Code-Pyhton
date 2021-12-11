notlar=[10,55,90,77,85,45,77]
toplam=0
for i in notlar:
   toplam+=i

print(toplam)
print(len(notlar))
genelOrtalama=toplam/len(notlar)
for b in notlar:
    if b<genelOrtalama:
        print(f"Çan eğrisine göre kalacak notlar\t: {b} ")
    else:
        print(f"Çan eğrisinden yüksek alan notlar\t: {b} ")

#ödev
"""
rakamlar = [6, 2, 7, 3, 5]
Çıktı:
["ALTI", "İKİ", "YEDİ", "ÜÇ", "BEŞ"]
"""

rakamlar = [6, 2, 7, 3, 5]
yaziİle = ["", "BİR","İKİ","ÜÇ", "DÖRT", "BEŞ", "ALTI", "YEDİ", "SEKİZ", "DOKUZ"]
for i in rakamlar:
    print(yaziİle)
print(yaziİle[8])
