#INPUT
x = 14
y = 20

#DATO INIZIALE
somma = 0

#CODICE
for i in range(x):
	if i%2 == 0:
		somma += i
print(somma)

if y == 20:
	print("bicicletta")

if y < 100:
	print("moto")

if 0 < y < 20:
	print("macchina")