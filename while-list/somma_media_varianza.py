# calcolo di somma, media artimetica e varianza di un insieme di dieci numeri 

print "Inserire una lista di dieci numeri:"
lista = input()
lunghezza_lista = 10

somma = 0.0
i = 0
while (i < lunghezza_lista):
    	somma = somma + lista[i]
    	i = i + 1
    	
media = somma / lunghezza_lista

print "La somma e': ", somma
print "La media e': ", media

varianza = 0.0
i = 0
while (i < lunghezza_lista):
	scarto = (lista[i] - media)
	varianza = varianza + scarto * scarto 
	i = i + 1

varianza = varianza / lunghezza_lista
 
print "La varianza e':", varianza
