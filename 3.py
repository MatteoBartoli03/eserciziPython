# Variabili
x = "cane"
y = ["cane", "gatto", "gatto", "cane", "gatto"]

# Codice

a = y.count(x) # Ritorna il numero di volte in cui la stringa contenuta nella variabile x appare nella lista y 
print(a)

for i in range(len(y)): # questo for viene eseguito per un range() che ha come valore la lunghezza della lista y
	print(str(i) + " -> " + y[i]) # per concatenare le stringhe usiamo i "+", es: "ciao" + " mare" = "ciao mare"