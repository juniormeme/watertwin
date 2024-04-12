from ursina import * 
import communication as com
# Les classes qui simplifierons le travail 
class Actionneur(Button):
    def __init__(self, description = "aucun",tag="00000" , model="junior", initial = 0):
        super().__init__(parent=scene,
                         model=model, 
                         texture='texture/vannes.png',
                         origin=(0,0,0),
                         color= color.white,
                         scale=k,
                         tooltip=Tooltip(f'Tag :{tag}\nDescription :{description}'),
                         highlight_color=color.gray) 
        self.description = description
        self.tag = tag
        self.state = 'close'
        self.behavior = {
            'VLV01' : [88.3580551147461,Vec3(-22.9717, 0, -5.54127),'open','y'],
            'VLV04' : [89.4161148071289,Vec3(8.7056, 0, 25.8274),'open','y'],
            'VLV09' : [-91.52202606201172,Vec3(1.91302, 0, 0.295945),'open','y'],
            'VLV08' : [90.32833099365234,Vec3(-1.93706, 0, 0.235669),'open','y'],
            'VLV05' : [-89.90215301513672,Vec3(0, 14.4676, 9.5421),'open','x'],
            'VLV02' : [-88.20781707763672,Vec3(0, 13.9216, 10.9239),'open','x'],
            'VLV06' : [-89.18460845947266,Vec3(0, 14.2213, 9.49221),'open','x'],
            'VLV03' : [-88.0353775024414,Vec3(0, 13.9893, 11.0476),'open','x'],
            'VLV07' : [-89.02767181396484,Vec3(0, 13.3133, 8.50784),'open','x'],
            'VLV10' : [-87.76103210449219,Vec3(0, 13.067, 8.54993),'open','x']
        }
        self.initially(initial)
    def input(self,key):
        # quand on click pour faire une action
        if self.hovered : 
            if key == 'left mouse down' :
                if self.state == 'open' : 
                    self.state = 'close'
                    if self.state == self.behavior[self.tag][2]:
                        if self.behavior[self.tag][3] == 'y' : 
                            self.rotation_y = self.behavior[self.tag][0]
                        else : 
                            self.rotation_x = self.behavior[self.tag][0]
                        self.position = self.behavior[self.tag][1]
                    else :
                        self.rotation = 0
                        self.position = Vec3(0,0,0)
                    #on envoie la commande à la couche application 
                    com.writeCommand({str(self.tag) : 0})
                else : 
                    self.state = 'open' 
                    if self.state == self.behavior[self.tag][2]:
                        if self.behavior[self.tag][3] == 'y' :
                            self.rotation_y = self.behavior[self.tag][0]
                        else : 
                            self.rotation_x = self.behavior[self.tag][0]
                        self.position = self.behavior[self.tag][1]
                    else :
                        self.rotation = 0
                        self.position = Vec3(0,0,0)
                    #
                    #on envoie la commande à la couche application 
                    com.writeCommand({str(self.tag) : 1}) 
    def initially(self,state): 
        if state == 0 : 
            self.state = 'close'
            if self.state == self.behavior[self.tag][2]:
                if self.behavior[self.tag][3] == 'y' : 
                    self.rotation_y = self.behavior[self.tag][0]
                else : 
                    self.rotation_x = self.behavior[self.tag][0]
                self.position = self.behavior[self.tag][1]
            else :
                self.rotation = 0
                self.position = Vec3(0,0,0)
        else :
            self.state = 'open' 
            if self.state == self.behavior[self.tag][2]:
                if self.behavior[self.tag][3] == 'y' :
                    self.rotation_y = self.behavior[self.tag][0]
                else : 
                    self.rotation_x = self.behavior[self.tag][0]
                self.position = self.behavior[self.tag][1]
            else :
                self.rotation = 0
                self.position = Vec3(0,0,0) 
            
                    
# creation de l'application de visionnage 
app = Ursina()
window.title = "3D Water twin by MEME : monitoring"
window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = False
window.position =(0,30)
# paramètres 
performance = "HIGH"
eau = {}
k = 2
# Les equipements passives de l'environnement 
if performance == "HIGH" : 
    Entity(model='objet/conduit1.obj', texture='texture/conduit.png',scale=k)
    Entity(model='objet/conduit2.obj', texture='texture/conduit.png',scale=k)
    Entity(model='objet/conduit3.obj', texture='texture/conduit.png',scale=k)
    Entity(model='objet/conduit4.obj', texture='texture/conduit.png',scale=k)
    Entity(model='objet/conduit5.obj', texture='texture/conduit.png',scale=k)

Button(
    parent=scene,
    model='objet/pompe1.obj', 
    texture='texture/pompe.png',
    scale=k,
    origin=0,
    tooltip= Tooltip(text=f'Tag :PMP01 \nDescription :Pompe immergée de 150 L/min',background_color=color.light_gray),
    color=color.white,
    highlight_color=color.gray,
    )
Button(
    parent=scene,
    model='objet/pompe2.obj', 
    texture='texture/pompe.png',
    scale=k,
    origin=0,
    tooltip= Tooltip(text=f'Tag :PMP02 \nDescription :Pompe immergée de 200 L/min',background_color=color.light_gray),
    color=color.white,
    highlight_color=color.gray,
    )
if performance == "HIGH" :
    Entity(model='objet/support_pompe.obj', texture='texture/support_pompe.png',color=color.white,scale=k)
    Entity(model='objet/ceinture_pompe.obj', texture='texture/ceinture.png',color=color.white,scale=k)
    Entity(model='objet/fondation.obj', texture='texture/fondation.png',color=color.white,scale=k)
    Entity(model='objet/structure.obj', texture='texture/structure.png',color=color.white,scale=k)
    Entity(model='objet/tank.obj',texture='texture/tank.png',color=color.white,scale=k)
    Entity(model='objet/maison.obj', texture='texture/maison_complet.png',scale=k)
    Entity(model='objet/panneau_solaire.obj', texture='texture/panneau.png',scale=k)
else :
    Entity(model='objet/objects.obj', texture='texture/texture_bake.png',scale=k)
# Mon bouton pour les batteries
Button(parent=scene,
       model='objet/batteries.obj', 
       texture='texture/batterie.png',
       origin=0,
       scale=k,
       tooltip=Tooltip(text="Equipement d'alimentation en electricité",background_color=color.blue),
       color = color.white
       )
niveau_eau_tank1 = Entity(model='objet/water_level_1.obj', texture='texture/niveau_eau_1.png',scale=k)
niveau_eau_tank2 = Entity(model='objet/water_level_2.obj', texture='texture/niveau_eau_2.png',scale=k)
Entity(model='objet/connexion.obj', texture='texture/fils.png',scale=k)
eau["VLV05"] = Entity(model='objet/eau_1.obj', texture='texture/mayi.png',scale=k)
eau["VLV02"] = Entity(model='objet/eau_2.obj', texture='texture/mayi.png',scale=k)
eau["VLV06"] = Entity(model='objet/eau_3.obj', texture='texture/mayi.png',scale=k)
eau["VLV03"] = Entity(model='objet/eau_4.obj', texture='texture/mayi.png',scale=k)
eau["VLV10"] = Entity(model='objet/eau_5.obj', texture='texture/mayi.png',scale=k)
eau["VLV08"] = Entity(model='objet/eau_6.obj', texture='texture/mayi.png',scale=k)
eau["VLV09"] = eau["VLV08"]
eau["VLV07"] = Entity(model='objet/eau_7.obj', texture='texture/mayi.png',scale=k)
if performance == "HIGH" :
    Entity(model='objet/controlbox1.obj',texture='texture/comandbox.png',scale=k,color = color.white)
    Entity(model='objet/controlbox2.obj',texture='texture/comandbox.png',scale=k,color = color.white)
Actionneur(description= "La vanne du conduit 1, on controle le debit",tag="VLV01",model='objet/vanne_1.obj',initial=1)
Actionneur(description= "La vanne du conduit 4, on controle le debit",tag="VLV04",model='objet/vanne_2.obj',initial=1)
Actionneur(description= "La vanne du conduit 9, on controle le debit",tag="VLV09",model='objet/vanne_3.obj',initial=1)
Actionneur(description= "La vanne du conduit 8, on controle le debit",tag="VLV08",model='objet/vanne_4.obj',initial=1)
Actionneur(description= "La vanne du conduit 5, on controle le debit",tag="VLV05",model='objet/vanne_5.obj',initial=1)
Actionneur(description= "La vanne du conduit 2, on controle le debit",tag="VLV02",model='objet/vanne_6.obj',initial=1)
Actionneur(description= "La vanne du conduit 6, on controle le debit",tag="VLV06",model='objet/vanne_7.obj',initial=1)
Actionneur(description= "La vanne du conduit 3, on controle le debit",tag="VLV03",model='objet/vanne_8.obj',initial=1)
Actionneur(description= "La vanne du conduit 7, on controle le debit",tag="VLV07",model='objet/vanne_9.obj',initial=1)
Actionneur(description= "La vanne du conduit 10, on controle le debit",tag="VLV10",model='objet/vanne_10.obj',initial=1)
if performance =="HIGH" :
    Entity(model='objet/texte.obj', texture='texture/reste.png',scale=k)

niveau_eau_tank1.y = -3.5631611347198486
niveau_eau_tank2.y = -3.5037078857421875
# Comportement globale de la scène 
def update() :
    # ici on ajuste le comportement de tout le système en fonction des données des capteurs 
    try:
        comportement = com.readValues()
        # mouvement du niveau du tank selon la vitesse
        #niveau_eau_tank1.y += 5*comportement['CANTK1RATE']*time.dt
        #niveau_eau_tank2.y += 5*comportement['CANTK2RATE']*time.dt 
        niveau_eau_tank1.y = ((3.5631611347198486*comportement["CANTK1"])/3) - 3.5631611347198486
        niveau_eau_tank2.y = ((3.5037078857421875*comportement["CANTK2"])/3) - 3.5037078857421875
        # pour le conduit 2
        if comportement['CADC02'] >= 2 :
            eau['VLV02'].enabled = True
        else: 
            eau['VLV02'].enabled = False
        #pour le conduit 3
        if comportement['CADC03'] >= 2 :
            eau['VLV03'].enabled = True
        else: 
            eau['VLV03'].enabled = False
        #pour le conduit 5   
        if comportement['CADC05'] >= 2 :
            eau['VLV05'].enabled = True
        else: 
            eau['VLV05'].enabled = False
        #pour le conduit 6
        if comportement['CADC06'] >= 2 :
            eau['VLV06'].enabled = True
        else: 
            eau['VLV06'].enabled = False
        #pour le conduit 7
        if comportement['CADC07'] >= 2 :
            eau['VLV07'].enabled = True
        else: 
            eau['VLV07'].enabled = False
        #pour le conduit 11
        if comportement['CADC11'] >= 2 :
            eau['VLV08'].enabled = True
        else: 
            eau['VLV08'].enabled = False
        #pour le conduit 10
        if comportement['CADC10'] >= 2 :
            eau['VLV10'].enabled = True
        else: 
            eau['VLV10'].enabled = False
    except KeyError :
        pass
    except IndexError :
        pass
    # virtuels 
    # les limites du niveau d'eau 
    # le tank 1 
    if niveau_eau_tank1.y >= 0 : 
        # effet du trop plein 
        niveau_eau_tank1.y = 0
    elif niveau_eau_tank1.y >= -0.16048488020896912:
        # debordement du conduit 2
        pass
    elif niveau_eau_tank1.y >= -0.4808924198150635 : 
        # debordement du conduit 5
        pass
    else : 
        if niveau_eau_tank1.y <= -3.5631611347198486 : 
            # envoie de notification tank vide 
            niveau_eau_tank1.y = -3.5631611347198486
    # Le tank 2
    if niveau_eau_tank2.y >= 0 : 
        # effet du trop plein 
        niveau_eau_tank2.y = 0
    elif niveau_eau_tank2.y >= -0.16048488020896912:
        # debordement du conduit 2
        pass
    elif niveau_eau_tank2.y >= -0.39633071422576904 : 
        # debordement du conduit 6
        pass
    else : 
        if niveau_eau_tank2.y <= -3.5037078857421875 : 
            # envoie de notification tank vide 
            niveau_eau_tank2.y = -3.5037078857421875
            
         
#definitions de l'environement globale 
Entity(model='plane', texture='grass',scale=300, texture_scale=(20,10))
Sky()
EditorCamera()
app.run()
