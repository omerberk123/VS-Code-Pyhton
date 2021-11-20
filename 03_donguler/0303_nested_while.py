#region nested_if
# iç içe döngü - iç içe loop
"""
+1 -> BAŞLANGIÇ
+2 -> BİTİŞ
+3 -> ARTIŞ MİKTARI
"""
#region

i , j = 0, 0 
while i<3:
    while j<3:
        j +1= 1
        print(i, " ", j)
    i += 1
    j = 0

i, j = 0, 0
while i<10:
    while j<10:
        j += 1
    i += 1

