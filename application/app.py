""" Fichier : app.py 
    Auteur : MEME ANDERMON JUNIOR 
    description : Ce fichier est le fichier principale de l'application et qui permet de reunir
    toute les pages du logiciel (DT) et permettra aussi l'echange des infos entre les différentes 
    pages programmer ainsi que leurs synchronisation 
"""
#les imports
from pathlib import Path
from tkinter import PhotoImage
import tkinter as tk 
import ttkbootstrap as ttk 
from scenario_app import ScenarioApp
from twin_app import TwinApp
from PIL import ImageTk, Image

PATH = Path(__file__).parent/ 'assets'

class Application(): 
    def __init__(self): 
        self.window = ttk.Window()
        self.window.title('Water twin')
        self.window_width = 1100
        self.window_height = 680
        self.window.geometry(f'{self.window_width}x{self.window_height}+49+6')
        # les etats 
        self.actual_panel = 0
        self.actual_panel_state = " "
        # les icones 
        self.images = [
            PhotoImage(
                name='monitoring', 
                file=PATH / 'icons8_pulse_20px.png'),
            PhotoImage(
                name='scenario', 
                file=PATH / 'icons8_graph_report_20px.png'),
            PhotoImage(
                name='formation', 
                file=PATH / 'icons8_training_20px.png'),
            PhotoImage(
                name='profile', 
                file=PATH / 'icons8_profile_20px.png'),
            PhotoImage(
                name='reglage', 
                file=PATH / 'icons8_settings_20px.png'),
            PhotoImage(
                name='user', 
                file=PATH / 'icons8_male_user_26px.png'),
            PhotoImage(
                name='capture', 
                file=PATH / 'icons8_fishing_24px.png'),
            PhotoImage(
                name='scene', 
                file=PATH / 'icons8_report_file_24px.png'),
            PhotoImage(
                name='play', 
                file=PATH / 'icons8_play_20px.png'),
            PhotoImage(
                name='pause', 
                file=PATH / 'icons8_pause_20px_2.png'),
            PhotoImage(
                name='stop', 
                file=PATH / 'icons8_stop_20px_1.png'),
            PhotoImage(
                name='visible', 
                file=PATH / 'icons8_eye_24px.png'),
            PhotoImage(
                name='invisible', 
                file=PATH / 'icons8_invisible_24px_4.png'),
        ]
        self.barreMenu()
        self.mainPanel()
        
    def barreMenu(self): 
        barre = ttk.Frame(self.window,bootstyle='primary')    
        barre.place(x=0,y=0,relwidth=1)
        ttk.Button(barre,text="Twin model",bootstyle="success",
                   image='monitoring',compound='left', command=lambda:self.switch(1)).grid(row=0,column=0,ipady=10,ipadx=10,sticky='nsew')
        ttk.Button(barre,text="Scenarios",bootstyle="primary",
                   image="scenario",compound='left',command=lambda : self.switch(2)).grid(row=0,column=1,ipady=10,ipadx=10,sticky='nsew')
        ttk.Button(barre,text="Trainning",bootstyle="primary",
                   image="formation",compound="left",command=lambda : self.switch(3)).grid(row=0,column=2,ipady=10,ipadx=10,sticky='nsew')
        ttk.Button(barre,text="Profiles",bootstyle="primary",
                   image="profile",compound="left",command=lambda : self.switch(4)).grid(row=0,column=3,ipady=10,ipadx=10,sticky='nsew')
        ttk.Button(barre,text="Settings",bootstyle="primary",
                   image="reglage",compound="left",command=lambda : self.switch(5)).grid(row=0,column=4,ipady=10,ipadx=10,sticky='nsew')
        interval = ttk.Frame(barre,bootstyle="primary").grid(row=0,column=5,ipadx=self.window_width,sticky='nsew')
        ttk.Label(interval,text="junior meme  ",font="Calibri 14 bold",
                  image="user",compound="left",background='#375A7F').pack(anchor="ne",ipady=10)
        
    def mainPanel(self):
        TwinApp(self.window).place(x=0,y=49,relheight=1,relwidth=1)
       
    def switch(self,a): 
        print(self.actual_panel_state)
        if a == 1 : 
            TwinApp(self.window).place(x=0,y=49,relheight=1,relwidth=1)
            self.actual_panel = a 
        elif a == 2 :
            if self.actual_panel == 1 : 
                box = ttk.dialogs.dialogs.Messagebox.show_question("Voullez-vous vraiment quitté le mode temps réel ?",
                                                                   "Confirmation",
                                                                   self.window,
                                                                   ['No:danger','Yes:succes']) 
                if box == "Oui":
                    ScenarioApp(self.window).place(x=0,y=49,relheight=1,relwidth=1)
                    self.actual_panel = a  
            else :
                 ScenarioApp(self.window).place(x=0,y=49,relheight=1,relwidth=1) 
        elif a == 3 :
            if self.actual_panel == 1 : 
                box = ttk.dialogs.dialogs.Messagebox.show_question("Voullez-vous vraiment quitté le mode temps réel ?",
                                                                   "Confirmation",
                                                                   self.window,
                                                                   ['No:danger','Yes:succes']) 
                if box == "Oui":
                    self.panel3 = ttk.Frame(self.window)  
                    ttk.Label(self.panel3,text="trainning", font="Calibri 32 bold").pack() 
                    self.panel3.place(x=0,y=49,relheight=1,relwidth=1)
                    self.actual_panel = a 
            else :
                self.panel3 = ttk.Frame(self.window)  
                ttk.Label(self.panel3,text="trainning", font="Calibri 32 bold").pack() 
                self.panel3.place(x=0,y=49,relheight=1,relwidth=1)
        elif a == 4 :
            if self.actual_panel == 1 : 
                box = ttk.dialogs.dialogs.Messagebox.show_question("Voullez-vous vraiment quitté le mode temps réel ?",
                                                                   "Confirmation",
                                                                   self.window,
                                                                   ['No:danger','Yes:succes']) 
                if box == "Oui":
                    self.panel4 = ttk.Frame(self.window)  
                    ttk.Label(self.panel4,text="Profiles", font="Calibri 32 bold").pack() 
                    self.panel4.place(x=0,y=49,relheight=1,relwidth=1)
                    self.actual_panel = a 
            else :
                self.panel4 = ttk.Frame(self.window)  
                ttk.Label(self.panel4,text="Profiles", font="Calibri 32 bold").pack() 
                self.panel4.place(x=0,y=49,relheight=1,relwidth=1)
            
        elif a == 5 : 
            if self.actual_panel == 1 : 
                box = ttk.dialogs.dialogs.Messagebox.show_question("Voullez-vous vraiment quitté le mode temps réel ?",
                                                                   "Confirmation",
                                                                   self.window,
                                                                   ['No:danger','Yes:succes']) 
                if box == "Oui":
                    self.panel5 = ttk.Frame(self.window)  
                    ttk.Label(self.panel5,text="settings", font="Calibri 32 bold").pack() 
                    self.panel5.place(x=0,y=49,relheight=1,relwidth=1)
                    self.actual_panel = a 
            else :
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