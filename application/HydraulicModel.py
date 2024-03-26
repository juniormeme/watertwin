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
        self.Ic5state = 0
        self.Ic7state = 0
        # Les valeurs pour les commandes 
        self.CommandeVanne = {
            'VLV01' : 1 ,
            'VLV02' : 1 ,
            'VLV03' : 1 ,
            'VLV04' : 1 ,
            'VLV05' : 1 ,
            'VLV06' : 1 ,
            'VLV07' : 1 ,
            'VLV08' : 1 ,
            'VLV09' : 1 ,
            'VLV10' : 1 ,
        }
        self.CommandePompe = {
            'PMP01' : 1,
            'PMP02' : 1
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
        See , Se1e = (277198.68* self.CommandePompe['PMP01']) ,(286969.44* self.CommandePompe['PMP02'])
        # les pressions resistantes
        Pres1e,Pres2e = -97707.6 ,-175873.68
        Pres3e,Pres4e = -175873.68,-107478.36
        Pres5e,Pres6e = -175873.68,-175873.68
        Pres7e,Pres11e,Pres10e = 175873.68,175873.68,175873.68
        # Commande pour les vannes 
        Rv1r,Rv2r = (13985716.43 * (1-self.CommandeVanne['VLV01'])),(13985716.43*(1-self.CommandeVanne['VLV02']))
        Rv3r,Rv4r = (13985716.43 *(1-self.CommandeVanne['VLV03'])),(13985716.43 *(1-self.CommandeVanne['VLV04']))
        Rv5r,Rv6r = (13985716.43 *(1-self.CommandeVanne['VLV05'])),(13985716.43 *(1-self.CommandeVanne['VLV06']))
        Rv7r,Rv8r = (13985716.43 *(1-self.CommandeVanne['VLV07'])),(13985716.43 *(1-self.CommandeVanne['VLV08']))
        Rv9r,Rv10r = (13985716.43 *(1-self.CommandeVanne['VLV09'])),(13985716.43 *(1-self.CommandeVanne['VLV10']))
        # Modèle partiellement calibré
        Rp1r,Rp2r,Rp3r=73556.43181,80600.0174,80600.0174
        Rp4r,Rp5r,Rp6r = 84701.34572,80600.0174,80600.0174
        Rp8r,Rp9r = 5349.558677,4457.965564
        Rp7r,Rp10r,Rp11r = 111449.1391,111449.1391,113232.3253
        Ct1c , Ct2c = 0.005526694 , 0.005526694 #Les capacités de tank 
        Ic1i,Ic2i,Ic3i = 7580258.303,8306125.461,8306125.461
        Ic4i,Ic5i,Ic6i = 8728782.288,8306125.461,8306125.461
        Ic7i,Ic10i,Ic11i = 11485239.85,11485239.85,11669003.69 # Les inerties des tuyaux 
        At1 , At2 = 54, 54 # les surfaces des tanks
        # Le coeur des calculs    
        # je dois traiter l'axe des X 
        self.Temps.append(k*Ts)
        if(len(self.Temps)>marge): 
            self.Temps.remove(self.Temps[0])
        # un scenario 
        
        # Les etats initiaux des states 
        if k == 0 : 
            self.Ct1state = 0
            self.Ct2state = 0
            self.Ic1state = 0
            self.Ic10state = 0
            self.Ic11state = 0
            self.Ic2state = 0
            self.Ic4state = 0
            self.Ic5state = 0
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
        Ic5f = self.Ic5state / Ic5i
        Ic7f = self.Ic7state / Ic7i
        # La première partie
        jonction1f = Ic1f - Ic2f
        jonction2f = Ic4f - Ic5f
        Rp1e = Rp1r * Ic1f
        Rp10e = Rp10r * Ic10f
        Rp11e = Rp11r * Ic11f
        Rp2e = Rp2r * Ic2f
        Rp4e = Rp4r * Ic4f
        Rp5e = Rp5r * Ic5f
        Rp7e = Rp7r * Ic7f
        Rv1e = Rv1r * Ic1f
        Rv10e = Rv10r * Ic10f
        Rv2e = Rv2r * Ic2f
        Rv4e = Rv4r * Ic4f
        Rv5e = Rv5r * Ic5f
        Rv7e = Rv7r * Ic7f
        # Les variables de haut niveau 
        Ic10e = (Ct2e - Rp10e) - Rv10e
        Ic7e = (Ct1e - Rp7e) - Rv7e
        Ic3state = jonction1f * Ic3i
        Ic6state = jonction2f * Ic6i
        Rp3e = Rp3r * jonction1f
        Rp6e = Rp6r * jonction2f
        Rv3e = Rv3r * jonction1f
        Rv6e = Rv6r * jonction2f
        Ic3e_in = ((((((See + Pres1e) - ((Rv3e + Rp3e) - Pres3e)) - Rp1e) - Rv1e) / Ic1i - (((Pres2e + ((Rv3e + Rp3e) - Pres3e)) - Rp2e) - Rv2e) / Ic2i) * Ic3i) / (1.0 + (1.0 / Ic1i + 1.0 / Ic2i) * Ic3i)
        Ic6e_in = ((((((Se1e + Pres4e) - ((Rv6e + Rp6e) - Pres6e)) - Rp4e) - Rv4e) / Ic4i - (((Pres5e + ((Rv6e + Rp6e) - Pres6e)) - Rp5e) - Rv5e) / Ic5i) * Ic6i) / (1.0 + (1.0 / Ic4i + 1.0 / Ic5i) * Ic6i)
        conduit3e = ((Ic3e_in + Rv3e) + Rp3e) - Pres3e
        conduit6e = ((Ic6e_in + Rv6e) + Rp6e) - Pres6e
        Ic1e = (((See + Pres1e) - conduit3e) - Rp1e) - Rv1e
        Ic4e = (((Se1e + Pres4e) - conduit6e) - Rp4e) - Rv4e
        Ic2e = ((Pres2e + conduit3e) - Rp2e) - Rv2e
        Ic5e = ((Pres5e + conduit6e) - Rp5e) - Rv5e
        Rp8e = (Rp8r * (Ic11f - ((Ct2e - (Ct1e - Rv8r * Ic11f)) / Rp9r) / (1.0 + (Rv8r + Rv9r) / Rp9r))) / (1.0 + Rp8r * ((1.0 / Rp9r) / (1.0 + (Rv8r + Rv9r) / Rp9r)))
        Rp9f = ((Ct2e - ((Ct1e - Rp8e) - Rv8r * Ic11f)) / Rp9r) / (1.0 + (Rv8r + Rv9r) / Rp9r)
        jonction3f = Ic11f - Rp9f
        Rv9e = Rv9r * Rp9f
        Ct2f = ((jonction1f + jonction2f) - Ic10f) - Rp9f
        Rv8e = Rv8r * jonction3f
        Ct1f = ((Ic2f + Ic5f) - Ic7f) - jonction3f
        conduit8e = (Ct1e - Rp8e) - Rv8e
        Ic11e = conduit8e - Rp11e
        conduit9e = Ct2e - (conduit8e + Rv9e)
        # Equation du système par Euler Forward
        self.Ct1state = self.Ct1state + Ts * Ct1f
        self.Ct2state = self.Ct2state + Ts * Ct2f
        self.Ic1state = self.Ic1state + Ts * Ic1e
        self.Ic10state = self.Ic10state+ Ts * Ic10e
        self.Ic11state = self.Ic11state+ Ts * Ic11e
        self.Ic2state = self.Ic2state + Ts * Ic2e
        self.Ic4state = self.Ic4state + Ts * Ic4e
        self.Ic5state = self.Ic5state + Ts * Ic5e
        self.Ic7state = self.Ic7state + Ts * Ic7e
        # Les sorties 
        self.Y['PMP01'].append(See*0.001)
        self.Y['PMP02'].append(Se1e*0.001)
        self.Y['CADC01'].append(Ic1f*1000)
        self.Y['CAPC01'].append((See - conduit3e)*0.001)
        self.Y['CADC02'].append(Ic2f*1000)
        self.Y['CADC03'].append(jonction1f*1000)
        self.Y['CADC04'].append(Ic4f*1000)
        self.Y['CAPC04'].append((Se1e - conduit6e)*0.001)
        self.Y['CADC05'].append(Ic5f*1000)
        self.Y['CADC06'].append(jonction2f*1000)
        self.Y['CANTK1'].append(self.Ct1state/At1)
        self.Y['CAPTK1'].append(Ct1e)
        self.Y['CANTK2'].append(self.Ct2state/At2)
        self.Y['CAPTK2'].append(Ct2e)
        self.Y['CADC07'].append(Ic7f*1000)
        self.Y['CAPC07'].append(((Ct1e+Pres7e)-Ic7e)*0.001)
        self.Y['CADC11'].append(Ic11f*1000)
        self.Y['CAPC11'].append(((conduit8e+Pres11e)-Ic11e)*0.001)
        self.Y['CADC10'].append(Ic10f*1000)
        self.Y['CAPC10'].append(((Ct2e+Pres10e)-Ic10e)*0.001)
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
        for i in range(100000) : 
            self.stepEulerForward(k=i)



if __name__ == '__main__' :     
    model = HydraulicModel(name="junior")
    model.pas = 0.1
    model.marge = 100000
    model.CommandePompe['PMP01'] = 1
    model.CommandePompe['PMP02'] = 1
    model.CommandeVanne['VLV02'] = 0
    model.CommandeVanne['VLV08'] = 1
    model.runModel()
    # Création de la figure
    plt.figure()

    # Tracé des courbes
    plt.plot(model.Temps, model.Y['CADC01'], 'b', label='debit')
    plt.plot(model.Temps, model.Y['CADC02'], 'r', label='Debit 2')
    #plt.plot(model.Temps, model.Y['CAPC07'], 'g', label='Debit 3')
    # Ajout d'une légende
    plt.legend()

    # Affichage de la figure
    plt.show()