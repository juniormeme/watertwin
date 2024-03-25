import tkinter as tk 
import ttkbootstrap as ttk 
from ttkbootstrap.scrolled import ScrolledFrame
from utils.command_showing import CommandShowing
from utils.graph import Graphique
from HydraulicModel import *
import threading
import communication as com

class ModelMonitoring(ttk.Frame) : 
    
    def __init__(self,master):
        ttk.Frame.__init__(self,master=master, bootstyle="dark")
        self.root = ScrolledFrame(self,autohide=True)
        self.root.pack(expand=True,fill='both')
        # les attributs 
        self.twin_app = self.master.master 
        self.k = 0 
        # la vue principale 
        self.figs = []
        self.figs.append(Graphique(self.root,"Pression Entré/sortie Conduit 1"))
        self.figs[-1].vision = True
        self.figs[-1].grid(row=0,column=0,padx=8,pady=8)
        self.figs.append(Graphique(self.root,"Pression Entré/sortie Conduit 4"))
        self.figs[-1].vision = False
        self.figs[-1].grid(row=0,column=1,padx=8,pady=8)
        self.figs.append(Graphique(self.root,"Debits conduits 1 , 2 et 3"))
        self.figs[-1].vision = False
        self.figs[-1].grid(row=1,column=0,padx=8,pady=8)
        self.figs.append(Graphique(self.root,"Debits conduits 4 , 5 et 6"))
        self.figs[-1].vision = False
        self.figs[-1].grid(row=1,column=1,padx=8,pady=8)
        self.figs.append(Graphique(self.root,"Pression et niveau d'eau au Tank 1"))
        self.figs[-1].vision = False
        self.figs[-1].grid(row=2,column=0,padx=8,pady=8)
        self.figs.append(Graphique(self.root,"Pression et niveau d'eau au Tank 2"))
        self.figs[-1].vision = False
        self.figs[-1].grid(row=2,column=1,padx=8,pady=8)
        self.figs.append(Graphique(self.root,"Debits aux conduits 7 , 11 et 10"))
        self.figs[-1].vision = False
        self.figs[-1].grid(row=3,column=0,padx=8,pady=8)
        self.figs.append(Graphique(self.root,"Pressions aux conduits 7 , 11 et 10"))
        self.figs[-1].vision = False
        self.figs[-1].grid(row=3,column=1,padx=8,pady=8)
        # on lance l'ecoute de la figure 1 
        threading.Thread(target=self.figure1).start()
        threading.Thread(target=self.figure2).start()
        threading.Thread(target=self.figure3).start()
        threading.Thread(target=self.figure4).start()
        threading.Thread(target=self.figure5).start()
        threading.Thread(target=self.figure6).start()
        threading.Thread(target=self.figure7).start()
        threading.Thread(target=self.figure8).start()
        #self.figure1()
        #self.figure2()
        #self.figure3()
        #self.figure4()
        #self.figure5()
        #self.figure6()
        #self.figure7()
        #self.figure8()
        
    def figure1(self):
        "Pression d'entré du conduit 1 + presssion de sortie du conduit 1"
        if self.twin_app.runningtext.get() == self.twin_app.running[1] : 
            # configuration par defaut du voyeur 
            self.figs[0].vision_btn.configure(text="Solveur : Calcul temps réel en cours...", bootstyle="primary")
            self.twin_app.model.stepEulerForward(k=self.k) # on lance le calcul du model 
            self.figs[0].axe.clear()
            self.figs[0].axe.grid()
            self.figs[0].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['PMP01'],color='dodgerblue',label="PMP01[Pa]")
            self.figs[0].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CAPC01'],color='r',label="CAPC01[Pa]")
            self.figs[0].axe.legend()
            self.figs[0].figure.canvas.draw()
            self.figs[0].figure.canvas.flush_events()
            # envois des comportements pour la visualisation 
            if self.k >= 2 :
                rate1 = float((self.twin_app.model.Y['CANTK1'][-1]-self.twin_app.model.Y['CANTK1'][-2])/self.twin_app.model.pas)
                rate1 = round(rate1,5)
                rate2 = float((self.twin_app.model.Y['CANTK2'][-1]-self.twin_app.model.Y['CANTK2'][-2])/self.twin_app.model.pas)
                rate2 = round(rate2,5)
            else: 
                rate1 = 1
                rate2 = 1
            com.writeValues({
                'RIEN' : 0,
                'CADC01' :self.twin_app.model.Y['CADC01'][-1],
                'CADC02':self.twin_app.model.Y['CADC02'][-1],
                'CADC03':self.twin_app.model.Y['CADC03'][-1],
                'CADC05':self.twin_app.model.Y['CADC05'][-1],
                'CADC06':self.twin_app.model.Y['CADC06'][-1],
                'CANTK1RATE':rate1,
                'CANTK2RATE':rate2,
                'CADC07':self.twin_app.model.Y['CADC07'][-1],
                'CADC11':self.twin_app.model.Y['CADC11'][-1],
                'CADC10':self.twin_app.model.Y['CADC10'][-1]
            })
            self.k += 1  
        else :
            self.figs[0].vision_btn.configure(text="Solveur : Calcul temps réel en arret...", bootstyle="danger")
        self.figs[0].after(1,self.figure1)
    def figure2(self):
        "On va monitorer le debit principale du conduit 1 + debit conduit 2 et 3"
        if self.twin_app.runningtext.get() == self.twin_app.running[1] and self.figs[1].vision == True : 
            self.figs[1].axe.clear()
            self.figs[1].axe.grid()
            self.figs[1].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['PMP02'],color='dodgerblue',label="PMP02[Pa]")
            self.figs[1].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CAPC04'],color='r',label="CAPC04[Pa]")
            self.figs[1].axe.legend()
            self.figs[1].figure.canvas.draw()
            self.figs[1].figure.canvas.flush_events()      
        self.figs[1].after(2,self.figure2)
    def figure3(self):
        "On va monitorer le debit principale du conduit 1 + debit conduit 2 et 3"
        if self.twin_app.runningtext.get() == self.twin_app.running[1] and self.figs[2].vision == True: 
            self.figs[2].axe.clear()
            self.figs[2].axe.grid()
            self.figs[2].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CADC01'],color='dodgerblue',label="CADC01[m3/s]")
            self.figs[2].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CADC02'],color='limegreen',label="CADC02[m3/s]")
            self.figs[2].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CADC03'],color='C1',label="CADC03[m3/s]")
            self.figs[2].axe.legend()
            self.figs[2].figure.canvas.draw()
            self.figs[2].figure.canvas.flush_events()      
        self.figs[2].after(2,self.figure3)
    def figure4(self):
        "On va monitorer le debit principale du conduit 1 + debit conduit 2 et 3"
        if self.twin_app.runningtext.get() == self.twin_app.running[1] and self.figs[3].vision == True: 
            self.figs[3].axe.clear()
            self.figs[3].axe.grid()
            self.figs[3].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CADC04'],color='dodgerblue',label="CADC04[m3/s]")
            self.figs[3].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CADC05'],color='limegreen',label="CADC05[m3/s]")
            self.figs[3].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CADC06'],color='C1',label="CADC06[m3/s]")
            self.figs[3].axe.legend()
            self.figs[3].figure.canvas.draw()
            self.figs[3].figure.canvas.flush_events()      
        self.figs[3].after(2,self.figure4)
    def figure5(self):
        "On va monitorer le debit principale du conduit 1 + debit conduit 2 et 3"
        if self.twin_app.runningtext.get() == self.twin_app.running[1] and self.figs[4].vision == True: 
            self.figs[4].axe.clear()
            self.figs[4].axe.grid()
            self.figs[4].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CANTK1'],color='C0',label="CANTK1[m]")
            #self.figs[4].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CAPTK1'],color='C1',label="CAPTK1[Pa]")
            self.figs[4].axe.legend()
            self.figs[4].figure.canvas.draw()
            self.figs[4].figure.canvas.flush_events()      
        self.figs[4].after(2,self.figure5)
    def figure6(self):
        "On va monitorer le debit principale du conduit 1 + debit conduit 2 et 3"
        if self.twin_app.runningtext.get() == self.twin_app.running[1] and self.figs[5].vision == True: 
            self.figs[5].axe.clear()
            self.figs[5].axe.grid()
            self.figs[5].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CANTK2'],color='C0',label="CANTK2[m]")
            self.figs[5].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CAPTK2'],color='C1',label="CAPTK2[Pa]")
            self.figs[5].axe.legend()
            self.figs[5].figure.canvas.draw()
            self.figs[5].figure.canvas.flush_events()      
        self.figs[5].after(2,self.figure6)
    def figure7(self):
        "On va monitorer le debit principale du conduit 1 + debit conduit 2 et 3"
        if self.twin_app.runningtext.get() == self.twin_app.running[1] and self.figs[6].vision == True: 
            self.figs[6].axe.clear()
            self.figs[6].axe.grid()
            self.figs[6].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CADC07'],color='dodgerblue',label="CADC07[m3/s]")
            self.figs[6].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CADC11'],color='limegreen',label="CADC11[m3/s]")
            self.figs[6].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CADC10'],color='C1',label="CADC10[m3/s]")
            self.figs[6].axe.legend()
            self.figs[6].figure.canvas.draw()
            self.figs[6].figure.canvas.flush_events()      
        self.figs[6].after(2,self.figure7)
    def figure8(self):
        "On va monitorer le debit principale du conduit 1 + debit conduit 2 et 3"
        if self.twin_app.runningtext.get() == self.twin_app.running[1] and self.figs[7].vision == True : 
            self.figs[7].axe.clear()
            self.figs[7].axe.grid()
            self.figs[7].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CAPC07'],color='dodgerblue',label="CAPC07[Pa]")
            self.figs[7].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CAPC11'],color='limegreen',label="CAPC11[Pa]")
            self.figs[7].axe.plot(self.twin_app.model.Temps,self.twin_app.model.Y['CAPC10'],color='C1',label="CAPC10[Pa]")
            self.figs[7].axe.legend()
            self.figs[7].figure.canvas.draw()
            self.figs[7].figure.canvas.flush_events()      
        self.figs[7].after(2,self.figure8)

class CommandMonitoring(ttk.Frame) : 

    def __init__(self,master):
        ttk.Frame.__init__(self,master=master)
        root = ttk.Frame(self)
        root.pack(expand=True,anchor='n')
        self.k = 0 
        self.twin_app = self.master.master
        self.vannes = []
        # On insère les UI des commandes
        self.vannes.append(CommandShowing(root,"VLVC01"))
        self.vannes[-1].grid(row=0,column=0,padx=10,pady=10,ipadx=15,sticky='nsew')
        self.vannes[-1].setOff()
        self.vannes.append(CommandShowing(root,"VLVC02"))
        self.vannes[-1].grid(row=0,column=1,padx=10,pady=10,ipadx=15,sticky='nsew')
        self.vannes[-1].setOff()
        self.vannes.append(CommandShowing(root,"VLVC03"))
        self.vannes[-1].grid(row=0,column=2,padx=10,pady=10,ipadx=15,sticky='nsew')
        self.vannes[-1].setOn()
        self.vannes.append(CommandShowing(root,"VLVC04"))
        self.vannes[-1].grid(row=0,column=3,padx=10,pady=10,ipadx=15,sticky='nsew')
        self.vannes[-1].setOff()
        self.vannes.append(CommandShowing(root,"VLVC05"))
        self.vannes[-1].grid(row=0,column=4,padx=10,pady=10,ipadx=15,sticky='nsew')
        self.vannes[-1].setOff()
        self.vannes.append(CommandShowing(root,"VLVC06"))
        self.vannes[-1].grid(row=1,column=0,padx=10,pady=10,ipadx=15,sticky='nsew')
        self.vannes[-1].setOff()
        self.vannes.append(CommandShowing(root,"VLVC07"))
        self.vannes[-1].grid(row=1,column=1,padx=10,pady=10,ipadx=15,sticky='nsew')
        self.vannes[-1].setOff()
        self.vannes.append(CommandShowing(root,"VLVC08"))
        self.vannes[-1].grid(row=1,column=2,padx=10,pady=10,ipadx=15,sticky='nsew')
        self.vannes[-1].setOff()
        self.vannes.append(CommandShowing(root,"VLVC09"))
        self.vannes[-1].grid(row=1,column=3,padx=10,pady=10,ipadx=15,sticky='nsew')
        self.vannes[-1].setOff()
        self.vannes.append(CommandShowing(root,"VLVC10"))
        self.vannes[-1].grid(row=1,column=4,padx=10,pady=10,ipadx=15,sticky='nsew')
        self.vannes[-1].setOff()
        # Afffichage des ouvertures ou fermeture des vannes chaque une seconde il se met à jour 
        self.monitorVannes()
        
        root1 = ttk.Frame(self)
        root1.pack(expand=True,anchor='n')
        # ajout des buttons de capture des donneées et capture des scenarios 
        ttk.Button(root1,text="capture data",bootstyle="success-outline", command=self.fermevanne).pack(side="left",ipady=10,ipadx=50,padx=5,pady=5)
        ttk.Button(root1,text="capture sceanrios",bootstyle="success-outline", command=self.fermevanne2).pack(side="left",ipady=10,ipadx=50,padx=5,pady=5)
    
    def monitorVannes(self): 
        nom = ""
        for i in range(len(self.twin_app.model.CommandeVanne)) : 
            #arrangement 
            if i >= 9 : 
                nom = "VLV10"
            else :
                nom = f"VLV0{i+1}"
            # on le monitore
            if self.twin_app.model.CommandeVanne[nom] == 0 :
                self.vannes[i].setOff()
            else : 
                self.vannes[i].setOn()
        self.after(100,self.monitorVannes)

    def fermevanne(self):
        if self.twin_app.model.CommandePompe['PMP01'] == 1 :
            self.twin_app.model.CommandePompe['PMP01'] = 0 
        else :
            self.twin_app.model.CommandePompe['PMP01'] = 1

    def fermevanne2(self):
        if self.twin_app.model.CommandePompe['PMP02'] == 1 :
            self.twin_app.model.CommandePompe['PMP02'] = 0 
        else :
            self.twin_app.model.CommandePompe['PMP02'] = 1