"""Write a program that creates a multiplication table in the range 1 to 10 
for any number entered by the user. 
Sample result:

Enter number:6 
6 x 1 = 6 
6 x 2 = 12 
6 x 3 = 18 
6 x 4 = 24 
6 x 5 = 30 
6 x 6 = 36 
6 x 7 = 42 
6 x 8 = 48 
6 x 9 = 54 
6 x 10 = 60"""
number = int(input("Podaj liczbę: "))

tab= [1,2,3,4,5,6,7,8,9,10]


print(" \n ", number, " x ", tab[0], "=", number * tab[0]," \n ",
       number, " x ", tab[1], "=", number * tab[1]," \n ",
       number, " x ", tab[2], "=", number * tab[2]," \n ",
       number, " x ", tab[3], "=", number * tab[3]," \n ",
       number, " x ", tab[4], "=", number * tab[4]," \n ",
       number, " x ", tab[5], "=", number * tab[5]," \n ",
       number, " x ", tab[6], "=", number * tab[6]," \n ",
       number, " x ", tab[7], "=", number * tab[7]," \n ",
       number, " x ", tab[8], "=", number * tab[8]," \n ",
       number, " x ", tab[9], "=", number * tab[9]," \n ")
