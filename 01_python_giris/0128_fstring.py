
"""
rakam = int(input("lütfen rakam giriniz\t: "))
print(str(rakam) + " rakamının 1 fazlası " + str(rakam+1))

#1.yontem format
rakam = int(input("lütfen rakam giriniz\t: "))
print("{} rakamının 1 fazlası {}" .format(rakam, (rakam+1)))

#2.yontem fstring
rakam = int(input("lütfen rakam giriniz\t: "))
print(f"{rakam} rakamın 1 fazlası {rakam+1}")
"""

s1 = int(input("1. sayıyı giriniz\t :"))
s2 = int(input("2. sayıyı giriniz\t :"))
s3 = int(input("3. sayıyı giriniz\t :"))
ort = (s1+s2+s3)/3
print(f"Girilen {s1}, {s2}, {s3} sayı değerlerinin ortalaması {ort}")

