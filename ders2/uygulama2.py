#kullanıcıdan 5 tane sayı isteyerek en büyük sayıyı listeye atayarak bulunuz.
sayi=input("1. Sayıyı giriniz")
sayi1=input("2. Sayıyı giriniz")
sayi2=input("3. Sayıyı giriniz")
sayi3=input("4. Sayıyı giriniz")
sayi4=input("5. Sayıyı giriniz")
sayilar=[]
sayilar.append(sayi)
sayilar.append(sayi1)
sayilar.append(sayi2)
sayilar.append(sayi3)
sayilar.append(sayi4)
sayilar.sort()
print("Girmiş olduğunuz en büyük sayı: ", sayilar[4])