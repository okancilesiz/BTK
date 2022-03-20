import os

secenek1=input("Yapmak istediğiniz işlem nedir? silme/açma")
if secenek1=="açma":
    ad = input("Açmak istediğiniz klasörün adını giriniz.")
    os.mkdir(ad)
elif secenek1=="silme":
    ad2=input("Silmek istediğiniz klasörün adını giriniz.")
    os.rmdir(ad2)