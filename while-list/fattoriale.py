# Il fattoriale di un numero naturale e' definito come:
#  n! = n * (n-1) * (n-2) * ... * 1
# Puo' essere calcolato iterativamente, eseguendo una moltiplicazione
#  alla volta, e memorizzando in una variabile il prodotto parziale. 

print "Scrivere un numero naturale: "
x = input()

if x < 2:
	fatt = 1
else:
	i = x - 1
	while i > 0:
		x = x * i
		i = i - 1
	fatt = x

print "Il fattoriale e'", fatt


# Una possibile soluzione alternativa:

# print "Scrivere un numero naturale: "
# x = input()

# fatt = 1
# i = 2
# while (i <= fatt):
#        fatt = fatt * i
#        i = i + 1

# print "Il fattoriale di", x, "e'", fatt
