#region
"""
loop 
loop ne zaman kullanılır?
loop -> sürekli tekrarlayan işlemlerin yapılmasını sağlayan komutlardır

indirimOrani = 5
print(f"Ekstra %{indirimOrani} İndirim Orani ") 
print(f"Ekstra %{indirimOrani} İndirim Orani ") 
print(f"Ekstra %{indirimOrani} İndirim Orani ") 

indirimOrani = 5
i = 0
while i<3:
    print(f"Ekstra %{indirimOrani} İndirim Orani")
    i += 1


indirimOrani = 5 
while True:
    print(f"Ekstra %{indirimOrani} İndirim Orani") infinite loop olmaması için eğer sonsuza dek calısmamasını istiyorsan ctrl + c yap
    """
#endregion

"""
1 -> BAŞLANGIÇ
2 -> BİTİŞ
3 -> ARTIK MİKTARI

i = 1
while i<=3:
    print(f"Ekstra %5 İndirim Orani ") 
    i += 1

i = 1
print(f"a")
while i<3: 
    print(f"b")
    i += 1
print(f"c")
"""
#region i=5 ten başlayacak. azalarak while'ı kontrol edelim 5....0'a kadar ekrana yazsın
"""
i = 5
while i>=0:
    print(f"{i}")
    i-=1

i = 5
while i!=0:
    print(f"{i}")
    i-=1
"""
#endregion

"""
yas = int(input("lütfen yaş gilgisi giriniz: "))
if yas:
    print(yas)
else:
    print("yaş değeri 0 olamaz")
devamMi=True 
"""

