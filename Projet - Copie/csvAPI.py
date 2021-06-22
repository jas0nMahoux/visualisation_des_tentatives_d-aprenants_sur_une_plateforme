import csv
from os import remove 
import string
import re
from jsonAPI import jsonAPI

with open('Embeddings.csv',"r") as file:
    donneeCSV = list(csv.reader(file))
file.close()

class csvAPI:
    #Affiche le csv
    def show_csv():
        csvList = []
        for elem in donneeCSV:
            csvList.append(elem)
        return csvList

    def Donnees(ID):
        res2 = csvAPI.show_csv()
        #récupération des données pour l'ID choisi
        res2.remove(res2[0])
        res3 = res2[int(ID)]
        données_ID = []
        données_final = []
        for elem in res3:
            #recherche des \n et compile en caractère spéciaux.
            regex = re.compile(r'[\n\r\t]')
            #remplace les caractères spéciaux par " " (espace)
            elem = regex.sub(" ", elem)
            #transforme la chaîne de caractères en list via la methode split
            données_ID.append(elem.split())
        for elem2 in données_ID[0]:
            données_final.append(float(elem2))
        return données_final

    def listeDonnees():
        data = jsonAPI.attemptIDList()
        res = []
        for elem in data :
            res.append(csvAPI.Donnees(elem))
        return res

    def liste_vecteur(nom_exo):
        attemptID = jsonAPI.filtre_exo(nom_exo)
        vecteur = []
        for elem in attemptID:
            vecteur.append(csvAPI.Donnees(elem))
        return vecteur


    # Cette fonction prend en entrée une liste de tentative
    # et retourne leur coordonnées

    def vecteur_attempt(list_attempt):
        list_vecteur = []
        for elem in list_attempt:
            list_vecteur.append(csvAPI.Donnees(elem))
        return list_vecteur


