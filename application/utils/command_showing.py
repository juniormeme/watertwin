import tkinter as tk 
import ttkbootstrap as ttk 


class CommandShowing(ttk.Frame) : 
    
    def __init__(self,boss,tag) : 
        self.commande = tk.StringVar()
        self.commande.set("       Close")
        ttk.Frame.__init__(self, master=boss,borderwidth=1,relief='solid')
        ttk.Label(self,text="Tag : "+tag, font='Calibri 13 bold').pack(expand=True,ipady=3,fill='both')
        self.texte = ttk.Label(self,textvariable=self.commande, font='Calibri 18')
        self.texte.pack(expand=True,ipady=10,fill='both') 
    
    def setOff(self): 
        self.texte.configure(bootstyle='danger.Inverse.TLabel')
        self.commande.set("      Closed")
        
    def setOn(self):
        self.texte.configure(bootstyle='success.Inverse.TLabel')
        self.commande.set("       Open")