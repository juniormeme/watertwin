import math  

# pour la communication des commandes entre les programmes 
def readCommand(): 
    dico = {}
    with open("../Water Twin by MEME/communication/command.txt","r") as fich:
        for ligne in fich.readlines(): 
            ligne = ligne.split(" : ")
            dico[str(ligne[0])] = int(ligne[1])   
        fich.close()
    return dico

def writeCommand(commande): 
    with open("../Water Twin by MEME/communication/command.txt","w") as fich:
        for clé, valeur in commande.items() :
            fich.write(f"{clé} : {valeur}\n")
        
        fich.close()
        
# pour la communication des données de capteurs virtuels 
def readValues(): 
    dico = {}
    with open("../Water Twin by MEME/communication/capture.txt","r") as fich:
        for ligne in fich.readlines(): 
            ligne = ligne.split(" : ")
            dico[str(ligne[0])] = float(ligne[1])   
        fich.close()
    return dico

def writeValues(commande): 
    with open("../Water Twin by MEME/communication/capture.txt","w") as fich:
        for clé, valeur in commande.items() :
            fich.write(f"{clé} : {valeur}\n")
        fich.close()



if __name__ == '__main__': 
    writeValues({
        "Junior" : 1,
    })
    
    print(readValues())