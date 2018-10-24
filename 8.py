# Variabili
x = 9

# Codice
def controlla(numero):
  if x % 3 == 0:
    return "x è un numero divisibile per tre" # La funzione ritorna una stringa
  else:
    return "x non è divisibile per tre"

risultato = controlla(x) # risultato assume il valore di ritorno della funzione
print(risultato)