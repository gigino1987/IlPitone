# -*- coding: utf-8 -*-
'''Programmazione a oggetti, classi
Con la programmazione a oggetti possiamo utilizzare codice in maniera versatile, trattando il tutto appunto, come un oggetto
Questo esercizio mostra come utilizzare la classe scatola
Quando si crea un nuovo oggetto parliamo di istanza di un oggetto. In questo caso, il compito
di crearlo, una volta istanziata la classe, spetta al costruttore, ossia il metodo init tra doppi underscore.
In una classe abbiamo degli attributi e dei metodi. Gli attributi sono variabili di classe che contengono
le varie caratteristiche dell\'oggetto. Ad esempio, nella classe scatola gli attributi sono X, Y che si riferiscono alle dimensioni,
Stato che verifica se la scatola è aperta o chiusa e contenuto che raccoglie gli elementi della scatola.
I metodi sono funzioni che consentono di compiere azioni sull\'oggetto. Ad esempio, nella classe scatola la funzione apri consente di variare l'attributo Stato.
Attenzione, gli attributi in questo esempio sono pubblici, quindi alcuni di essi che,
di norma potrebbero essere variati solo dalla classe, possono esser cambiati anche da fuori generando errori.'''

class Scatola:
    Stato = 0
    contenuto = []
    def __init__(self, X=20, Y=20):
        self.X = X
        self.Y = Y
    
    def apri(self):
        if self.Stato == 1:
            return 'La scatola è già aperta'
        else:
            self.Stato = 1
            return 'Ho aperto la scatola'

    def chiudi(self):
        if self.Stato == 0:
            return 'La scatola è già chiusa'
        else:
            self.Stato = 0
            return 'Ho chiuso la scatola'

    def stato(self):
        if self.Stato == 0: return 'Chiusa'
        else: return 'Aperta'

    def aggiungi(self, elemento):
        if type(elemento) != type(''): return 'Accetto solo stringhe'
        elif self.Stato == 0: return 'Devi prima aprire la scatola per inserire oggetti'
        elif elemento in self.contenuto: return 'C\'è già'
        else:
            self.contenuto.append(elemento)
            return 'Ok'

    def rimuovi(self, elemento):
        if elemento not in self.contenuto: return 'Non puoi rimuoverlo se non c\'è'
        else:
            self.contenuto.remove(elemento)
            return 'Ok'

    def stampa(self):
        print('Dimensioni: %dx%d'%(self.X, self.Y))
        if self.Stato == 0:
            print('La scatola è chiusa')
        else:
            print('La scatola è aperta')
        if self.contenuto == []:
            print('La scatola è vuota')
        else:
            print('La scatola contiene: ')
            for c in self.contenuto:
                print(c)

if __name__ == '__main__':
    print('Non puoi avviare lo script direttamente,\ndevi importarlo nel tuo progetto!!!')