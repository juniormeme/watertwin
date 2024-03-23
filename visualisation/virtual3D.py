from ursina import * 
from communication import *
# creation des modèles pour le DT
class Capteur(Button):
    def __init__(self, name = "aucun",tag="00000" , model="junior"):
        super().__init__(parent=scene,model=model, 
                         texture='texture/bake.png',
                         origin=0,
                         color= color.white,
                         tooltip=Tooltip(f'Tag : {tag}\n\nObjet :{name}'),
                         highlight_color=color.gray) 
        self.name = name
        self.tag = tag
    def input(self,key):
        if self.hovered : 
            if key == 'left mouse down' :
                print(f"Demande de montitoring pour le capteur {self.tag}") 

class Actionneur(Button):
    def __init__(self, name = "aucun",tag="00000" , model="junior"):
        super().__init__(parent=scene,model=model, 
                         texture='texture/bake.png',
                         origin=0,
                         color= color.white,
                         tooltip=Tooltip(f'Tag : {tag}\n\nObjet :{name}'),
                         highlight_color=color.gray) 
        self.name = name
        self.tag = tag
        self.state = 'close'
    def input(self,key):
        if self.hovered : 
            if key == 'left mouse down' :
                if self.state == 'open' : 
                    self.state = 'close'
                    entre_eau.enabled = False
                    writeCommand({str(self.tag) : 0})
                else : 
                    self.state = 'open' 
                    entre_eau.enabled = True
                    writeCommand({str(self.tag) : 1}) 

# creation de l'application de visionnage 
app = Ursina()
window.title = "3D digital Twins : monitoring"
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = False
window.position =(0,30)
#quelques améliorations la mise à jour de tout la scene 
def update():
    # lectures des capteurs 
    try:
        rate = readValues()["CAPNIV01RATE"]
    except KeyError :
        rate = 0.005
    # ecriture des commandes
    try: 
        comd = readCommnand()['ACTVLV01']
        
        if comd == 1 : 
            valve.state = 'open'
            entre_eau.enabled = True
        else : 
            valve.state = 'close'
            entre_eau.enabled = False

    except KeyError :
        comd = 1
        
    # reagissement en fonction de l'etat des valves 
    if valve.state == 'open' : 
        niveau_eau.y += 2.8*rate*time.dt
    else : 
        niveau_eau.y -= 2.8*rate*time.dt
    
    # limite du niveau
    if niveau_eau.y > 0 :
        niveau_eau.y = 0 
    
    if niveau_eau.y < -2.60 : 
        niveau_eau.y = -2.60
        sortie_eau.enabled = False 
    else :
        sortie_eau.enabled = True
    
# Paramètre generale 
tank_vide = -2.76
tank_plein = 0 
tank_arret = -2.60
# on rempli les elements du DT 
tank = Capteur(tag="CAPNIV01",name="Main water tank",model='objet/tank.obj')
Capteur(tag="CAPFLW01",name="Flow meter of input",model='objet/flowmeter_1.obj')
Capteur(tag="CAPFLW02",name="Flow meter of output",model='objet/flowmeter_2.obj')

valve = Actionneur(tag="ACTVLV01",name="Input flow valve",model='objet/valve.obj')

entre_eau  = Entity(model='objet/eau_remplissage.obj', texture='texture/bake.png',color=color.blue)
sortie_eau = Entity(model='objet/eau_vidange.obj', texture='texture/bake.png', color=color.blue)
Entity(model='objet/mur.obj', texture='texture/bake.png')
niveau_eau = Entity(model='objet/niveau_eau.obj', texture='texture/bake.png')
niveau_eau.position = (0,((2.60*readValues()["CAPNIV01"])-2.60),0)
Entity(model='objet/tuyau_1.obj', texture='texture/bake.png')
Entity(model='objet/tuyau_2.obj', texture='texture/bake.png')
#config
sortie_eau.enabled = False 
entre_eau.enabled = False
niveau_eau.enabled = True 
#definitions de l'environement globale 
Entity(model='plane', texture='grass',scale=300, texture_scale=(20,10))
Sky()
EditorCamera()
app.run()