""" Write a program that calculates a dog's age in dog’s years.
For the first two years, a dog's life is equal to 10.5 human years. 
After that, each dog year is equal to 4 human years. Sample result:

Enter the dog's age in human years: 15 The dog's age in dog’s years is 73 years."""
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
    
