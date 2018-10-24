# Variabili
x = 14
y = 20

# Inizializziamo la Somma
somma = 0

# Codice
for i in range(x): # Questo for viene eseguito x volte (14)
	if i % 2 == 0:   # se il resto di i / 2 da 0
		somma += i     # stessa cosa di scrivere somma = somma + 1, si incrementa il valore di uno
print(somma)       # mandiamo in output la somma

if y == 20: # se y è uguale a 20
	print("bicicletta")

if y < 100: # se y è minore di 100
	print("moto")

if 0 < y < 20: # se y è maggiore di 0 e minore di 20
	print("macchina")

# Nota che questi if non sono nidificati ma sono uno sotto l'altro sulla stessa colonna,
# quindi verranno eseguiti TUTTI E TRE