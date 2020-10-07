import sqlite3
import random
import datetime
import time



connect=sqlite3.connect("dersler.db")

cursor=connect.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1 (zaman REAL,tarih TEXT,anahtarkelime TEXT,deger REAL)")

def rastgeledegerekle():
    zaman=time.time()
    tarih=str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d $H:$M:$S'))
    anahtarkelime="Pyhton SQLITE3"
    deger=random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo1 (zaman,tarih,anahtarkelime,deger) VALUES(?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
    connect.commit()

tabloolustur()

i=0
while i<10:
    rastgeledegerekle()
    time.sleep(1)
    i=i+1

connect.close()

























