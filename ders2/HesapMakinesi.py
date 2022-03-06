ad=input("Lütfen İsminizi yazınız.")
print("Hoşgeldiniz:",ad)
print("Bugün sizin için yapacağımız işlem hesap makinesi.")
sayi1=int(input("Lütfen 1. Sayıyı giriniz."))
sayi2=int(input("Lütfen 2. Sayıyı Giriniz."))
islem=input("Lütfen Yapmak İstediğiniz İşlemi Giriniz.Çarpma-Toplama-Bölme-Çıkarma")
if islem == "Toplama" or "toplama":
    sonuc = sayi1 + sayi2
    print("Toplama işleminizin sonucu :",sonuc)
elif islem == "Çarpma" or "çarpma":
    sonuc = sayi1 * sayi2
    print("Çarpma İşleminizin Sonucu :",sonuc)
elif islem == "Bölme" or "bölme":
    sonuc = sayi1 / sayi2
    print("Bölme İşleminizin Sonucu :",sonuc)
elif islem == "Çıkarma" or "çıkarma":
    sonuc = sayi1 - sayi2
    print("Çıkarma İşleminizin Sonucu :",sonuc)
