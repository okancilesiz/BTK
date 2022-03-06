# Uygulama : Kullanıcıdan ad,soyad ve telefon alarak bilgiler adlı listeye atayınız.
bilgiler=[]
ad=input("Lütfen adınızı giriniz:")
soyad=input("Lütfen Soyadınızı giriniz:")
ceptelefonu=input("Lütfen Cep telefonu numaranızı giriniz:")
print("Vermiş olduğunuz bilgiler için teşekkür ederiz.")
print(bilgiler)
bilgiler.append(ad)
bilgiler.append(soyad)
bilgiler.append(ceptelefonu)
bilgiler=[ad,soyad,ceptelefonu]
print("Adınız:" , bilgiler[0], "\nSoyad:", bilgiler[1], "\nTelefon Numaranız:", bilgiler[2])
#print("Soyad:" , bilgiler[1])
#print("Telefon numaranız:" , bilgiler[2])
#print(bilgiler)


