'''

1) Scrivere una funzione "scrivi_personaggi" che, acquisiti i dati relativi a dei personaggi famosi, li scriva in un file "personaggi.txt".
   Per ogni personaggio, in righe separate, dovranno essere indicati: nome (si assuma che ogni personaggio abbia un solo nome), cognome, sesso (M/F), età presunta.
 
2) Scrivere una funzione "leggi_personaggi" in grado di restituire un'opportuna struttura dei dati contenenti le informazioni su tutti i personaggi famosi.
   In altri termini, creare una lista in cui ogni elemento rappresenti un dizionario con i dati del personaggio.
 
3) Scrivere una funzione che esegua la seguente operazione: dato come parametro il valore del sesso (M/F), sia in grado di restituire un personaggio famoso a caso del sesso specificato (M/F).
 
4) Scrivere una funzione in grado di stampare un diagramma "a torta" con la frequenza di maschi e femmine.
   Utilizzare la funzione pie([numero_maschi, numero_femmine], labels=['maschi', 'femmine']).

'''

from random import choice
from pylab import *

def scrivi(nome_file):
	f = open(nome_file, 'w')
	while (True):
    		nome = raw_input("Nome del prossimo personaggio (Invio per terminare): ")
    		if (nome == ''):
        		break
    		cognome = raw_input("Cognome : ")
    		sesso = raw_input("Sesso (M/F): ")
    		eta = raw_input("Eta' presunta: ")
    		f.write(nome + ' ' + cognome + ' ' + sesso + ' ' + eta + '\n')
	f.close()

def leggi_file(nome_file):
	f = open(nome_file, 'r')
	personaggi = []

    	while (True):
		riga = f.readline()
		dati = riga.split(' ')
		if (riga == '' or riga == '\n'):
            		break
		personaggio = { 'nome': dati[0],
				'cognome': dati[1],
				'sesso': dati[2], 
				'eta': int(dati[3]) }

		personaggi = personaggi + [ personaggio ]

	f.close()
	return personaggi

def leggi_personaggio(personaggi, sesso):
	personaggi_selezionati = []
	for d in personaggi: 
		if d['sesso'] == sesso: 
			personaggi_selezionati = personaggi_selezionati + [d]
	return choice(personaggi_selezionati)

def stampa_torta(personaggi):
	frequenza_sesso = [0, 0] # assumo che il primo elemento della lista si riferisca ai maschi
	for d in personaggi:
		if d['sesso'] == 'M':
			frequenza_sesso[0] = frequenza_sesso[0] + 1 # assumendo che il primo elemento della lista si riferisca ai maschi
		else:
			frequenza_sesso[1] = frequenza_sesso[1] + 1
	pie(frequenza_sesso, labels = ['maschi', 'femmine'])
	show()
	
		
def main():
	nome_file = '/tmp/01-personaggi.txt'
	# scrivi(nome_file)
	personaggi = leggi_file(nome_file)
	print leggi_personaggio(personaggi, 'F')
	stampa_torta(personaggi)

main()
