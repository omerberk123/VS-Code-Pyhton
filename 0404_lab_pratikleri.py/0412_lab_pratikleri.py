"""ogrenci1 = ["Alp", "Besi", 90,	90]
ogrenci2 = ["Batu", "Koçhan", 10, 90]
ogrenci3 = ["Emir", "Besi", 100,	90]
ogrenci4 = ["Umut", "Ahmet", 95, 80]
ogrenci5 = ["Aziz", "Bektaş", 15, 10]
ogrenciler = [ogrenci1, ogrenci2, ogrenci3, ogrenci4, ogrenci5]

for i in (ogrenciler):
    ort = (i[2]+i[3])/2
    if ort<50:
        print(f" Öğrenci adı soyadı: {i[0]} {i[1]} aldığı notlar: {i[2]}, {i[3]}. Kaldı.")
    else:
        print(f" Öğrenci adı soyadı: {i[0]} {i[1]} aldığı notlar: {i[2]}, {i[3]}. Geçti.")

aziz hoca atacak..


ogrenci1 = [
    "Alp",
    "Besi",
    90,
    90,
    "Video, size görüşünüzü kanıtlamak için güçlü bir yol sunar. Çevrimiçi Video'ya tıkladığınızda, eklemek istediğiniz videoya ait ekleme kodunu yapıştırabilirsiniz. Belgenize en iyi uyan videoyu çevrimiçi olarak aramak için bir anahtar sözcük de yazabilirsiniz.Word, belgenizin profesyonelce üretilmiş görünmesini sağlamak için birbirini tamamlayan üst bilgi, alt bilgi, kapak sayfası ve metin kutusu tasarımları sağlar. Örneğin, birbiriyle uyumlu bir kapak sayfası, başlık ve kenar çubuğu ekleyebilirsiniz. Ekle'ye tıklayın ve ardından farklı galerilerden eklemek istediğiniz öğeleri seçin.Temalar ve stiller de belgenizin düzenli kalmasına yardımcı olur. Tasarım'a tıklayıp yeni bir Tema seçtiğinizde, resimler, grafikler ve SmartArt grafikleri, yeni temanızla eşleşecek şekilde değiştirilir. Stilleri uyguladığınızda, başlıklarınız yeni tema ile eşleşecek şekilde değiştirilir."
]
ogrenci2 = [
    "Batu",
    "Koçhan",
    10,
    90,
    "Video, size görüşünüzü kanıtlamak için güçlü bir yol sunar. Çevrimiçi Video'ya tıkladığınızda, eklemek istediğiniz videoya ait ekleme kodunu yapıştırabilirsiniz. Belgenize en iyi uyan videoyu çevrimiçi olarak aramak için bir anahtar sözcük de yazabilirsiniz.Word, belgenizin profesyonelce üretilmiş görünmesini sağlamak için birbirini tamamlayan üst bilgi, alt bilgi, kapak sayfası ve metin kutusu tasarımları sağlar. Örneğin, birbiriyle uyumlu bir kapak sayfası, başlık ve kenar çubuğu ekleyebilirsiniz. Ekle'ye tıklayın ve ardından farklı galerilerden eklemek istediğiniz öğeleri seçin.Temalar ve stiller de belgenizin düzenli kalmasına yardımcı olur. Tasarım'a tıklayıp yeni bir Tema seçtiğinizde, resimler, grafikler ve SmartArt grafikleri, yeni temanızla eşleşecek şekilde değiştirilir. Stilleri uyguladığınızda, başlıklarınız yeni tema ile eşleşecek şekilde değiştirilir."
]
ogrenci3 = [
    "Emir",
    "Besi",
    100,
    90,
    "Video, size görüşünüzü kanıtlamak için güçlü bir yol sunar. Çevrimiçi Video'ya tıkladığınızda, eklemek istediğiniz videoya ait ekleme kodunu yapıştırabilirsiniz. Belgenize en iyi uyan videoyu çevrimiçi olarak aramak için bir anahtar sözcük de yazabilirsiniz.Word, belgenizin profesyonelce üretilmiş görünmesini sağlamak için birbirini tamamlayan üst bilgi, alt bilgi, kapak sayfası ve metin kutusu tasarımları sağlar. Örneğin, birbiriyle uyumlu bir kapak sayfası, başlık ve kenar çubuğu ekleyebilirsiniz. Ekle'ye tıklayın ve ardından farklı galerilerden eklemek istediğiniz öğeleri seçin.Temalar ve stiller de belgenizin düzenli kalmasına yardımcı olur. Tasarım'a tıklayıp yeni bir Tema seçtiğinizde, resimler, grafikler ve SmartArt grafikleri, yeni temanızla eşleşecek şekilde değiştirilir. Stilleri uyguladığınızda, başlıklarınız yeni tema ile eşleşecek şekilde değiştirilir."
]
ogrenci4 = [
    "Umut",
    "Ahmet",
    95,
    80,
    "Video, size görüşünüzü kanıtlamak için güçlü bir yol sunar. Çevrimiçi Video'ya tıkladığınızda, eklemek istediğiniz videoya ait ekleme kodunu yapıştırabilirsiniz. Belgenize en iyi uyan videoyu çevrimiçi olarak aramak için bir anahtar sözcük de yazabilirsiniz.Word, belgenizin profesyonelce üretilmiş görünmesini sağlamak için birbirini tamamlayan üst bilgi, alt bilgi, kapak sayfası ve metin kutusu tasarımları sağlar. Örneğin, birbiriyle uyumlu bir kapak sayfası, başlık ve kenar çubuğu ekleyebilirsiniz. Ekle'ye tıklayın ve ardından farklı galerilerden eklemek istediğiniz öğeleri seçin.Temalar ve stiller de belgenizin düzenli kalmasına yardımcı olur. Tasarım'a tıklayıp yeni bir Tema seçtiğinizde, resimler, grafikler ve SmartArt grafikleri, yeni temanızla eşleşecek şekilde değiştirilir. Stilleri uyguladığınızda, başlıklarınız yeni tema ile eşleşecek şekilde değiştirilir."
]
ogrenci5 = [
    "Aziz",
    "Bektaş",
    15,
    10,
    "Muhtar"
]
ogrenciler = [ogrenci1, ogrenci2, ogrenci3, ogrenci4, ogrenci5]
for i in ogrenciler:
    ort = (i[2]+i[3])/2
    if len(i[4]) > 20:
        cv = f"{i[4][:20]}..."
    else:
        cv = i[4]
    if ort < 50:
        print(
            f"Öğrenci adı soyadı: {i[0]} {i[1]} aldığı notlar: {i[2]}, {i[3]}. Kaldı. {cv}")
    else:
        print(
            f"Öğrenci adı soyadı: {i[0]} {i[1]} aldığı notlar: {i[2]}, {i[3]}. Geçti.{cv}")


liste = [[random.randrange(30,40) for j in range(24)] for i in range(7)]
haftaninKacinciGunu = int(input("Hangi Gün [1..7] "))
for i in range(len(liste)):
    for j in range(len(liste[i])):
        if i==1:
            print(liste[i][j], end= " ")

"""

