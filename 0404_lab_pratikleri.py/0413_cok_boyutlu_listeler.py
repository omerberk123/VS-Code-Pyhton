# region cok_boyutlu_listeler_giris
"""
matris yapıları oluşturma
veri tabanı mimarisine benzer satırxsütun yapıları oluşturma
"""
# endregion

# region kurum_ici_veri_tabani_ornegi
"""
Örn. kurum içi bilgisayarların özelliklerini tutacağınız bir tablo
Bil.No  Cihaz Adı       CPU     PID
1       Desktop_Test    %56     chrome.exe
2       Guest101        %60     excel.exe
3       Kat-1_Laptop    %90     camtasia.exe, chrome.exe
"""
# endregion
# region 
"""
print(a)
2x4
1 2 3 4
5 6 7 8

a = [[1,2,3,4], [5,6,7,8]]
print(a[0])
print(a[1])
print(a[1][1])
a[1][1] = 66
print(a[1])

a = [[1,2,3,4], [5,6,7,8]]

for i in range(2): #0,1
    for j in range(4): #0,1,2,3
        print(a[i][j], end=" ")
    print()

a = [[1,2,3,4], [5,6,7,8], [9,9,9,9]]

for i in range(len(a)): #0,1
    for j in range(4): #0,1,2,3
        print(a[i][j], end=" ")
    print()


a = [[1,2,3,4,5], [5,6,7,8,9], [9,9,9,9,9]]

for i in range(len(a)): #0,1
    for j in range(len(a[i])): #0,1,2,3
        print(a[i][j], end=" ")
    print()
"""
# endregion
"""
liste = [[1, "Desktop_Test", 56, "chrome.exe"], [2, "Guest101", 60, "excel.exe"], [3, "Kat-1_Laptop", 90, "camtasia.exe, chrome.exe"]]
for i in range(len(liste)):
    for j in range (len(liste[i])):
        if j == 2:
            print(f"%{liste[i][j]}", end= " ")
        else:  
            print(f"{liste[i][j]}", end= " ")
    print()

liste = [[1, "Desktop_Test", 56, "chrome.exe"], 
        [2, "Guest101", 60, "excel.exe"],  
        [3, "Kat-1_Laptop", 90, "camtasia.exe, chrome.exe"]
]
for i in range(len(liste)):
        if liste[i][2]>80:
            print(f"bilgisayar adı {liste[i][1]} olan {liste[i][0]}.kattaki host'un işlemcisi %{liste[i][2]}")

liste = [[random.randrange(30,40) for j in range(24)] for i in range(7)]
gununHangiSaati = int(input("Hangi Gün [0..24] "))
yeniSicaklik = []
for sicaklik in liste:
    yeniSicaklik.append(sicaklik[gununHangiSaati])
print(f"tüm haftada {gununHangiSaati} saatteki ortalama sıcaklık {sum(yeniSicaklik)/len(yeniSicaklik)} ")"""
