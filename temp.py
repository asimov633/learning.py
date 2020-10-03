def mainfunction():
    def_kullanici="admin"
    def_parola="admin2002"
    while True:
        print("Kredi Sorgusuna Giris Yapmak Icin Bilgilerinizi Girin...")
        giris_kullanici=input("Kullanici Adi: ")
        giris_parola=input("Parola: ")
        
        if (giris_kullanici!=def_kullanici) and (giris_parola==def_parola):
            print("Kullanici Adiniz Yanlis!")
            continue
        
        elif (giris_kullanici==def_kullanici) and (giris_parola!=def_parola):
            print("Yanlis Giris Yaptiniz!")
            parola_secenek=input("Sifrenizi Degistirmek Istiyormusunuz? ")
            
            if parola_secenek.lower()=="evet":
                yeni_parola=input("Yeni Parola: ")
                yeni_parola_tekrar=input("Tekrar Yeni Parola: ")
                
                if yeni_parola!=yeni_parola_tekrar:
                    print("Yanlis Parola Girdiniz Tekrar Giris Yapin...")
                    continue
                elif yeni_parola==yeni_parola_tekrar:
                    def_parola=yeni_parola
                    print("Sifre Basari Ile Degistirilmistir...")
                    continue
            elif parola_secenek.lower()=="hayir":
                print("Giris Yapmaya Devam Edin...")
                continue
        
        elif (def_kullanici==giris_kullanici) and (def_parola==giris_parola):
            print("Giris Basari Ile Yapilmistir...")
            print("Telefon Markasini Girerek Baslaya Bilirsiniz")
            telefon_marka=input("Marka: ")
            
            if telefon_marka.lower()=="iphone":
                marka_numara=input("Hangi Seri Olsun? ")
                
                if marka_numara.lower()=="x":
                    print("9.399,99 TL...")
                    
                    secenek_=input("Alis Nasil Olacak? ")
                    if secenek_.lower()=="kredi":
                        print("Kredi Icin Bankaya Yonlendiriliyorsunuz...")
                        
                        print("Bankaya Hos Geldiniz...")
                        banka_kullanici=input("Banka Kullanici Adiniz: ")
                        banka_parola=input("Banka Parolaniz: ")
                        
                        if banka_kullanici=="yusifhacizade" and banka_parola=="0554057235":
                            print("Giris Dogrudur...")
                            bakiye=8500
                            print(f"Bakiyeniz: {bakiye}")
                            kredimiktari=9399-int(bakiye)
                            print(f"Telefon icin {kredimiktari} kadar Kredi Cekmelisiniz...")
                            
                            secenek2=input("Kredi Cekilsinmi? ")
                            
                            if secenek2.lower()=="evet":
                                print(f"Cekilecek Miktar: {kredimiktari} TL...")
                                kredi_ay=int(input("Kac Aylik Kredi: "))
                                
                                kredi_borcu=float(kredimiktari/kredi_ay)
                                
                                print(f"Aylik Borcunuz: {kredi_borcu} TL...")
                                break
                            elif secenek2.lower()=="hayir":
                                print("Islem Tamamlanmadi...")
                                break
                            else:
                                print("Yanlis Secim...")
                                break
                        elif banka_kullanici!="yusifhacizade" and banka_parola=="0554057235":
                            print("Kulllanici Adiniz Yanlis...")
                            continue
                        elif banka_kullanici=="yusifhacizade" and banka_parola!="0554057235":
                            print("Parolaniz Yanlis...")
                            continue
                        else:
                            print("Yanlis Giris!")
                            break
                    else:
                        print("Yalnizca Kredi Gecerlidir...")
                        break
                elif marka_numara=="6":
                    print("1.749,99 TL...")
                    print("Kredi Icin Bankaya Yonlendiriliyorsunuz...")
                        
                    print("Bankaya Hos Geldiniz...")
                    banka_kullanici=input("Banka Kullanici Adiniz: ")
                    banka_parola=input("Banka Parolaniz: ")
                    
                    if banka_kullanici=="yusifhacizade" and banka_parola=="0554057235":
                        print("Banka Girisi Dogrulandi...")
                        bakiye=8500
                        
                        alis=input("Telefon Alinsinmi? ")
                        
                        if alis.lower()=="evet":
                            kalan_para=int(bakiye)-1749
                            
                            print(f"Alis Gerceklesti...")
                            print(f"Kalan Banka Bakiyeniz: {kalan_para}")
                            break
                        elif alis.lower()=="hayir":
                            print("Alis Gerceklestirilmedi...")
                            break
                        else:
                            print("Lutfen (Evet) ve ya (Hayir) Seklinde Giris Yapiniz!")
                            break
                    elif banka_kullanici=="yusifhacizade" and banka_parola!="0554057235":
                        print("Parolaniz Yanlis!")
                        continue
                    elif banka_kullanici!="yusifhacizade" and banka_parola=="0554057235":
                        print("Kullanici Adiniz Yanlis...")
                        continue
                    else:
                        print("Lutfen Dogru Giris Yapin...")
                        break
                    
                elif marka_numara=="7":
                    print("3.799,99 TL...")
                    print("Kredi Icin Bankaya Yonlendiriliyorsunuz...")
                        
                    print("Bankaya Hos Geldiniz...")
                    banka_kullanici=input("Banka Kullanici Adiniz: ")
                    banka_parola=input("Banka Parolaniz: ")
                    
                    if banka_kullanici=="yusifhacizade" and banka_parola=="0554057235":
                        print("Banka Girisi Dogrulandi...")
                        bakiye=8500
                        
                        alis=input("Telefon Alinsinmi? ")
                        
                        if alis.lower()=="evet":
                            kalan_para=int(bakiye)-3799
                            
                            print(f"Alis Gerceklesti...")
                            print(f"Kalan Banka Bakiyeniz: {kalan_para}")
                            break
                        elif alis.lower()=="hayir":
                            print("Alis Gerceklestirilmedi...")
                            break
                        else:
                            print("Lutfen (Evet) ve ya (Hayir) Seklinde Giris Yapiniz!")
                            break
                    elif banka_kullanici=="yusifhacizade" and banka_parola!="0554057235":
                        print("Parolaniz Yanlis!")
                        continue
                    elif banka_kullanici!="yusifhacizade" and banka_parola=="0554057235":
                        print("Kullanici Adiniz Yanlis...")
                        continue
                    else:
                        print("Lutfen Dogru Giris Yapin...")
                        break
                    
                elif marka_numara=="8":
                    print("5.749,90 TL...")
                    print("Kredi Icin Bankaya Yonlendiriliyorsunuz...")
                        
                    print("Bankaya Hos Geldiniz...")
                    banka_kullanici=input("Banka Kullanici Adiniz: ")
                    banka_parola=input("Banka Parolaniz: ")
                    
                    if banka_kullanici=="yusifhacizade" and banka_parola=="0554057235":
                        print("Banka Girisi Dogrulandi...")
                        bakiye=8500
                        
                        alis=input("Telefon Alinsinmi? ")
                        
                        if alis.lower()=="evet":
                            kalan_para=int(bakiye)-5749
                            
                            print(f"Alis Gerceklesti...")
                            print(f"Kalan Banka Bakiyeniz: {kalan_para}")
                            break
                        elif alis.lower()=="hayir":
                            print("Alis Gerceklestirilmedi...")
                            break
                        else:
                            print("Lutfen (Evet) ve ya (Hayir) Seklinde Giris Yapiniz!")
                            break
                    elif banka_kullanici=="yusifhacizade" and banka_parola!="0554057235":
                        print("Parolaniz Yanlis!")
                        continue
                    elif banka_kullanici!="yusifhacizade" and banka_parola=="0554057235":
                        print("Kullanici Adiniz Yanlis...")
                        continue
                    else:
                        print("Lutfen Dogru Giris Yapin...")
                        break
                elif marka_numara.lower()=="8 plus":
                    print("6.699,99 TL...")
                    print("Kredi Icin Bankaya Yonlendiriliyorsunuz...")
                        
                    print("Bankaya Hos Geldiniz...")
                    banka_kullanici=input("Banka Kullanici Adiniz: ")
                    banka_parola=input("Banka Parolaniz: ")
                    
                    if banka_kullanici=="yusifhacizade" and banka_parola=="0554057235":
                        print("Banka Girisi Dogrulandi...")
                        bakiye=8500
                        
                        alis=input("Telefon Alinsinmi? ")
                        
                        if alis.lower()=="evet":
                            kalan_para=int(bakiye)-6699
                            
                            print(f"Alis Gerceklesti...")
                            print(f"Kalan Banka Bakiyeniz: {kalan_para}")
                            break
                        elif alis.lower()=="hayir":
                            print("Alis Gerceklestirilmedi...")
                            break
                        else:
                            print("Lutfen (Evet) ve ya (Hayir) Seklinde Giris Yapiniz!")
                            break
                    elif banka_kullanici=="yusifhacizade" and banka_parola!="0554057235":
                        print("Parolaniz Yanlis!")
                        continue
                    elif banka_kullanici!="yusifhacizade" and banka_parola=="0554057235":
                        print("Kullanici Adiniz Yanlis...")
                        continue
                    else:
                        print("Lutfen Dogru Giris Yapin...")
                        break
                else:
                    print("Marka Bulunamadi...")
                    break
                
            
            
            
mainfunction()           
            


   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    