# La successione di Fibonacci e' una successione di numeri naturali
#  definita come segue: il primo elemento e' 0, il secondo e' 1,
#  e ogni elemento successivo e' pari alla somma dei due precedenti.

n = input("Quanti termini della successione di Fibonacci si vogliono mostrare? ")
a = 0 # primo termine
b = 1 # secondo termine
fib = 0 # termine generale della successione

print "Ecco i primi ", n, " termini:"

print a

if (n>1):
        print b

i = 2 # indice
while (i < n):
	i = i + 1 # incremento l'indice
	fib = a + b  # sommo l'n-esimo termine con quello che lo precede
	print fib # stampo il termine n+1-esimo
	a = b # aggiorno i valori dei termini
	b = fib # aggiorno i valori dei termini

