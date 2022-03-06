Liste=[] #Boş bir liste tanımlar.
Liste=["Elma" , "Armut" , 20] # artık listenin elemanları değişti!
sayilar=[15,19,2,3,8,25,6]
isimler=["Ali","Veli","Ahmet","Zehra","Hatice"]
gunler=["Pazartesi","Salı","Çarşamba"] # Haftanın ilk üç günü listelendi
print(gunler)
print("0. indeksdeki eleman",gunler[0])
print(gunler[1])  # ctrl d satırı kopyalar , ctrl y satırı siler
print(gunler[2])
gunler.append("Perşembe") # append: komutu yeni eleman ekler !!
print(gunler[3])
print("Eleman Sayısı :" , len(gunler)) #len: listenin eleman sayısını verir!
gunler.pop() #Hiçbir şey yazılmadıgında listenin son elemanını çıkarır.
print(gunler)
print("Eleman Sayısı :" , len(gunler)) #len: listenin eleman sayısını verir!
gunler.pop(0)
print(gunler)
print("Eleman Sayısı :" , len(gunler)) #len: listenin eleman sayısını verir!
print(sayilar)
sayilar.sort() # Varsıyalan (Default) olarak küçükten büyüğe doğru
print(sayilar)
sayilar.sort(reverse=True) # Büyükten küçüğe doğru sıralar
print(sayilar)
isimler.sort()
print(isimler)
isimler.sort(reverse=True)
print(isimler)