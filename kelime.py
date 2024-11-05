import random

harfler = ["a","b","c","ç","d","e","f","g","ğ","ı","i","j","k",
           "l","m","n","o","ö","r","p","v","y","z","t","h",
           "u","ü","s","ş"]
havuz = []
kelimenin_harfleri = {}

harf_oranları = {"a":100,"b": 100,"c": 100,"ç": 100,"d": 100,"e": 100,"f": 100,
                "g": 100,"ğ": 100,"ı": 100,"i": 100,"j": 100,"k": 100,
                "l": 100,"m": 100,"n": 100,"o": 100,"ö": 100,"r": 100,"p": 100,"v": 100,
                "y": 100,"z": 100,"t": 100,"h": 100,"u": 100,"ü": 100,"s": 100,"ş": 100}

yazı = ""
seçilen_harf = ""
hedef = "elma"

deneme_sayısı = 0
doğruluk_oranı = 100
yuvarlanmış_sayı = 0
kelime_sayısı = 0

for c in range(300):
    kelime = list(random.choice(["elma","yedi","deri","veri","kedi"]))
    print(kelime)
    for i in range(len(kelime)):
        seçilen_harf = ""
        while seçilen_harf != kelime[i]:
            if c < 1:
                kelimenin_harfleri[i] = {harf:oran for harf, oran in sorted(harf_oranları.items(), key=lambda x: x[1], reverse=True)}
            havuz = {harf: oran for harf, oran in sorted(kelimenin_harfleri[i].items(), key=lambda x: x[1],reverse=True)}.copy().keys()
            for y in havuz:
                seçilen_harf = y
                deneme_sayısı += 1
                if seçilen_harf != kelime[i]:
                    doğruluk_oranı -= 1
                    yuvarlanmış_sayı = doğruluk_oranı / 100
                    kelimenin_harfleri[i][seçilen_harf] = round(harf_oranları[seçilen_harf] - yuvarlanmış_sayı * 3, 2)

                elif seçilen_harf == kelime[i]:
                    doğruluk_oranı += 1
                    yuvarlanmış_sayı = doğruluk_oranı / 100
                    kelimenin_harfleri[i][seçilen_harf] = round(2 *yuvarlanmış_sayı + harf_oranları[seçilen_harf], 2)
                    break

            doğruluk_oranı = 100
            yuvarlanmış_sayı = 0
        yazı += seçilen_harf
        if list(yazı) == kelime:
            kelime_sayısı += 1
            print(f"yazılan kelime:{yazı}")
            print(f"deneme sayısı:{deneme_sayısı}")
            yazı = ""
            deneme_sayısı = 0


