"""Write a program that calculates the Body Mass Index (BMI) based on your height in cm and weight in kg. 
The user enters the data from the keyboard. 
Find the formula on the Internet for calculating BMI. 
Then, using your program, check that you have the correct weight. 
Sample result:

Enter your height in cm: ... Enter your weight in kg: ... BMI index: ... """
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
