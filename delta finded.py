# len() uzunluk
# find() string arama
# lower() Stringleri Kucuk Harf yapma
# upper() Stringleri buyuk harf yapma
# title() Basliklari buyuk harf yapma
# count() String sayisini ogrenme
# replace("degisen","neyle degistireceginiz") string degistirme
# rfind() Sondan baslayarak karakter bulma
# in keyword  stringin icinde olup-olmadigini ogrenme


temp=float(input("Hava Kac Derece: "))
yagmur=input("Yagmur Yagiyormu? ")
kar=input("Peki Kar Yagiyormu? ")
soguk=False
sicak=False
yagmurlu=False
karli=False
prosese="e"
prosesh="h"
if temp>=25:
    sicak=True
    if yagmur==prosese and kar==prosesh:
        print("Hava Sicak ve Yagmur Yagiyor")
    elif yagmur==prosese and kar==prosese:
        print("Cok Garip Bir Hava... ve sicak")
    elif yagmur==prosesh and kar==prosesh:
        print("Hava Sadece Sicak")

else:
    soguk=True
    if soguk:
        print("Hava Biraz Soguk")
        if yagmur==prosese and kar==prosesh:
            print("Hava Soguk ve Yagmur Yagiyor")
        elif yagmur==prosese and kar==prosese:
            print("Cok Garip Bir Hava... ve soguk")
        elif yagmur==prosesh and kar==prosesh:
            print("Hava Sadece soguk")




































    
    

