""" Fichier : app.py 
    Auteur : MEME ANDERMON JUNIOR 
    description : Ce fichier est le fichier principale de l'application et qui permet de reunir
    toute les pages du logiciel (DT) et permettra aussi l'echange des infos entre les différentes 
    pages programmer ainsi que leurs synchronisation 
"""
#les imports
import tkinter as tk 
import ttkbootstrap as ttk 
from scenario_app import ScenarioApp
from twin_app import TwinApp
from PIL import ImageTk, Image


class Application(): 
    def __init__(self): 
        self.window = ttk.Window()
        self.window.title('Water twin')
        self.window_width = 1100
        self.window_height = 680
        self.window.geometry(f'{self.window_width}x{self.window_height}+50+6')
        self.barreMenu()
        self.mainPanel()
        
        
    def barreMenu(self): 
        barre = ttk.Frame(self.window,bootstyle='primary')    
        barre.place(x=0,y=0,relwidth=1)
        ttk.Button(barre,text="Twin model",bootstyle="success", command=lambda:self.switch(1)).grid(row=0,column=0,ipady=10,ipadx=10,sticky='nsew')
        ttk.Button(barre,text="Scenarios",bootstyle="primary",command=lambda : self.switch(2)).grid(row=0,column=1,ipady=10,ipadx=10,sticky='nsew')
        ttk.Button(barre,text="Inventory",bootstyle="primary",command=lambda : self.switch(3)).grid(row=0,column=2,ipady=10,ipadx=10,sticky='nsew')
        ttk.Button(barre,text="Profiles",bootstyle="primary",command=lambda : self.switch(4)).grid(row=0,column=3,ipady=10,ipadx=10,sticky='nsew')
        ttk.Button(barre,text="Settings",bootstyle="primary",command=lambda : self.switch(5)).grid(row=0,column=4,ipady=10,ipadx=10,sticky='nsew')
        interval = ttk.Frame(barre,bootstyle="primary").grid(row=0,column=5,ipadx=self.window_width,sticky='nsew')
        ttk.Label(interval,text="junior meme  ",font="Calibri 14 bold",background='#375A7F').pack(anchor="ne",ipady=10)
        
    def mainPanel(self):
        self.panel1 = TwinApp(self.window) 
        self.panel1.place(x=0,y=49,relheight=1,relwidth=1)
       
    def switch(self,a): 
        if a == 1 : 
            TwinApp(self.window).place(x=0,y=49,relheight=1,relwidth=1)
        elif a == 2 : 
            ScenarioApp(self.window).place(x=0,y=49,relheight=1,relwidth=1)  
        elif a == 3 :
            self.panel3 = ttk.Frame(self.window)  
            ttk.Label(self.panel3,text="Inventory", font="Calibri 32 bold").pack() 
            self.panel3.place(x=0,y=49,relheight=1,relwidth=1)
        elif a == 4 :
            self.panel4 = ttk.Frame(self.window)  
            ttk.Label(self.panel4,text="Profiles", font="Calibri 32 bold").pack() 
            self.panel4.place(x=0,y=49,relheight=1,relwidth=1)
        elif a == 5 : 
            self.panel5 = ttk.Frame(self.window)  
            ttk.Label(self.panel5,text="settings", font="Calibri 32 bold").pack() 
            self.panel5.place(x=0,y=49,relheight=1,relwidth=1)
        else : 
            print("nothing")
            
         
    def runApp(self): 
        self.window.mainloop()
        


if __name__ == '__main__' : 
    # Ici devient le point d'entrer du logiciel tout entier 
    Application().runApp()