kwota = int(input())
  
ilość_monet_5 = kwota//5
print("Ilość 5 zł: ",ilość_monet_5)

reszta= kwota-ilość_monet_5*5

ilość_monet_2 = reszta//2
reszta_2= reszta-ilość_monet_2*2
ilość_monet_1=reszta_2//1
ilość_monet_11=reszta//1

if reszta // 2  and reszta % 1 == 0:
    print("Ilość 2 zł: ",ilość_monet_2)
    print("Ilość 1 zł: ", ilość_monet_1)

elif reszta % 2 == 0:
    print("Ilość 2 zł: ",ilość_monet_2)

elif reszta % 1 == 0:
    print("Ilość 1 zł: ", ilość_monet_11)
