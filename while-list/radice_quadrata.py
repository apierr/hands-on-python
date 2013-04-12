# Il calcolo della parte intera della radice quadrata di un numero
#  si puo' eseguire per tentativi, calcolando il quadrato dei numeri 
#  1, 2, 3, ..., fino a quando il risultato e' minore o uguale
#  al numero considerato.

n = input("insersci un numero positivo: ")
r = 1
while (r * r <= n):
	r = r + 1

print  "La parte intera della radice quadrata di", n, "e'", r - 1
