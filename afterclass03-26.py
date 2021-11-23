"""The payment card is secured with a four-digit PIN code (0805).
Write a program that checks if the PIN code entered in the payment terminal is correct.
The user has up to three possibilities for entering a PIN code. 
In case of three unsuccessful attempts, the card is blocked. 
Sample result:

Enter the PIN code: 2398 
Incorrect... 
Enter the PIN code: 0912 
Incorrect... 
Enter the PIN code: 7860 
Incorrect... 
Sorry, your payment card has been blocked."""
PIN = "0805"

for i in range(3):
    
    wprowadzony_PIN = input("Wprowadź kod PIN: ")
    if wprowadzony_PIN == PIN:
        print("Wprowadzony PIN jest poprawny")
        break
    elif wprowadzony_PIN != PIN:
        print("Nieprawidłowo... ")
    
print("Przepraszamy, Twoja karta płatnicza została zablokowana.")

    
