# Variabili
x = 100
y = [2, 5, 4, 29] # Lista

# Codice
for i in y: # Per ogni elemento in y
	if i % 2 == 0:
		x -= i
	else:
		x += i

print(x)

for i in y:
	if i < 5:
		print('ciao')

	elif i >= 5:
		print("arrivederci")

	elif i == 5:
		print("bentornato")

	# Questi if - elif sono nidificati, quindi ne verrà eseguito solo UNO dei tre