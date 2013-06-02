'''
Scrivere un programma che gestisca una piccola biblioteca e che fornisca le seguenti funzionalita':

1) 
Aggiunta di nuovi libri:
questa funzionalita' prende come input l'autore, il titolo e il prezzo di un libro e li scrive in un file
(dato che il cognome dell'autore e/o il titolo del libro possono contenere spazi, 
si consiglia - durante la scrittura - di separare i vari valori (autore, libro, prezzo) con un carattere non-alfanumerico come "/")

2)
Elenco di tutti i libri:
questa funzionalita' stampa il titolo e l'autore di tutti i libri presenti nella biblioteca
(leggere dal file tutti i dati relativi ai libri della biblioteca);

3)
Numero di libri di un autore:
questa funzionalita' prende come input un autore e restituisce il numero di libri dell'autore che si trovano nella biblioteca;

4)
Lista dei libri della biblioteca:
Si rappresenti ciascun libro con un dizionario di tre chiavi: titolo, autore e prezzo; 
la biblioteca e' semplicemente una lista di libri.

5)
Libro piu' costoso:
questa funzionalita' restituisce il libro piu' costoso che si trova nella biblioteca
(per questa funzionalita' si usi la struttura dati "lista libri biblioteca" calcolata nel punto precedente)

'''

nome_file_biblioteca = '/tmp/02-biblioteca.txt'

def aggiungi_libro():
    vuoi_continuare = 'si'
    f = open(nome_file_biblioteca, 'a')
    while (vuoi_continuare == 'si'):
        autore = raw_input('Insersci autore: ' )
        titolo = raw_input('Inserisci titolo: ')
        prezzo = raw_input('Inserisci il prezzo: ')
        f.write(autore + '/' + titolo + '/' + prezzo + '\n')
        vuoi_continuare = raw_input('Voui continuare (si/no)? ')
    f.close()
	
def elenco_libri():
    f = open(nome_file_biblioteca, 'r')
    righe = f.readlines()
    f.close()
    for riga in righe:
	dati = riga.split('/')
	for dato in dati:
		print dato

def numero_libri_per_autore():
    numero_libri = 0
    f = open(nome_file_biblioteca, 'r')
    righe = f.readlines()
    f.close()
    autore = raw_input('Inserisci un autore di libri: ')
    for riga in righe:
        dati = riga.split('/')
        if (dati[0] == autore):
            numero_libri = numero_libri +1
    print 'Ci sono ' + str(numero_libri) + ' libri di ' + autore 

def lista_biblioteca():
    lista = []
    f = open(nome_file_biblioteca, 'r')
    righe = f.readlines()
    f.close()
    for riga in righe:
       dati = riga.split('/')
       libro = { 'autore' : dati[0], 'titolo': dati[1], 'prezzo': float(dati[2]) }
       lista = lista + [libro]
    return lista

def libro_piu_caro(lista_libri): 
    prezzo_max = 0
    titolo_libro_piu_caro = ''
    for d in lista_libri:
	if (d['prezzo'] > prezzo_max ):
	   prezzo_max = d['prezzo']
           titolo_libro_piu_caro = d['titolo']
    print 'Il libro piu\' caro della biblioteca e\': ' + d['titolo']

#aggiungi_libro()
elenco_libri()
#numero_libri_per_autore()
lista_libri =  lista_biblioteca()
print lista_libri
libro_piu_caro(lista_libri)
