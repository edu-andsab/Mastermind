import random
kod = []
Nummer = []

for i in range(4):
    ran = random.randint(1,6)
    kod.append(ran)
print(kod)
print("Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6. Du ska försöka gissa denna kods siffror på max 12 drag. Efter respektive gissning så kommer du att få en respons:☑ rätt,☒ fel. För de siffror som inte är med i koden ges ingen markering.")
while True:
    Gissad = []
    Gissa = input("Gissa talet ---> ")
    index = 0
    Nummer = kod.copy()
    for i in Gissa:
         
        
        if int(i) in kod:
            if int(i) == kod[index]:
                if int(i) in Nummer:
                    Gissad.append("✔")
                    Nummer.remove(int(i))
            else:
                if int(i) in Nummer:
                    Gissad.append("?")
                    Nummer.remove(int(i))

            
        index += 1
    print(*Gissad)
    
print(kod)
            
            
    
    
        

    