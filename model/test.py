import matplotlib.pyplot as plt
import numpy as np
#mon code de test pour transformer ces equations en code 
X = []
Y1 = []
Y2 = []
Y3 = []
Y4 = []


for k in range(10000) : 
    # les constantes 
    See = 1000
    Rvr,Rv1r,Rv2r = 0.2 , 20 , 0.2
    Rpr,Rp1r,Rp2r = 0.8 , 0.8 , 0.8
    Ii, I1i, I2i = 3 ,3 , 3
    # Les listes pour calcul des bails
    if k == 0 :  
        Istatek1 = 0
        I1statek1 = 0
    #if k >= 100 : 
    #    Rv1r = 0.1
    #    Rv2r = 20
    # Les valeurs initaux 
    Ts = 0.01
    # La valeur du temps
    X.append(k*Ts)
    # Les equations dynamiques
    # part 1 
    If = Istatek1 / Ii
    I1f = I1statek1 / I1i
    # part 2 
    Rve = Rvr * If
    Rpe = Rpr * If
    Rv1e = Rv1r * I1f
    Rp1e = Rp1r * I1f

    Zerojunctionf = If - I1f
    I2state = Zerojunctionf * I2i
    Rv2e = Rv2r * Zerojunctionf
    Rp2e = Rp2r * Zerojunctionf

    I2ein = (((See -((Rv2e + (Rv2e+Rp2e))+Rpe))/Ii - ((Rv2e+Rp2e)-(Rv1e+Rp1e)/I1i)*I2i) / (1+(1+Ii+1/I1i)*I2i))
    Onejunction4e = (Rv2e+Rp2e)+I2ein
    Ie = See-((Rve+Onejunction4e)+Rpe)
    I1e = Onejunction4e - (Rv1e+Rp1e)

    # Les states 
    Istatek1 = Istatek1 + Ts * Ie
    I1statek1 = I1statek1 + Ts * I1e
    #print(f"debit principale = {If} : sous-debit 1 = {I1f} : sous-debit 2 = {Zerojunctionf}")
    Y1.append(If)
    Y2.append(I1f)
    Y3.append(Zerojunctionf)
    Y4.append(Onejunction4e)

# Création de la figure
plt.figure()

# Tracé des courbes
plt.plot(X, Y1, 'b', label='Debit principale')
plt.plot(X, Y2, 'r', label='Conduit 1')
plt.plot(X, Y3, 'g', label='conduit 2')
plt.plot(X, Y4, 'y', label='Pression principale')
# Ajout d'une légende
plt.legend()

# Affichage de la figure
plt.show()