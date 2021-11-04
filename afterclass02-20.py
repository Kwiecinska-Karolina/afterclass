height = int(input("Podaj swój wzrost w cm: "))
weight = int(input("Podaj swoją wagę w kg: "))

BMI= weight/(height/100)**2

print(BMI)
if BMI<18.5:
    print("Niedowaga")
elif BMI>=18.5 and BMI<25:
    print("Norma")
elif BMI>=25 and BMI<30:
    print("Nadwaga")
elif BMI>=30 :
    print("Otyłość")