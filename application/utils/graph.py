""" Fichier : graph.py 
    Auteur : MEME ANDERMON JUNIOR 
    description : C'est dans ce fichier qu'est codé toute la structure 
    d'un graph de monitoring du DT, sa manipulation et sa mise à jour 
    sera faite par l'interface qui va l'appeler
"""
import tkinter as tk 
import ttkbootstrap as ttk 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graphique(ttk.Labelframe) : 
    
    def __init__(self,master,titre) :
        ttk.Labelframe.__init__(self,master=master,text=titre, bootstyle="primary") 
        
        self.figure = plt.Figure(figsize=(4,3), dpi= 100)
        self.axe = self.figure.add_subplot(111)
        # fig1.suptitle("Capteur virtuel de niveau du tank : CAPNIV01",fontsize=10, ha='center', color='C0')
        self.plot = FigureCanvasTkAgg(self.figure, master=self)
        self.plot.draw()
        self.plot.get_tk_widget().grid(row=0,column=0,sticky='nsew',)
        self.vision = True
        self.vision_btn = ttk.Button(self,text="voir",bootstyle="success",command=self.changerEtat)
        self.vision_btn.grid(row=1,column=0,ipadx=10,ipady=6,sticky='w')
    
    def changerEtat(self):
        if self.vision == True : 
            self.vision = False
            self.vision_btn.configure(text="Voir",bootstyle="success")
        else : 
            self.vision = True
            self.vision_btn.configure(text="cacher",bootstyle="danger")