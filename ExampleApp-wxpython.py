# -*- coding: utf-8 -*-
# applicazione di prova con wx
# Mostra un numero casuale quando si preme il pulsante genera
# Questo esempio è un esercizio di programmazione con wxpython, ispirato dalla lettura del  libro "Capire wxpython" di Riccardo Polignieri dal quale sto studiando per realizzare GUI con questo motore grafico.
# In questo esempio sono presenti una classe per il frame principale, una ovviamente per wx.App ed una per la finestra di dialogo per la modifica dei valori

# importo i moduli necessari al funzionamento del programma
import wx, random

# Classe per l'istanziazione della finestra di dialogo per le modifiche dei parametri
# Definizione ed inserimento dei widjet
class ChangeIntervalDialog(wx.Dialog):  # La classe ChangeIntervalDialog eredita da wx.Dialog, quindi utilizza tutti gli attributi e i metodi di quella classe
    def __init__(self, *args, **kwargs):  # costruttore della classe
        # Istanziazione degli attributi di classe e di wx.Dialog e impostazione dei parametri su quest'ultimo
        # I valori iniziali sono stati istanziati all'interno della classe MainFrame e qui ci servono per la riassegnazione dei valori
        self.minVal = main.minVal
        self.maxVal = main.maxVal
        wx.Dialog.__init__(self, *args, **kwargs)
        # Aggiungiamo un pannello alla finestra di dialogo (nota, il primo parametro è riferito al genitore del widjet, quindi self è riferito alla finestra di dialogo padre). Il parametro è obbligatorio.
        panel = wx.Panel(self)
        # Aggiungiamo i widjet all'interno del pannello allo stesso modo di prima, ma anzicché self il genitore sarà panel
        # Ci servono due campi editazione (wx.TextCtrl), due etichette per identificare i campi editabili (wx.StaticText)
        # e due pulsanti (wx.Button). Il secondo parametro è l'ID del widjet, settiamo a -1 in modo tale da consentire a Python di allocare in automatico la posizione del widjet in memoria.
        # Il terzo parametro è il titolo o comunque il testo che deve comparire sui widjet.
        # I widjet vengono disposti nell'ordine in cui li si dichiari, quindi l'ordine è importante.
        self.minValLabel = wx.StaticText(panel, -1, "Valore minimo")
        self.minValEdit = wx.TextCtrl(panel, -1, value=str(main.minVal))
        self.maxValLabel = wx.StaticText(panel, -1, "Valore massimo")
        self.maxValEdit = wx.TextCtrl(panel, -1, value=str(main.maxVal))
        self.btnOk = wx.Button(panel, -1, "&Conferma")
        self.btnCancel = wx.Button(panel, -1, "&Annulla")
        # Una volta immessi i widjet questi andranno associati a degli eventi. Possiamo far ciò chiamando il metodo Bind su ciascuno di essi e passando come parametri
        # wx.EVT_EVENTO, ad esempio wx.EVT_BUTTON nel caso di un pulsante e il callback, cioè la funzione che verrà chiamata quando si verifica quell'evento, di solito il callback è self.OnXxxxx dove Xxxx indica il nome della funzione, ad esempio OnExit. Il callback non chiede parentesi dal momento che i parametri fissi sono self ed event.
        self.minValEdit.Bind(wx.EVT_TEXT, self.OnMinValueSet)
        self.maxValEdit.Bind(wx.EVT_TEXT, self.OnMaxValueSet)
        self.btnOk.Bind(wx.EVT_BUTTON, self.OnOk)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.OnCancel)

        # Per evitare che i widjet vengano sparpagliati nel frame a casaccio esistono i contenitori (sizer) che consentono di disporre automaticamente i widjet nello spazio qualora venga ridimensionata o ingrandita la finestra.
        # Qui viene inserito un contenitore principale (mainSizer), quindi ne vengono inseriti altri due (uno per i campi di testo e le etichette e e l'altro per i pulsanti).
        # Possiamo disporre i widjet in orizzontale (wx.HORIZONTAL) o in verticale (wx.VERTICAL).
        # Le ultime due istruzioni posizionano il sizer nel pannello del frame e ne stabiliscono il layout
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        buttonsSizer = wx.BoxSizer(wx.HORIZONTAL)
        editSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Tramite il metodo Add aggiungiamo i widjet ai rispettivi sizer
        # I valori immessi come parametri stabiliscono le distanze in pixel tra i vari elementi
        editSizer.Add(self.minValLabel, 10, wx.ALL, 10)
        editSizer.Add(self.minValEdit, 10, wx.ALL, 10)
        editSizer.Add(self.maxValLabel, 10, wx.ALL, 10)
        editSizer.Add(self.maxValEdit, 10, wx.ALL, 10)
        buttonsSizer.Add(self.btnOk, 10, wx.ALL, 10)
        buttonsSizer.Add(self.btnCancel, 10, wx.ALL, 10)
        mainSizer.Add(editSizer, 0, wx.ALL, 10, 10)
        mainSizer.Add(buttonsSizer, 0, wx.ALL, 10, 10)
        panel.SetSizer(mainSizer)
        panel.Layout()

    def OnMinValueSet(self, event):  # callback associato al widjet minValEdit
        # verifica se i caratteri immessi sono numeri, nel caso in cui non lo fossero viene sollevata un'eccezione e visualizzato un messaggio
        # Se invece è tutto a posto man mano che si scrivono i numeri l'attributo self.minVal viene aggiornato di volta in volta.
        try:
            self.minVal = int(self.minValEdit.GetValue())
        except ValueError:
            if not self.minValEdit.GetValue() == "": # Se l'eccezione non è rappresentata dal campo vuoto visualizza il messaggio altrimenti viene ignorato il blocco di istruzioni
                wx.MessageBox("Attenzione, non è un intero!")
                self.minValEdit.Clear()

    def OnMaxValueSet(self, event):  # callback associato al widjet maxValEdit
        # verifica se i caratteri immessi sono numeri, nel caso in cui non lo fossero viene sollevata un'eccezione e visualizzato un messaggio
        # Se invece è tutto a posto man mano che si scrivono i numeri l'attributo self.maxVal viene aggiornato di volta in volta.
        try:
            self.maxVal = int(self.maxValEdit.GetValue())
        except ValueError:
            if not self.maxValEdit.GetValue() == "":  # Se l'eccezione non è sollevata dal campo vuoto visualizza il messaggio altrimenti viene ignorato il blocco di istruzioni
                wx.MessageBox("Attenzione, non è un intero!")
                self.maxValEdit.Clear()

    def OnOk(self, evt):  # Callback associato al widjet btnOk
        # Se si verificano le condizioni sottostanti non viene dato il consenso al cambio
        # dei valori, altrimenti vengono settati i valori che erano stati utilizzati nella classe MainFrame e il dialogo viene chiuso.
        if self.minVal > self.maxVal:
            wx.MessageBox("Intervallo minimo maggiore dell'intervallo massimo, riprova.", "Errore")
        elif self.minVal == self.maxVal:
            wx.MessageBox("I valori non possono essere identici, riprova.", "Errore")
        else:
            main.minVal, main.maxVal = self.minVal, self.maxVal
            self.Destroy()

    def OnCancel(self, evt):  # Callback associato al widjet btnCancel
        # Chiude il dialogo distruggendo l'oggetto
        self.Destroy()

# definizione della classe della finestra principale
# e inserimento dei widget
class MainFrame(wx.Frame):  # La classe MainFrame eredita i metodi e gli attributi di wx.Frame
    def __init__(self, parent=None, *args, **kwargs):  # Costruttore
        # Attributi di classe per i valori minimo e massimo
        self.minVal = 1
        self.maxVal = 100
        wx.Frame.__init__(self, parent, *args, **kwargs)  # Istanziazione del frame
        # Inserimento del panel e dei widjet
        panel1 = wx.Panel(self)
        self.label1 = wx.TextCtrl(panel1, -1, style=wx.TE_READONLY|wx.TE_MULTILINE)
        self.button1 = wx.Button(panel1, -1, "&Genera")
        self.button2 = wx.Button(panel1, -1, "&Cambia")
        self.button3 = wx.Button(panel1, -1, "   E&sci")
        # Associazione dei widjet ai rispettivi callback tramite il metodo Bind sugli stessi
        self.button1.Bind(wx.EVT_BUTTON, self.OnGenerate)
        self.button2.Bind(wx.EVT_BUTTON, self.OnChangeInterval)
        self.button3.Bind(wx.EVT_BUTTON, self.OnExit)
        # Aggiunta di un contenitore (sizer) per la disposizione ottimizzata dei widjet sul pannello
        sizer = wx.BoxSizer(wx.VERTICAL)
        # Aggiungiamo i widjet in maniera compatta al pannello tramite il ciclo for
        # dichiariamo una tupla contenente ciascun widjet e col ciclo for li aggiungiamo mediante il metodo Add del sizer.
        widgets = (self.label1, self.button1, self.button2, self.button3)
        for i in widgets:
            sizer.Add(i, 10, wx.ALL, 10)
            # Settiamo il sizer sul pannello e adattiamo il layout
        panel1.SetSizer(sizer)
        panel1.Layout()

    def OnGenerate(self, event):   # Callback associato al widjet button1 
        # Setta l'etichetta del widjet con un numero casuale intero compreso nell'intervallo impostato
        self.label1.SetLabel(str(random.randint(self.minVal, self.maxVal)))

    def OnChangeInterval(self, event):  # Callback associato al widjet button2
        # istanzia la finestra di dialogo per la modifica dei parametri e la mostra tramite il metodo Show
        dialog = ChangeIntervalDialog(parent=None, title="Cambia intervalli")
        dialog.Show()

    def OnExit(self, event): # Callback associato al widjet button3
        # Viene mostrato un messaggio e poi l'applicazione viene chiusa mediante il metodo Destroy
        wx.MessageBox("Grazie per aver utilizzato l'applicazione!", "Arrivederci")
        self.Destroy()

# L'istanziazione di wx.App è importantissima altrimenti la GUI non partirà
# In questo esempio abbiamo istanziato wx.App mediante una classe che consente
# il settaggio dei parametri iniziali e all'uscita mostra un messaggio
# dopo di che viene chiuso tutto.

class MyApp(wx.App):
    def OnInit(self):  # qui si possono inserire le istruzioni che servono all'inizializzazione del programma
        wx.MessageBox("Prima mia applicazione grafica funzionante con wxpython.", "Generatore di numeri casuali")  # messaggio di benvenuto
        return True  # il valore di ritorno deve essere esplicito, True significa che tutto va bene e l'applicazione può avviarsi, False interrompe immediatamente lo svolgimento del programma.

    def OnExit(self):  # Qui si possono inserire le istruzioni per il programma quando viene chiuso
        wx.MessageBox("Grazie per aver utilizzato l'applicazione!", "Arrivederci")  # messaggio di chiusura programma
        self.Destroy()   # chiusura del programma vera e propria con la distruzione dell'istanza di wx.App
        return False

# Istruzioni per l'avvio del programma
# il blocco if __name__ == "__main__" ci consente di effettuare operazioni solo se lo script viene caricato direttamente e non importato come modulo

if __name__ == "__main__":
    # Istanziazione di wx.App, MainFrame e avvio della GUI tramite i metodi MainLoop su app e Show su MainFrame
    app = MyApp(0)  # Lo 0 significa "mostra l'output dei messaggi di Python nella console e non su wx.App".
    main = MainFrame(title="Genera numeri casuali")
    main.Show()
    app.MainLoop()
