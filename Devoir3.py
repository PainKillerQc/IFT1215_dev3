tab = []

for i in range(10):
    tab.append(int(input("Valeur " + str(i+1) + ": ")))
    
valeurCherchee = int(input("Valeur cherchée : "))
    
index = -1

while (index + 10) >= 0:
    if valeurCherchee == tab[index]:
        break
    else:
        index -= 1
    
print(index)
