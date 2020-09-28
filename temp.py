print("Banka Giris")
def_kullaniciadi="admin"
def_kullaniciparola="admin2002"

def kullanici_girisi():
    while True:
        kullaniciadi=input("Kullanici Adiniz: ")
        kullaniciparola=input("Kullanici Parolaniz: ")
        
        if (kullaniciadi==def_kullaniciadi) and (kullaniciparola!=def_kullaniciparola):
            print("Parolaniz Yanlis...")
        elif (kullaniciadi!=def_kullaniciadi) and (kullaniciparola==def_kullaniciparola):   
            print("Kullanici Adiniz Yanlis")
        elif (kullaniciadi=="quit") and (kullaniciparola=="quit"):
            break
        elif (kullaniciadi!=def_kullaniciadi) and (kullaniciparola!=def_kullaniciparola):
            print("Yanlis Giris...")
        elif (kullaniciadi==def_kullaniciadi) and (kullaniciparola==def_kullaniciparola):
            print("Giris Yapilmistir...")
            print(f"Merhaba,{kullaniciadi}")
            print("Nasil Yardimci Ola Biliriz? ")
            print("1-Para Cekme")
            print("2-Para Yatirma")
            print("3-Kredi Cekme")
            
            giris=int(input("Secenek: "))
            
            if giris==1:
                bakiye=8500
                print(f"Bakiyeniz-{bakiye}")
                cekilecek_para=float(input("Ne Kadar Para Cekmek Istiyorsunuz? "))
                kalan_miktar=float(bakiye)-cekilecek_para
                print(f"Kalan Bakiyeniz: {kalan_miktar} TL...")
                break
            elif giris==2:
                bakiye=8500
                print(f"Bakiyeniz-{bakiye}")
                yatirilacak_para=float(input("Ne Kadar Para Yatirmak Istiyorsunuz? "))
                toplam_miktar=float(bakiye)+yatirilacak_para
                print("Para Yatirma Islemi Tamamlanmistir...")
                print(f"Toplam Bakiyeniz: {toplam_miktar} TL...")
                break
            elif giris==3:
                bakiye=8500
                kredi_miktari=float(input("Ne Kadar Kredi Cekmek Istiyorsunuz? "))
                kredi_zaman=int(input("Kac Aylik Kredi..."))
                kredi_odeme=input("Kredi Icin On Odeme Istiyormusunuz? ")
                
                if kredi_odeme.lower()=="evet":
                    kredi_odeme_odenecekpara=float(input("Ne Kadar On Odeme Yapcaksiniz? "))
                    
                    if kredi_odeme_odenecekpara>bakiye:
                        print("Yeterli Bakiye Yoktur...")
                        continue
                    else:
                        print("Odeme Islemi Baslamistir...")
                        toplamkredi_borcu=kredi_miktari-float(bakiye)
                        kredi_aylikborcu=float(toplamkredi_borcu/kredi_zaman)
                        print(f"Aylik Odeyeceginiz Miktar: {kredi_aylikborcu} TL...")
                        break
                elif kredi_odeme.lower()=="hayir":
                    kredi_aylikborcu=float(kredi_miktari/kredi_zaman)
                    print(f"Aylik Kredi Borcunuz: {kredi_aylikborcu} TL...")
                    break
                
                
kullanici_girisi()
        


    

    
        
        
 
    
    
