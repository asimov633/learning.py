program kapitalbank;

uses crt;
var
  ad,soyad,kartnomresi:string;
  balans:real;
  sifre:integer;
  cvv:integer;
  secim1:integer;
  cekilecekpul:real;
  yuklenecekpul:real;
  kreditmiqdari:real;
  kreditayliq:integer;
  odenismeblegi:real;
begin
  writeln('KAPITAL BANKA XOS GELDINIZ...');
  writeln('SIFRE: ');readln(sifre);
  
  if sifre=2002 then begin
    clrscr;
    textcolor(green);
    ad:='YUSIF';
    soyad:='HAJIZADA';
    kartnomresi:='4169********8661';
    writeln('ADINIZ: ',ad);
    writeln('SOYADINIZ: ',soyad);
    writeln('KART NOMRESI: ',kartnomresi);
    
    writeln('CVV KODUNUZU GIRIN: ');readln(cvv);
    
    if cvv=958 then begin
      clrscr;
      balans:=645.55;
      writeln('BALANSINIZ: ',balans);
      writeln('------EMELIYATLAR------');
      writeln('1-PUL CEKMEK');
      writeln('2-BALANS ARTIRILMASI');
      writeln('3-KREDIT CEKILMESI');
      
      writeln('SECIM: ');readln(secim1);
      
      if secim1=1 then begin
        clrscr;
        balans:=645.55;
        writeln('BALANSINIZ: ',balans);
        writeln('1-MANAT KOMISSIYA ILE!!!');
        writeln('CEKILECEK PULUN MIQDARI: ');readln(cekilecekpul);
        
        if cekilecekpul>=645 then begin
          clrscr;
          textcolor(red);
          writeln('BALANS ASILDI!!!')
        end;
        
        if cekilecekpul<645 then begin
          clrscr;
          balans:=645.55;
          balans:=(balans-cekilecekpul)-1;
          writeln('PULUNUZ HAZIRLANIR...');
          writeln('QALAN BALANSINIZ: ',balans:0:2);
        end;
        
        
      end;
      
      if secim1=2 then begin
        clrscr;
        balans:=645.55;
        writeln('YUKLENECEK PUL: ');readln(yuklenecekpul);
        balans:=balans+yuklenecekpul;
        writeln('PUL YUKLENMESI BASA CATDI...');
        writeln('BALANS: ',balans);  
      end;
      
      if secim1=3 then begin
        clrscr;
        balans:=645.55;
        writeln('KREDIT MIQDARI: ');readln(kreditmiqdari);
        writeln('***************************************');
        writeln('KREDIT AYLIQ: ');readln(kreditayliq);
        writeln('HESABLANIR...');
        odenismeblegi:=kreditmiqdari/kreditayliq;
        writeln('AYLIQ ODEYECEYINIZ MEBLEG: ',odenismeblegi:0:2);
      end;
      
      if secim1>3 then begin
        clrscr;
        textcolor(red);
        writeln('XAIS OLUNUR SISTEME DUZGUN GIRIS EDIN!!!');
      end;
    end;
    
    if cvv<>958 then begin
      clrscr;
      textcolor(red);
      writeln('SISTEM CALISMADI!!!');
    end;
  end;
  
  if sifre<>2002 then begin
    clrscr;
    textcolor(red);
    writeln('SISTEM CALISMADI!!! YENIDEN YOXLAYIN...');
  end;
  
end.
