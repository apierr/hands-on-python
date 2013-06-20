# coding=utf-8
'''
Un file di nome iscritti.txt contiene i seguenti dati sugli studenti iscritti a un esame 
(una riga per ogni studente, con i diversi elementi separati da un carattere di spaziatura): 
nome, cognome, codice del corso di laurea e numero di matricola. 
Definire una funzione senza parametri, che acquisisca dal file i dati degli iscritti, 
chieda all’utente di inserire attraverso la tastiera l’esito dell’esame (un intero tra 18 e 31, 
dove 31 codifica il voto “trenta con lode”, oppure il valore 0 per indicare che lo studente era assente), 
e scriva in un nuovo file di nome “esiti.txt” i seguenti dati sui soli studenti che si sono presentati all’esame:
matricola, cognome, nome e voto (una riga distinta per ogni studente).
'''

file_iscritti = '06-iscritti.txt'
file_esiti = '06-esiti.txt'

def scrivi_esiti():
    f_iscritti = open(file_iscritti, 'r')
    f_esiti = open(file_esiti, 'w')
    iscritti = f_iscritti.readlines()
    for iscritto in iscritti:
        dati = iscritto.split()
        nome = dati[0]
        cognome = dati[1]
        matricola = dati[3]
        voto = raw_input('Inserisci il voto di ' + nome + ' ' + cognome + ': ')
        if (int(voto) > 0):
            f_esiti.write(matricola + ' ' + cognome + ' '+ nome + ' ' + voto + '\n')
    f_iscritti.close()
    f_esiti.close()

scrivi_esiti()
