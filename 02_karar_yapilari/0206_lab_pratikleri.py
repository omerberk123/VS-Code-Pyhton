"""
a=int(input("lütfen birinci notu giriniz: "))
b=int(input("lütfen ikinci notu giriniz: "))
c=int(input("lütfen üçüncü notu giriniz: "))
ort=(a+b+c)/3
if ort>=50:
    print("Dersi geçtin")

"""
"""
a=int(input("lütfen birinci sayıyı giriniz: "))
b=int(input("lütfen ikinci sayıyı giriniz: "))
if a>b:
    print(f" {a} > {b} ")
print(f" {b} > {a} ")
#ikinci çıktı için bir mantık hatası oldu. her halükarda 5 > 15 girdiğinde çalıştığını anlar.


x=int(input("lütfen bir sayı giriniz: "))
if x<0:
    x*=-1
print(f"{x} sayısının mutlak değeri {x}")

x=int(input("Lütfen bir sayı giriniz:"))
if x<0:
    y =x * -1
print(f"{x} sayının mutlak değeri [{y}]")
"""

"""
s1 = int(input("lütfen 1. sayıyı giriniz\t: "))
s2 = int(input("lütfen 2. sayıyı giriniz\t: "))
s3 = int(input("lütfen 3. sayıyı giriniz\t: "))
eb = 0
if s1>eb:
    eb = s1
if s2>eb:
    eb = s2
if s3>eb:
    eb = s3
    print(f"girilen değerlerin en büyüğü {eb}")
"""

fiyat = int(input("Lütfen bilet fiyatını giriniz:"))
agirlik = float(input("Lütfen bavul ağırlığı giriniz:"))
ogrenciMi = str(input("Öğreni misiniz? (Evet/Hayır): "))
if agirlik>15.0:
    fiyat += (agirlik-15)*5
if ogrenciMi == "Hayır":
    fiyat*=1.18
print(f"Bilet fiyatınız: {round(fiyat, 2)}")
