#INPUT
x = 100
y = [2, 5, 4, 29]

#CODICE
for i in y:
	if i%2 == 0:
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