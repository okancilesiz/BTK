#Kullanıcıdan harf girmesini isteyiniz. e girerse erkek k girerse kadın ekrana yazdırınız

harf=str(input("Lütfen e/k harflerinden birini giriniz."))
if harf == "e" or "E":
    print("Erkek")
elif cinsiyet=="k" or "K": #2. Veya daha fazla şart olursa elif kullanılır
    print("Kadın")
else:
    print("Lütfen E veya K Giriniz!")
print("Hoşcakalın...")