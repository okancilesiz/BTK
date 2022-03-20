try:
    sayi1=int(input("Lütfen bir sayı Giriniz:"))
    sayi2=int(input("Lütfen bir sayı Giriniz:"))
    print("Bölüm" , sayi1/sayi2)
except ValueError:
    print("Lütfen Sayı gir! Harf Girme!")
except ZeroDivisionError:
    print("0'a Bölme Yapılamaz!")
except SyntaxError:
    print("Yazım Hatan var!")
except NameError:
    print("Böyle Bir değişken yok")
except:
    print("Genel bir hata oluştu")
print("Program buradan çalışmasına devam eder...")