# pour l'affichage d'une fenetre specialisé dans l'affichage des scenarios 
# by MEME Junior
import tkinter as tk 
import ttkbootstrap as ttk 
from ttkbootstrap.constants import * 
from ttkbootstrap.scrolled import ScrolledText 
from pathlib import Path


class ScenarioVue : 
    
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

if __name__ == '__main__' : 
    ScenarioVue(['junior'])