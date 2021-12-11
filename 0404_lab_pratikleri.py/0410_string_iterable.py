"""
kurumAdi = "ecodation"
print(kurumAdi)
print(type(kurumAdi)) #str -> iterable
print(kurumAdi[2])
for i in kurumAdi:
    print(i)
    """

"""kurumAdi = "ecodation"
ara = input("aranan karakter: ")
if ara in kurumAdi:
    print(f"{kurumAdi.count(ara)} adet bulundu")
else:
    print("karakter bulunamadı")"""
"""
kurumAdi = "ecodation"
sesliHarfler = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
for i in kurumAdi:
    if i in sesliHarfler:
        print(f"{i} sesli harfinden {kurumAdi.count(i)} var")


kurumAdi = "ecodation"
sesliHarfler = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
yeniListe = []
for i in kurumAdi:
    if i in sesliHarfler:
        yeniListe.append(i)
yeniListe.sort()
print(yeniListe)

kurumAdi = "ecodation"
sesliHarfler = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
yeniListe = []
for i in kurumAdi:
    if i in sesliHarfler and not i in yeniListe:
        yeniListe.append(i)
print(yeniListe)
"""