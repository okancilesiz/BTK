#Kullanıcıdan Sayı isteyin.. sayı girmediğinde tekrar iste
while True:
    try:
            sayi=int(input("Lütfen Bir sayı giriniz"))
            break
    except ValueError:
        print("Sayı sayı :)")
print("Karesi : ", sayi**2)
