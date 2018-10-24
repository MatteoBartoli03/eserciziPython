#INPUT
x = "cane"
y = ["cane", "gatto", "gatto", "cane", "gatto"]

#CODICE

a = y.count(x)
print(a)

for i in range(len(y)):
	print(str(i) + " -> " + y[i])