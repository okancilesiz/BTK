liste=[2,4,"a",87,"5b","51"]
#Soru : Yukarıdıaki listenin sadece int olanlarını try except ile
#Ekran yazdırınız.
for i in liste:
    try:
        print(int(i))
    except:
        pass