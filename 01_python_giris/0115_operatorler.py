#region aritmetik-operatorler
#aritmetik operatorler
"""
1→      +       toplama
2→      -       çıkarma
3→      *       çarpma
4→      /       bölme
5→      //      tam bölme
6→      **      üst alma
7→      %       mod alma
"""
#endregion 

#region işlemler
""""
print(2+3)
print(3-3)
print(4+2.8)
print(-9)
"""
#unary  sayının işareti 
#endregion

#region işlem örnekleri 
""""
print(5*6)
print(5*6.0)
print(10/2)
print(type(10/2))
print(16**0.5)
"""
#endregion


#region floor divison her zaman bir küçük sayıya yuvarlar
"""
print(12/7)
print(12//7)
"""
#endregion

print(12%5)

#region operator_oncelikleri
"""
1→  +, -        unary
2→  **          üst alma
3→  *, /, %     çarpma, bölme, mod alma
4→  +,-         toplama çıkarma
"""

print(3+4*5)
print(17/5%2)
print(15%4*2)   #% soldan başlayıp yaparız
print(15%4%2)   #% eğer öncelikler aynı sıradaysa
print(2**2**3)  #** right-side binding
print(2*3*(3-2)/2)
#endregion