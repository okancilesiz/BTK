# #Kullanıcıadı ve şifre alınız.. Kullanıcı adı olarak "admin" şifre olarak
# 123456 girilince "Sisteme başarıyla giriş yaptınız" yazsın..
# yanlış girildikçe "kullanıcıadı veya şifre hatalı" yazıp
# tekrar kullanıcıadı ve şifre sorsun!
while True:
    kullaniciadi = input("Kullanıcı adınız:")
    sifre = input("Şifreniz :")
    if kullaniciadi=="admin" and sifre=="123456":
        break
    else:
        print("Kullanıcı adı veya parola hatalı")
print("Sisteme başarıyla giriş yaptınız..")






