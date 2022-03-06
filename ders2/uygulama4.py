#Kullanıcıdan not ortalamalarını isteyin ve takdir ya da teşekkür aldığını belirtin
notortalama=float(input("Lütfen Not Ortlamasını giriniz."))
if notortalama >= 85:
    print("Bravo KANKS... Taktir belgesi aldın")
elif notortalama >= 70:
    print("Fena sayılmaz... Teşekkür belgesi aldın")
elif notortalama <=50:
    print("Eyvah eyvah...")
else: print("Lütfen Geçerli bir not ortalaması gir.")