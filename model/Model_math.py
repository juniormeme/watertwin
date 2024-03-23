import matplotlib.pyplot as plt
import numpy as np
#mon code de test pour transformer ces equations en code 
X = []
Y1 = []
Y2 = []
Y3 = []
Y4 = []
Y5 = []
    
    
for k in range(100000) :   
    # Arrangement des equations 
    See , Se1e = 285,285
    Rv1r,Rv2r,Rv3r,Rv4r,Rv5r,Rv6r,Rv7r,Rv8r,Rv9r,Rv10r = 1,1,1,1,1,1,1,1,1,1 # Pour les pertes de charges aux vannes 
    Rp1r,Rp2r,Rp3r=73556.43181,80600.0174,80600.0174
    Rp4r,Rp5r,Rp6r = 84701.34572,80600.0174,80600.0174
    Rp8r,Rp9r = 5349.558677,4457.965564
    Rp7r,Rp10r,Rp11r = 111449.1391,111449.1391,113232.3253
    Ct1c , Ct2c = 0.005526694 , 0.005526694 #Les capacités de tank 
    Ic1i,Ic2i,Ic3i = 7580258.303,8306125.461,8306125.461
    Ic4i,Ic5i,Ic6i = 8728782.288,8306125.461,8306125.461
    Ic7i,Ic10i,Ic11i = 11485239.85,11485239.85,11669003.69 # Les inerties des tuyaux 
    # pas de discretisation 
    Ts = 0.01 
    X.append(k*Ts) # la valeur du temps 
    # Les etats initiaux des states 
    if k == 0 : 
        Ct1state = 0
        Ct2state = 0 
        Ic1state = 0 
        Ic10state = 0 
        Ic11state = 0 
        Ic2state = 0 
        Ic4state = 0 
        Ic6state = 0 
        Ic7state = 0 
    # les actions de commutations 
    if k >= 50000 : 
        Rv1r = 13985716.43
    #dynamic equations
    # Les variables liées aux states 
    Ct1e = Ct1state / Ct1c 
    Ct2e = Ct2state / Ct2c
    Ic1f = Ic1state / Ic1i
    Ic10f = Ic10state / Ic10i
    Ic11f = Ic11state / Ic11i
    Ic2f = Ic2state / Ic2i
    Ic4f = Ic4state / Ic4i
    Ic6f = Ic6state / Ic6i
    Ic7f = Ic7state / Ic7i
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
    Ct1state = Ct1state + Ts * Ct1f
    Ct2state = Ct2state + Ts * Ct2f
    Ic1state = Ic1state + Ts * Ic1e
    Ic10state = Ic10state + Ts * Ic10e 
    Ic11state = Ic11state + Ts * Ic11e
    Ic2state = Ic2state + Ts * Ic2e
    Ic4state = Ic4state + Ts * Ic4e
    Ic6state = Ic6state + Ts * Ic6e
    Ic7state = Ic7state + Ts * Ic7e 
    # les sorties à afficher 
    Y1.append(Ic1f)
    Y2.append(Ic2f)
    Y3.append(ZeroJunctionf)
    Y4.append(See-Conduit3e)

# Création de la figure
plt.figure()

# Tracé des courbes
#plt.plot(X, Y5, 'c', label='Target')
plt.plot(X, Y1, 'b', label='Debit 1')
plt.plot(X, Y2, 'r', label='Debit 2')
plt.plot(X, Y3, 'g', label='Debit 3')
#plt.plot(X, Y4, 'y', label='Pression principale')
# Ajout d'une légende
plt.legend()

# Affichage de la figure
plt.show()