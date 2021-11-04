PIN = "0805"

for i in range(3):
    
    wprowadzony_PIN = input("Wprowadź kod PIN: ")
    if wprowadzony_PIN == PIN:
        print("Wprowadzony PIN jest poprawny")
        break
    elif wprowadzony_PIN != PIN:
        print("Nieprawidłowo... ")
    
print("Przepraszamy, Twoja karta płatnicza została zablokowana.")

    