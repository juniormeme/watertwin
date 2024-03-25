""" Fichier : main.py 
    Auteur : MEME ANDERMON JUNIOR 
    description : Ce fichier est le fichier principale du logiciel, il affiche un splash screen qui prepare
    l'utilisateur du logiciel et nous ramène directement dans l'utilisation du menu principale du logiciel 
    concu selon l'architecture présenté ci bas 
"""
# les imports modules 
import tkinter as tk 
import ttkbootstrap as ttk
from PIL import ImageTk, Image
import subprocess, sys 


# variable de base 
window_height = 400 # la longueur de ma fenetre 
window_width = 400 # La largeur de ma fentre

# affchage de la fenetre principale 
window = tk.Tk()
window.title("Splash screen test")
window.geometry(f"400x400+{int((window.winfo_screenwidth()/2)-(window_width/2))}+{int((window.winfo_screenheight()/2)-(window_height/2))}")
window.overrideredirect(True)

# preparation de l'image de fond 
frame = tk.Frame(window)
frame.pack(fill=tk.BOTH,expand=True)
# chargement de l'image de fond 
image = Image.open("application/assets/splash_screen.jpg")
image = image.resize((window_width, window_height),Image.ADAPTIVE)  # Redimensionnez l'image selon vos besoins
# Création de l'objet ImageTk
photo = ImageTk.PhotoImage(image)
# Création du label avec l'image
background_label = tk.Label(frame, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
tk.Label(background_label,text="WATER ",font="Calibri 20 bold").place(x=10,y=180)
tk.Label(background_label,text="TWIN v1.0",font="Calibri 20").place(x=100,y=180)
tk.Label(background_label,text="By MEME JUNIOR",font="Calibri 12").place(x=99,y=210)
# la barre de progression 
progress = ttk.Progressbar(window,mode='determinate',bootstyle='primary',length=400)
progress.place(x= 0,y=386)

# vers le dossier d'application
def execute_script_with_sys():
    sys.executable
    subprocess.call([sys.executable,'application/app.py'])

# la fonction de chargement
def loading(): 
    progress['value'] += 1 
    if progress['value'] < 100 : 
        window.after(40,loading)
    else : 
        window.destroy()
        execute_script_with_sys()  
        print("enregistrement des donnees du programme")
           
window.after(0,loading)


window.mainloop()