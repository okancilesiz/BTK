import os
try:
    os.mkdir("elma")
except FileExistsError:
    print("Girmiş olduğunuz isimde bir klasör mevcut. Lütfen Yeni bir isim giriniz.")