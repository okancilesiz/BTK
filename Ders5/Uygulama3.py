#kendisine gönderilen kullanıcı adı ve şifreyi kontrol ederek
#sonucunda true ya da false gönderen fonksiyonun pyhton kodu
#kullanıcıadı: admin , şifre:123456 olmalı
def kontrol(kullaniciadi,şifre):
    if kullaniciadi=="admin" and şifre=="123456":
        return True
    else:
        return False
kullaniciadi=input("Lütfen Kullanıcı adınızı giriniz: ")
şifre=input("Lütfen Şifrenizi Giriniz: ")
sonuc=kontrol(kullaniciadi,şifre)
print(sonuc)
if sonuc==True:
    print("Doğru Giriş")
else:
    print("Kullanıcı adı veya şifre hatalı")