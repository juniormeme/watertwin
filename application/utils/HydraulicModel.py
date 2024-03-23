import matplotlib.pyplot as plt
import numpy as np

class HydraulicModel : 
    
    def __init__(self, name):
        #Les parèmetres globales et statiques du modèle
        self.name = name 
        self.running = False 
        self.capture = False 
        self.pas = 0
        self.marge = 0
        # les etats du modèles
        self.Ct1state = 0
        self.Ct2state = 0
        self.Ic1state = 0
        self.Ic10state = 0 
        self.Ic11state = 0
        self.Ic2state = 0
        self.Ic4state = 0
        self.Ic6state = 0
        self.Ic7state = 0
        # Les valeurs pour les commandes 
        self.CommandeVanne = {
            '1' : 1 ,
            '2' : 1 ,
            '3' : 1 ,
            '4' : 1 ,
            '5' : 1 ,
            '6' : 1 ,
            '7' : 1 ,
            '8' : 1 ,
            '9' : 1 ,
            '10' : 1 ,
        }
        self.CommandePompe = {
            'PMP01' : 0,
            'PMP02' : 0
        }
        # Les axes à manipuler 
        self.Temps = [] 
        self.Y = {}
        self.Y['PMP01'] = []
        self.Y['PMP02'] = []
        self.Y['CADC01'] = []
        self.Y['CAPC01'] = []
        self.Y['CADC02'] = []
        self.Y['CADC03'] = []
        self.Y['CADC04'] = []
        self.Y['CAPC04'] = []
        self.Y['CADC05'] = []
        self.Y['CADC06'] = []
        self.Y['CANTK1'] = []
        self.Y['CAPTK1'] = []
        self.Y['CANTK2'] = []
        self.Y['CAPTK2'] = []
        self.Y['CADC07'] = []
        self.Y['CAPC07'] = []
        self.Y['CADC11'] = []
        self.Y['CAPC11'] = []
        self.Y['CADC10'] = []
        self.Y['CAPC10'] = []
        
    def stepEulerForward(self,k = 0): 
        Ts , marge = self.pas ,self.marge 
        # Arrangement des equations 
        # Commande pour les pompes 
        See , Se1e = (1000* self.CommandePompe['PMP01']) ,(1000* self.CommandePompe['PMP02'])
        # Commande pour les vannes 
        Rv1r,Rv2r = (-19 * self.CommandeVanne['1'] + 20),(-19 * self.CommandeVanne['2'] + 20)
        Rv3r,Rv4r = (-19 * self.CommandeVanne['3'] + 20),(-19 * self.CommandeVanne['4'] + 20)
        Rv5r,Rv6r = (-19 * self.CommandeVanne['5'] + 20),(-19 * self.CommandeVanne['6'] + 20)
        Rv7r,Rv8r = (-19 * self.CommandeVanne['7'] + 20),(-19 * self.CommandeVanne['8'] + 20)
        Rv9r,Rv10r = (-19 * self.CommandeVanne['9'] + 20),(-19 * self.CommandeVanne['10'] + 20)
        # Les constantes à determiner 
        Rp1r,Rp2r,Rp3r,Rp4r,Rp5r,Rp6r,Rp7r,Rp8r,Rp9r,Rp10r,Rp11r = 0.8,1,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8 # Pour les pertes de charges linéaires 
        Ct1c , Ct2c = 100 , 100#Les capacités de tank 
        Ic1i,Ic2i,Ic3i,Ic4i,Ic5i,Ic6i,Ic7i,Ic10i,Ic11i = 5,5,5,3,3,3,3,3,3 # Les inerties des tuyaux 
        At1 , At2 = 100, 100 # les surfaces des tanks
        # Le coeur des calculs    
        # je dois traiter l'axe des X 
        self.Temps.append(k*Ts)
        if(len(self.Temps)>marge): 
            self.Temps.remove(self.Temps[0])
            
        # Les etats initiaux des states 
        if k == 0 : 
            self.Ct1state = 0
            self.Ct2state = 0 
            self.Ic1state = 0 
            self.Ic10state = 0 
            self.Ic11state = 0 
            self.Ic2state = 0 
            self.Ic4state = 0 
            self.Ic6state = 0 
            self.Ic7state = 0 
        #dynamic equations
        # Les variables liées aux states 
        Ct1e = self.Ct1state / Ct1c 
        Ct2e = self.Ct2state / Ct2c
        Ic1f = self.Ic1state / Ic1i
        Ic10f = self.Ic10state / Ic10i
        Ic11f = self.Ic11state / Ic11i
        Ic2f = self.Ic2state / Ic2i
        Ic4f = self.Ic4state / Ic4i
        Ic6f = self.Ic6state / Ic6i
        Ic7f = self.Ic7state / Ic7i
        # Les etats de resistance 
        # Le coeur des calculs 
        Rp1e = Rp1r * Ic1f
        Rp10e = Rp10r * Ic10f
        Rp11e = Rp11r * Ic11f
        Rp2e = Rp2r * Ic2f
        Rp4e = Rp4r * Ic4f
        Rp6e = Rp6r * Ic6f
        Rp7e = Rp7r * Ic7f
        Rv1e = Rv1r * Ic1f
        Rv10e = Rv10r * Ic10f
        Rv2e = Rv2r * Ic2f
        Rv4e = Rv4r * Ic4f
        Rv6e = Rv6r * Ic6f
        Rv7e = Rv7r * Ic7f
        # Les variables de haut niveau 
        ZeroJunctionf = Ic1f - Ic2f
        ZeroJunction1f = Ic4f - Ic6f
        Ic7e = (Ct1e - Rp7e) - Rv7e
        Ic10e = (Ct2e - Rp10e) - Rv10e
        Ic3state = ZeroJunctionf * Ic3i
        Ic5state = ZeroJunction1f * Ic5i
        Rp3e = Rp3r * ZeroJunctionf
        Rp5e = Rp5r * ZeroJunction1f
        Rv3e = Rv3r * ZeroJunctionf
        Rv5e = Rv5r * ZeroJunction1f
        Ic3e_in = (((((See - Rp1e) - Rv1e) - (Rv3e + Rp3e)) / Ic1i - (((Rv3e + Rp3e) - Rp2e) - Rv2e) / Ic2i) * Ic3i) / (1.0 + (1.0 / Ic1i + 1.0 / Ic2i) * Ic3i)
        Ic5e_in = (((((Se1e - Rp4e) - Rv4e) - (Rv5e + Rp5e)) / Ic4i - (((Rv5e + Rp5e) - Rp6e) - Rv6e) / Ic6i) * Ic5i) / (1.0 + (1.0 / Ic4i + 1.0 / Ic6i) * Ic5i)
        Conduit3e = (Ic3e_in + Rv3e) + Rp3e
        Conduit5e = (Ic5e_in + Rv5e) + Rp5e
        Ic1e = ((See - Rp1e) - Rv1e) - Conduit3e
        Ic4e = ((Se1e - Rp4e) - Rv4e) - Conduit5e
        Ic6e = (Conduit5e - Rp6e) - Rv6e
        Ic2e = (Conduit3e - Rp2e) - Rv2e
        Rp8f = ((Ct1e - ((Ct2e - Rv9r * Ic11f) - Rp9r * Ic11f)) / Rp8r) / (1.0 + (Rv8r + (Rv9r + Rp9r)) / Rp8r)
        Rv8e = Rv8r * Rp8f
        Ct1f = (Ic2f + ZeroJunction1f) - (Rp8f + Ic7f)
        ZeroJunction4f = Ic11f - Rp8f
        Rp9e = Rp9r * ZeroJunction4f
        Ct2f = (ZeroJunctionf + Ic6f) - (Ic10f + ZeroJunction4f)
        Rv9e = Rv9r * ZeroJunction4f
        Conduit9e = (Ct2e - Rv9e) - Rp9e
        Conduit8e = (Ct1e - Rv8e) - Conduit9e
        Ic11e = Conduit9e - Rp11e
        # Equation du système par Euler Forward
        self.Ct1state = self.Ct1state + Ts * Ct1f
        self.Ct2state = self.Ct2state + Ts * Ct2f
        self.Ic1state = self.Ic1state + Ts * Ic1e
        self.Ic10state = self.Ic10state + Ts * Ic10e 
        self.Ic11state = self.Ic11state + Ts * Ic11e
        self.Ic2state = self.Ic2state + Ts * Ic2e
        self.Ic4state = self.Ic4state + Ts * Ic4e
        self.Ic6state = self.Ic6state + Ts * Ic6e
        self.Ic7state = self.Ic7state + Ts * Ic7e 
        # Les sorties 
        self.Y['PMP01'].append(See)
        self.Y['PMP02'].append(Se1e)
        self.Y['CADC01'].append(Ic1f)
        self.Y['CAPC01'].append(See - Conduit3e)
        self.Y['CADC02'].append(Ic2f)
        self.Y['CADC03'].append(ZeroJunctionf)
        self.Y['CADC04'].append(Ic4f)
        self.Y['CAPC04'].append(Se1e - Conduit5e)
        self.Y['CADC05'].append(ZeroJunction1f)
        self.Y['CADC06'].append(Ic6f)
        self.Y['CANTK1'].append(self.Ct1state/At1)
        self.Y['CAPTK1'].append(Ct1e)
        self.Y['CANTK2'].append(self.Ct2state/At2)
        self.Y['CAPTK2'].append(Ct2e)
        self.Y['CADC07'].append(Ic7f)
        self.Y['CAPC07'].append(Ic7e)
        self.Y['CADC11'].append(Ic11f)
        self.Y['CAPC11'].append(Conduit8e)
        self.Y['CADC10'].append(Ic10f)
        self.Y['CAPC10'].append(Ct2e)
        if(len(self.Y['PMP01'])>marge): 
            self.Y['PMP01'].remove(self.Y['PMP01'][0])
            self.Y['PMP02'].remove(self.Y['PMP02'][0])
            self.Y['CADC01'].remove(self.Y['CADC01'][0])
            self.Y['CAPC01'].remove(self.Y['CAPC01'][0])
            self.Y['CADC02'].remove(self.Y['CADC02'][0])
            self.Y['CADC03'].remove(self.Y['CADC03'][0])
            self.Y['CADC04'].remove(self.Y['CADC04'][0])
            self.Y['CAPC04'].remove(self.Y['CAPC04'][0])
            self.Y['CADC05'].remove(self.Y['CADC05'][0])
            self.Y['CADC06'].remove(self.Y['CADC06'][0])
            self.Y['CANTK1'].remove(self.Y['CANTK1'][0])
            self.Y['CAPTK1'].remove(self.Y['CAPTK1'][0])
            self.Y['CANTK2'].remove(self.Y['CANTK2'][0])
            self.Y['CAPTK2'].remove(self.Y['CAPTK2'][0])
            self.Y['CADC07'].remove(self.Y['CADC07'][0])
            self.Y['CAPC07'].remove(self.Y['CAPC07'][0])
            self.Y['CADC11'].remove(self.Y['CADC11'][0])
            self.Y['CAPC11'].remove(self.Y['CAPC11'][0])
            self.Y['CADC10'].remove(self.Y['CADC10'][0])
            self.Y['CAPC10'].remove(self.Y['CAPC10'][0])
            
    def stopModel(self):
        pass
    
    def runModel(self) : 
        for i in range(10000) : 
            self.stepEulerForward(k=i)


if __name__ == '__main__' :     
    model = HydraulicModel(name="junior")
    model.pas = 0.01
    model.marge = 10000
    model.CommandePompe['PMP01'] = 1
    model.CommandePompe['PMP02'] = 1
    model.CommandeVanne['1'] = 1
    model.CommandeVanne['3'] = 1
    model.CommandeVanne['2'] = 1
    model.CommandeVanne['5'] = 0
    model.runModel()
    # Création de la figure
    plt.figure()

    # Tracé des courbes
    plt.plot(model.Temps, model.Y['CADC01'], 'b', label='Debit 1')
    plt.plot(model.Temps, model.Y['CADC02'], 'r', label='Debit 2')
    plt.plot(model.Temps, model.Y['CADC03'], 'y', label='Debit 3')
    # Ajout d'une légende
    plt.legend()

    # Affichage de la figure
    plt.show()