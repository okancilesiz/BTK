import random

while True:
    seviye = input("Bir Seviye Seçiniz:kolay/orta/zor")
    if seviye=="kolay":
        uret=random.randint(1,10)
        break
    elif seviye=="orta":
        uret=random.randint(1,50)
        break
    elif seviye=="zor":
        uret=random.randint(1,100)
        break
    else:
        print("Lütfen doğru seçim yapınız!")


while True:
    tahmin=int(input("Lütfen Bir tahminde bulununuz :"))
    if tahmin<uret:
        print("Sayınızı büyütün")
    elif tahmin>uret:
        print("Sayınızı Küçültün")
    else:
        print("Tebrikler Bildiniz")
        break