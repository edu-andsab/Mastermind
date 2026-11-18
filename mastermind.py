import random
kod = []
for i in range(4):
    ran = random.randint(0,9)
    kod.append(ran)
print(kod)

while True:
    Gissad = []
    Gissa = input("Gissa talet ---> ")
    index = 0
    for i in Gissa:
         
        
        if int(i) in kod:
            if int(i) == kod[index]:
                Gissad.append("✔")
            else:
                Gissad.append("?")
        
        index += 1
    print(*Gissad)
print(kod)
            
            
    
    
        

    