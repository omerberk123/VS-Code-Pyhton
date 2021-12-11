#index, #count
#in / not in


miniMiniBirler = ["buse", "ender", "büşra", "ömer", "ender", "selin", "ece", "ege"]
isim = "buse"
if isim in miniMiniBirler:
    print(f"{isim} liste içinde var")
    print(f"{miniMiniBirler.index(isim)}.indexli eleman")
else: 
    print(f"{isim} liste içinde yok")