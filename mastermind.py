import random
kod = []
Nummer = []
Gissningar = []
svar = []
for i in range(4):
    ran = random.randint(1,6)
    kod.append(ran)
print(kod)

#print(kod)
print("Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6. Du ska försöka gissa denna kods siffror på max 12 drag. Efter respektive gissning så kommer du att få en respons:☑ rätt,☒ fel. För de siffror som inte är med i koden ges ingen markering.")

def drag():
    print("Drag #		Drag 		Feedback \n ---------------------------------")
    nm = 0
    for i in range(12):
        
        if nm < len(Gissningar):
            print(i+1, "\t\t", Gissningar[i], "\t\t", svar[i], "\n")
        else:
            print(i+1,"\n")
        nm += 1 

while True:
    Gissad = []
    Gissa = input("Gissa talet ---> ")
    Gissningar.append(Gissa)
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
    svar.append(" ".join(Gissad))
    drag()

    print(*Gissad)
    
print(kod)
            
            
    
    
        

    