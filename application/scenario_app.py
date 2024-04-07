""" Fichier : scenario_app.py 
    Auteur : MEME ANDERMON JUNIOR 
    description : C'est dans ce fichier qu'est codé toute la partie visuel 
    et logique qui vont gerer les scenarios qui seront enregistrés par 
    l'opérateur lors de son interaction avec le DT 
"""
import tkinter as tk 
import ttkbootstrap as ttk 
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
from scenario_monitoring import ScenarioVue
from scenario_monitoring import ScenarioTesting
from ttkbootstrap import utility
import sys,threading,subprocess
class ScenarioApp(ttk.Frame):
    
    def __init__(self,boss):
        """le constructeur de base"""
        ttk.Frame.__init__(self, master=boss)
        self.scenario_running = False 
        # Le premier truc est un label frame 
        self.haut = ttk.Frame(self)
        self.haut.pack(anchor='n')
        # Le deuxième truc est la table ou il y a bcq des trucs 
        self.centre = ttk.Frame(self)
        self.centre.pack(anchor='n',ipady=80,ipadx=280)
        self.placer_en_haut()
        self.placer_au_centre()
    def placer_en_haut(self):
        # le bouton de lancer hors temps reel, il span toute la ligne du dessus la et je diminue les dimensions 
        ttk.Button(self.haut,image='play',compound="left",bootstyle="success-outline",
                   text="Tester un scenario",command=self.onClickScenario).grid(row=0,columnspan=3,pady=5,padx=20,ipadx=3,ipady=5,sticky="w")
        # Monitoring des nombres de manière globale
        one = ttk.Frame(self.haut,bootstyle='primary')
        one_frame  = ttk.Frame(one,bootstyle='primary')
        ttk.Label(one_frame,text="Nombre de scenario",font="Consolas 14 bold",bootstyle="light",background='#375A7F').pack(side="top")
        ttk.Label(one_frame,text="12",font="Consolas 16 bold",bootstyle="light",background='#375A7F').pack(side='top')
        one_frame.pack(anchor='center',expand=True)
        one.grid(column=0,row=1,ipadx=30,ipady=30,padx=20,pady=10,sticky='nsew')
        one = ttk.Frame(self.haut,bootstyle='warning')
        one_frame  = ttk.Frame(one,bootstyle='warning')
        ttk.Label(one_frame,text="Nombre de scenario",font="Consolas 14 bold",bootstyle="light",background='#F39C12').pack(side="top")
        ttk.Label(one_frame,text="12",font="Consolas 16 bold",bootstyle="light",background='#F39C12').pack(side='top')
        one_frame.pack(anchor='center',expand=True)
        one.grid(column=1,row=1,ipadx=30,ipady=30,padx=20,pady=10,sticky='nsew')
        one = ttk.Frame(self.haut,bootstyle='danger')
        one_frame  = ttk.Frame(one,bootstyle='danger')
        ttk.Label(one_frame,text="Nombre de scenario",font="Consolas 14",bootstyle="light",background='#E74C3C').pack(side="top")
        ttk.Label(one_frame,text="12",font="Consolas 16 bold",bootstyle="light",background='#E74C3C').pack(side='top')
        one_frame.pack(anchor='center',expand=True)
        one.grid(column=2,row=1,ipadx=30,ipady=30,padx=20,pady=10,sticky='nsew')
        # L'entry pour la recherche d'un scenarios 
        self.searchFrame = ttk.Frame(self.haut,width=201, height=20)
        self.searchFrame.grid(sticky='nsew',row=2, columnspan=3, padx=22,pady=2)
        self.placer_au_search()
    def placer_au_centre(self):
        self.resultview = ttk.Treeview(
            master=self.centre, 
            bootstyle=PRIMARY, 
            columns=[0, 1, 2, 3],
            show=HEADINGS
        )
        self.resultview.pack(fill='y', expand=YES, pady=5)
        #style = style  = ttk.Style()
        #style.configure("Treeview",font="Calibri 12")
        # On Configure les colonnes et leurs enfants 
        self.resultview.heading(0, text='Identifiant', anchor=W)
        self.resultview.heading(1, text='Nom du scenario', anchor=W)
        self.resultview.heading(2, text='Date de creation', anchor=W)
        self.resultview.heading(3, text='Emplacement du fichier', anchor=W)
        self.resultview.column(
            column=0, 
            anchor=W, 
            width=utility.scale_size(self, 101), 
            stretch=False
        )
        self.resultview.column(
            column=1, 
            anchor=W, 
            width=utility.scale_size(self, 201), 
            stretch=False
        )
        self.resultview.column(
            column=2, 
            anchor=W, 
            width=utility.scale_size(self, 151), 
            stretch=False
        )
        self.resultview.column(
            column=3, 
            anchor=W, 
            
            width=utility.scale_size(self, 351), 
            stretch=False
        )
        # pour inserer les valeurs 
        valeur = [
            ["Commutation Vanne 1","20-03-2024","/scenario_folder/scene1.scenario"],
            ["Remplissage tank 1","20-03-2024","/scenario_folder/scene2.scenario"],
            ["Fermeture pompes","21-03-2024","/scenario_folder/scene3.scenario"],
            ["observation des pressions","23-03-2024","/scenario_folder/scene4.scenario"]
        ]
        for i in range(len(valeur)): 
            iid = self.resultview.insert(
                    parent='', 
                    index=END, 
                    values=(str(i+1),valeur[i][0],valeur[i][1],valeur[i][2])
                )
            self.resultview.selection_set(iid)
            self.resultview.see(iid)
        # Les ecoutes 
        self.resultview.bind("<Button-1>",self.onClicItem) 
        
    def onClicItem(self,event): 
        item_id = self.resultview.identify_row(event.y)
        values = self.resultview.item(item_id)["values"]
        self.resultview.selection_set(item_id)
        self.resultview.see(item_id)
        ScenarioVue(values)
    
    def placer_au_search(self):
        ttk.Label(self.searchFrame,text="Chercher un scenario", font="Calibri 12").pack(side=LEFT,padx=10)
        ttk.Entry(self.searchFrame,font="Calibri 12").pack(side=LEFT,expand=TRUE,fill=X)
        ttk.Button(self.searchFrame,image="search").pack(side=LEFT,padx=5,ipady=2,ipadx=2)
           
    def onClickScenario(self) :
        #ScenarioTesting()
        threading.Thread(target=self.execute_script_with_sys).start()
    
    def execute_script_with_sys(self):
        sys.executable
        subprocess.call([sys.executable,'../Water Twin by MEME/application/scenario_monitoring.py'])
if __name__ == '__main__' : 
    app = ttk.Window()
    ScenarioApp(app).pack()
    app.mainloop()


