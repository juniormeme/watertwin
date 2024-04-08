# pour l'affichage d'une fenetre specialisé dans l'affichage des scenarios 
# by MEME Junior
from pathlib import Path
from tkinter import PhotoImage
import tkinter as tk 
import ttkbootstrap as ttk 
from ttkbootstrap.constants import * 
from ttkbootstrap.scrolled import ScrolledText 
from ttkbootstrap.scrolled import ScrolledFrame
import matplotlib.pyplot as plt
from HydraulicModel import HydraulicModel
import random 

PATH = Path(__file__).parent/ 'assets'


class ScenarioVue : 
    """Pour le fichier scenario dans l'interface scenario monitoring"""
    def __init__(self, data) :
        self.window = ttk.Window()
        self.data  = data 
        self.window.title(self.data[0])
        self.window_width = 500
        self.window_height = 600
        self.window.geometry(f'{self.window_width}x{self.window_height}+600+50')
        self.placement()
        self.window.mainloop()      
    
    def placement(self) : 
        self.text = ScrolledText(self.window,font="Calibri 12",padding=5,autohide=True)
        self.text.pack(expand=True,fill='both',anchor='n')
        contenu = self.Remplir()
        for line in contenu :
            self.text.insert(END,line)
    
    def Remplir(self): 
        nom = f'scenario_folder/{self.data[1]}.scenario'
        file_path = Path(__file__).parent / nom
        with open(file_path,'r+') as file:
            contenu = file.readlines()
        return contenu 

class ScenarioTesting :
    
    def __init__(self) -> None:
        self.window = ttk.Window(themename="darkly")
        self.window.title("Scenario testing")
        self.window_width = 600
        self.window_height = 600
        self.window.geometry(f'{self.window_width}x{self.window_height}+500+50')
        # les icones 
        self.images = [
            PhotoImage(
                name='play', 
                file=PATH / 'icons8_play_22px.png'),
            PhotoImage(
                name='propriete', 
                file=PATH / 'icons8_window_settings_22px.png'),
            PhotoImage(
                name='3d', 
                file=PATH / 'icons8_3d_object_22px.png'),
            PhotoImage(
                name='plus', 
                file=PATH / 'icons8_plus_22px.png'),
            PhotoImage(
                name='minus', 
                file=PATH / 'icons8_minus_22px.png'),
        ]
        # variables des paramètres généraux
        self.pas = tk.StringVar()
        self.marge = tk.IntVar()
        self.k = tk.IntVar()  
        self.parametre = []
        self.initiaux = []
        self.action = []
        # les dispositions des elements graphiques 
        self.barre_haut = ttk.Frame(self.window,bootstyle="warning")
        self.barre_haut_center = ttk.Frame(self.barre_haut)
        self.barre_haut.pack(side="top",pady=3)
        self.barre_haut_center.pack(expand=True, anchor=CENTER)
        ttk.Button(self.barre_haut_center,text="Simulate",image='play',compound="left",command=self.affiche).pack(side="left",ipadx=15,ipady=3,padx=2)
        ttk.Button(self.barre_haut_center,text="3D inspection",image='3d',compound="left").pack(side="left",ipadx=5,ipady=3,padx=2)
        ttk.Button(self.barre_haut_center,text="proprieties",image='propriete',compound="left").pack(side="left",ipadx=5,ipady=3,padx=2)
        self.main = ttk.Frame(self.window)
        self.main.pack(side="top")
        # entre les panels de configuration et les buttons : configuration globale du système
        lateral = ttk.Frame(self.main)
        lateral.pack(side='top',pady=2)
        ttk.Label(lateral,text="Pas de discretisation :",font="Calibri 13").pack(side="left",padx=1,ipadx=10)
        ttk.Entry(lateral,textvariable=self.pas).pack(side="left",padx=1)
        lateral = ttk.Frame(self.main)
        lateral.pack(side='top',pady=2)
        ttk.Label(lateral,text="Points de discretisation :",font="Calibri 13").pack(side="left",ipadx=1)
        ttk.Entry(lateral,textvariable=self.k).pack(side="left",padx=1)
        lateral = ttk.Frame(self.main)
        lateral.pack(side='top',pady=2)
        ttk.Label(lateral,text="Marge d'affichage :",font="Calibri 13").pack(side="left",padx=1,ipadx=20)
        ttk.Entry(lateral,textvariable=self.marge).pack(side="left",padx=1)
        lateral = ttk.Frame(self.main)
        lateral.pack(side='top',pady=2)
        ttk.Label(lateral,text="Solveur :",font="Calibri 13").pack(side="left",padx=1,ipadx=75)
        ttk.Label(lateral,text="Euler Foward",font="Calibri 13 ").pack(side="left",padx=1)
        #-------------
        self.main = ScrolledFrame(self.window,autohide=True,width=580,height=550)
        self.main.pack(side="top")
        ControlPanel(self.main,"Selectionner les paramètres à observer",self.parametre,type="parametre").pack(side="top")
        ControlPanel(self.main,"Definir les conditionnements initiaux",self.initiaux,type="action",condition="initiale").pack(side="top")
        ControlPanel(self.main,"Spécifications des actions à simuler",self.action,type="action").pack(side="top")
        
        self.window.mainloop()      
    def affiche(self):
        self.model = HydraulicModel(name="Modèle")
        # on configure le modèle 
        self.model.pas = float(self.pas.get())
        self.model.marge = self.marge.get()
        # on met les conditionns initiaux
        for x in self.initiaux :
            if x[1] == "PMP01" or x[1] == "PMP02" :
                if x[2] == "Open" :
                    self.model.CommandePompe[x[1]] =  1
                else :
                    self.model.CommandePompe[x[1]] =  0
            else:
                if x[2] == "Open" :
                    self.model.CommandeVanne[x[1]] =  1
                else :
                    self.model.CommandeVanne[x[1]] =  0
        # on lance la simulation
        for i in range(self.k.get()) :
            for x in self.action :
                if float(x[3]) == float(self.pas.get())*i :
                    if x[1] == "PMP01" or x[1] == "PMP02" :
                        if x[2] == "Open" :
                            self.model.CommandePompe[x[1]] =  1
                        else :
                            self.model.CommandePompe[x[1]] =  0
                    else:
                        if x[2] == "Open" :
                            self.model.CommandeVanne[x[1]] =  1
                        else :
                            self.model.CommandeVanne[x[1]] =  0
            self.model.stepEulerForward(k=i)
        # on affiche les courbes 
        plt.figure()
        for x in self.parametre :
            plt.plot(self.model.Temps, self.model.Y[x[1]],f'C{random.randrange(10)}', label=x[1])
        
        plt.grid()
        plt.legend()
        plt.show()     

class ControlPanel(ttk.Frame):
    def __init__(self,boss,titre, data, type = "parametre", condition = "normal") :
        ttk.Frame.__init__(self, master=boss,width=120)
        self.data = data
        self.commandeNum = 0
        self.type = type 
        self.condition = condition
        self.haut= ttk.Frame(self)
        self.haut.pack(side='top',ipady=5)
        ttk.Label(self.haut,text=titre,font="Calibri 16").pack(padx=3,pady=2,ipadx=20,side="left")
        ttk.Button(self.haut,image="plus",command=self.ajouter).pack(padx=2,pady=2,side="left")
        ttk.Button(self.haut,image="minus",command=self.retrancher).pack(padx=2,pady=2,side="left")
        self.ajouter()
    def ajouter(self):
        self.commandeNum += 1
        self.data.append([self.commandeNum])
        #ttk.Frame(self,bootstyle="warning",height=50,width=400).pack(side="top",pady=1)
        #ActionPutter(self, self.commandeNum).pack(side="top",pady=1)
        #
        if self.type == "parametre" : 
            ParamsChooser(self,self.commandeNum,self.data).pack(side="top",pady=1)
        else :
            if self.condition == "normal" :
                ActionPutter(self, self.commandeNum,self.data,condition="normal").pack(side="top",pady=1)
            else :
                ActionPutter(self, self.commandeNum,self.data,condition="initiale").pack(side="top",pady=1)
        
    
    def retrancher(self):
        child_keys = list(self.children.keys())
        if len(child_keys) > 1:
            self.children[child_keys[-1]].destroy()
            self.commandeNum -= 1
            self.data.remove(self.data[-1])
        else :
            print("pas present")

class ActionPutter(ttk.Frame):
    
    def __init__(self,boss,num,data,condition="normal"):
        ttk.Frame.__init__(self, master=boss,width=300)
        ttk.Label(self,text=str(num)+")",font="Calibri 14").pack(side="left",ipady=5,padx=1)
        self.data = data
        self.i = num
        self.t = tk.StringVar()
        # on pack les menubuttons 
        self.actionneurMenu = ttk.Menubutton(self,image="play",compound='left',text="Actionneur",bootstyle="primary-outline")
        if condition == "initiale" : 
            self.actionneurMenu.pack(side='left',ipady=5,ipadx=45,padx=2)
        else :
            self.actionneurMenu.pack(side='left',ipady=5,padx=2)
        self.data[self.i-1].append(" ")
        # on cree ca liste perso 
        inside_menu = ttk.Menu(self.actionneurMenu)
        actionneur_var = tk.StringVar()
        # on rempli les elements dedans 
        for x in ["PMP01","PMP02","VLV01","VLV02","VLV03","VLV04","VLV05","VLV06","VLV07","VLV08","VLV09","VLV10"] :
            inside_menu.add_radiobutton(label=x,variable=actionneur_var,font="Calibri 14",command= lambda x=x : self.selectedActionneur(x))
        self.actionneurMenu['menu'] = inside_menu
        self.actionMenu = ttk.Menubutton(self,image="play",compound='left',text="Action")
        if condition == "initiale" :
            self.actionMenu.pack(side='left',ipady=5,ipadx=45,padx=2)
        else :
            self.actionMenu.pack(side='left',ipady=5,padx=2)
        self.data[self.i-1].append(" ")
        # on cree ca liste perso 
        inside_menu = ttk.Menu(self.actionMenu)
        action_var = tk.StringVar()
        # on rempli les elements dedans 
        for x in ["Open","Close"] :
            inside_menu.add_radiobutton(label=x,font="Calibri 14",variable=actionneur_var,command= lambda x=x : self.selectedAction(x))
        self.actionMenu['menu'] = inside_menu
        if condition == "normal" :
            ttk.Label(self,text="Temps(sec) :").pack(side='left',padx=1,ipady=5)
            self.temps = ttk.Entry(self,textvariable=self.t)
            self.temps.pack(side='left',ipady=5)
            self.data[self.i-1].append(" ")
            self.temps.bind('<FocusOut>',lambda event : self.selectedTime(event))
    def selectedTime(self,event):
        self.data[self.i-1][3] = self.t.get()
    def selectedActionneur(self,x): 
        self.actionneurMenu.config(text=x)
        self.data[self.i-1][1] = x
    def selectedAction(self,x): 
        self.actionMenu.config(text=x)
        if x == "Open": 
            self.actionMenu.config(bootstyle="success")
        else :
            self.actionMenu.config(bootstyle="danger")
        self.data[self.i-1][2] = x
class ParamsChooser(ttk.Frame):
    def __init__(self,boss,num,data):
        ttk.Frame.__init__(self, master=boss,width=300)
        ttk.Label(self,text=str(num)+")",font="Calibri 14").pack(side="left",ipady=5,padx=1)
        self.data = data
        self.i = num
        # on pack les menubuttons 
        self.paramMenu = ttk.Menubutton(self,image="play",compound='left',text="Paramètre",bootstyle="primary-outline")
        self.paramMenu.pack(side='left',ipady=5,ipadx=150,padx=2)
        # on cree ca liste perso 
        inside_menu = ttk.Menu(self.paramMenu)
        param_var = tk.StringVar()
        # on rempli les elements dedans 
        for x in ["PMP01","PMP02","CADC01","CAPC01","CADC02","CADC02","CADC03",
                  "CADC04","CAPC04","CADC05","CADC06","CANTK1","CANTK1","CAPTK1"
                  ,"CANTK2","CAPTK2","CADC07","CAPC07","CADC11","CAPC11","CADC10","CAPC10"] :
            inside_menu.add_radiobutton(label=x,variable=param_var,font="Calibri 14",command= lambda x=x : self.selected(x))
        self.paramMenu['menu'] = inside_menu
        self.data[self.i-1].append(" ")
    def selected(self,x): 
        self.paramMenu.config(text=x)
        self.data[self.i-1][1] = x
if __name__ == '__main__' : 
    ScenarioTesting()