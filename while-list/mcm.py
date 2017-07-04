# Minimo comune multiplo tra due numeri
# Un possibile algoritmo scandisce tutti i numeri tra max{m,n} e m*n,
#  arrestandosi non appena si trova un multiplo comune

m = input("Inserire il primo numero: ")
n = input("Inserire il secondo numero: ")

mcm = 0

if (m > n):
	mcm = m
else:
    mcm = n
while ((mcm % m != 0 or mcm % n != 0) and mcm < m * n):
	mcm = mcm + 1

print "Il mcm e': ", mcm 
