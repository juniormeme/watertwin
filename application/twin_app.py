""" Fichier : twin_app.py 
    Auteur : MEME ANDERMON JUNIOR 
    description : C'est dansce fichier que toute la programmation visuel 
    pour le monitoring et le controle du jumeau numérique se fait
"""
import tkinter as tk 
import ttkbootstrap as ttk 
from random import randrange
from ttkbootstrap.scrolled import ScrolledFrame
from twin_app_monitoring import CommandMonitoring, ModelMonitoring
from utils.command_showing import CommandShowing
import communication as com
from HydraulicModel import *
import psutil
import sys 
import threading
import subprocess

class TwinApp(ttk.Frame):
    
    def __init__(self,boss):
        ttk.Frame.__init__(self)
        # Les variables de manipulation du DT
        self.compteur = 0 
        self.model = HydraulicModel(name="Test mode")
        self.model.marge = 10000
        self.model.pas = 0.1
        #on allume les pompes
        self.model.CommandePompe['PMP01'] = 1
        self.model.CommandePompe['PMP02'] = 1
        # les variables de manipulation des widgets venant du master
        self.gauges = []
        self.monitoring_time = tk.StringVar()
        self.monitoring_time.set("00:00:00")
        self.real_time = tk.StringVar()
        self.real_time.set("00:00:00")
        self.running = ['demarrer','arreter']
        self.running3D = True
        self.runningtext = tk.StringVar()
        self.runningtext.set(self.running[0])
        # le classement de ces widgets pour le panel de generale 
        self.general_monitoring()
        self.simple_showing('Simulation time',self.monitoring_time).grid(row=0,column=0,sticky='nsew',padx=4,pady=5,ipadx=60)
        self.simple_showing('Real time',self.real_time).grid(row=1,column=0,sticky='nsew',padx=5,pady=4,ipadx=60)
        self.gauge_showing(titre='CPU consumption').grid(row=2,column=0,sticky='nsew',padx=5,pady=2)
        self.gauge_showing(titre='RAM consumption',bootstyle='danger').grid(row=3,column=0,sticky='nsew',padx=5)
        self.runningBtn = ttk.Button(self.gauche,textvariable=self.runningtext,
                                     image="play",compound="left",bootstyle='success-outline',command=self.runningTest)
        self.runningBtn.grid(row=4,column=0,sticky='nsew',padx=5,ipady=4)
        # je vais tester le conteneur principale 
        self.OnRunning()
        self.commandListinning()
    def general_monitoring(self):
        self.gauche = ttk.Frame(self,width=300)
        self.gauche.place(x=0,y=0,relheight=1)
        #self.main = ScrolledFrame(self, autohide=True,width=1121)
        #on cree la tabulation 
        self.main = ttk.Notebook(self,bootstyle="primary")
        self.main.place(x=245,y=0,relheight=0.93,relwidth=0.775)
        #on rajoute les tabs 
        self.main.add(ModelMonitoring(self.main),text='Model monitoring')
        self.main.add(CommandMonitoring(self.main),text='command monitoring')
        
    def simple_showing(self,titre, variable): 
        panel = ttk.Frame(self.gauche,borderwidth=1,relief='solid')
        
        center1 = ttk.Frame(panel,style='info.Inverse.TLabel')
        ttk.Label(center1,text=titre, font='Calibri 12 bold',style='info.Inverse.TLabel').pack(expand=True,ipady=5)
        center1.pack(side='top',expand=True,fill='both')
        
        center1 = ttk.Frame(panel)
        ttk.Label(center1,text='00:00:00',textvariable=variable, font='Calibri 18').pack(expand=True,ipady=6)
        center1.pack(side='top',expand=True,fill='both')
        
        return panel
    
    def gauge_showing(self,titre="aucun", bootstyle="success"):
        panel = ttk.Frame(self.gauche)
        meter = ttk.Meter(
            master=panel,
            bootstyle=bootstyle,
            metersize=200,
            amounttotal=100,
            amountused=0,
            meterthickness=20,
            stripethickness=5,
            metertype="semi",
            textright="%",
            subtext=titre,
            interactive=False,
        )
        meter.pack(anchor='center')
        self.gauges.append(meter)
        return panel

    
    # mes fonctions de comportement 
    def OnRunning(self): 
        if self.runningtext.get() == self.running[1] :
            ram = psutil.virtual_memory().percent
            cpu = psutil.cpu_percent()
            self.monitoring_time.set(self.conversionTime(int(self.model.Temps[-1])))
            self.real_time.set(self.conversionTime(self.compteur))
            self.gauges[0].configure(amountused=cpu)
            self.gauges[1].configure(amountused=ram)
            self.compteur += 1
        self.gauche.after(1000,self.OnRunning)
    def commandListinning(self): 
        if self.runningtext.get() == self.running[1] :
            lire = next(iter(com.readCommand().items()))
            self.model.CommandeVanne[str(lire[0])] = int(lire[1])
        self.gauche.after(1,self.commandListinning)
    def conversionTime(self,sec)-> str:
        temp = ""
        heure = sec // 3600 
        minute = (sec % 3600) // 60
        seconde = (sec % 3600) % 60
        if heure < 10 :
            temp += f"0{heure}:"
        else :
            temp += str(heure)+":"
        if minute < 10 :
            temp += f"0{minute}:"
        else :
            temp += str(minute)+":"
        if seconde < 10 :
            temp += f"0{seconde}"
        else :
            temp += str(seconde)
        return temp

    def runningTest(self):
        if self.runningtext.get() == self.running[0] :
            self.runningBtn.configure(bootstyle='danger-outline',image="stop",compound="left")
            self.runningtext.set(self.running[1])
            if self.running3D == False :
                self.running3D = True
                self.voir_3D()
        else: 
            self.runningBtn.configure(bootstyle='success-outline',image="play",compound="left")
            self.runningtext.set(self.running[0])
    def execute_script_with_sys(self):
        sys.executable
        subprocess.call([sys.executable,'../Water Twin by MEME/visualisation/visualisation3D.py'])
    def voir_3D(self):
        #self.running3D = False
        my_thread = threading.Thread(target=self.execute_script_with_sys)
        my_thread.start()
        #my_thread.join()
        
    
if __name__ == '__main__' : 
    app = ttk.Window()
    TwinApp(app).pack()
    app.mainloop()