age = float(input("Podaj wiek psa: "))
rok = 10.5
dwa_lata = rok * 2
następne_lata = dwa_lata + 4 * (age - 2)

if age == 1:
    print("Wiek psa na psie lata: ",rok)
elif age == 2 :
    print("Wiek psa na psie lata: ",dwa_lata)
elif age > 2:
    print("Wiek psa na psie lata: ",następne_lata)
    