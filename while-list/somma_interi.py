# calcolare la somma dei primi N interi

print "Inserire un numero intero:"

n = input()

somma = 0
i = 0

while (i < n + 1):
	somma = somma + i
	i = i + 1

print "La somma dei primi ", n, " numeri interi e': ", somma
