# coding=utf-8
'''
Si assuma che un file di testo contenga un certo numero di righe, 
ciascuna corrispondente a una voce di menu di un dato programma. 
Definire una funzione che, dato il nome del file, 
stampi sullo schermo le voci del menu, 
ciascuna preceduta dal proprio numero d’ordine (a partire da 1), 
e chieda all'utente di scegliere una delle voci, 
inserendo attraverso la tastiera il numero corrispondente. 
Se il valore inserito non corrispondesse a nessuna voce del menu, 
si dovra` stampare sullo schermo un messaggio opportuno e chiedere all’utente di ripetere la scelta, 
mostrando di nuovo le voci del menu. 
Non appena l’utente inserisce un valore corretto, 
la funzione dovra` terminare restituendo tale valore. 
La stampa delle voci del menu dovra` essere eseguita da una seconda funzione.
'''

nome_file = '04.txt'

def stampa_menu():
    f = open(nome_file, 'r')
    voci_menu = f.readlines()
    i = 0
    for voce_menu in voci_menu:
        i = i + 1
        print i, voce_menu
    f.close()
    
def stampa_valore():
    numero = input('inserisci numero: ')
    f = open(nome_file, 'r')
    voci_menu = f.readlines()
    if ( numero <= len(voci_menu)):
        print voci_menu[numero - 1]
    else:
        print "Hai sbagliato!\n"
        stampa_menu()
        stampa_valore()
    f.close()

stampa_menu()
stampa_valore()
