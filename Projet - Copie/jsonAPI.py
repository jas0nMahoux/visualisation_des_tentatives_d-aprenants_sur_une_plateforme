import json


with open('bdd.json', 'r') as f:
    data = json.load(f)
f.close()

class jsonAPI:
    
    def liste_exo():
        liste_exo = []
        for elem in data:
            if elem['exercise_name'] in liste_exo:
                continue
            else:
                liste_exo.append(elem['exercise_name'])
        return liste_exo

    def liste_users():
        liste_users = []
        for elem in data:
            if elem["user"] in liste_users:
                continue
            else:
                liste_users.append(elem["user"])
        return liste_users


    # fonction qui retourne le nombre de tentative total d'un étudiant 
    def nbTentative(user):
        nbTentative = 0
        for elem in data:
            if elem['user'] == user:
                nbTentative += 1
        return nbTentative

    """
    ne pense pas que ça fonctionne voir avec J et E

    def correct(attemptId):
        i=0
        for elem in data:
            if elem['attemptId'] == attemptId:
                return elem['correct']
            else:
                continue
    """

    def attemptIDList():
        attemptIDList = []
        for elem in data:
            if elem['attemptID'] in attemptIDList:
                continue
            else:
                attemptIDList.append(elem['attemptID'])
        attemptIDList.remove(attemptIDList[0])
        return attemptIDList

    def filtre_exo(nom_exo):
        filtre_liste = []
        for elem in data:
            if elem['exercise_name'] == nom_exo:
                filtre_liste.append(elem['attemptID'])
        return filtre_liste


    def liste_exo_users(user):
        liste_exo_users = []
        for elem in data:
            if elem['exercise_name'] in liste_exo_users:
                continue
            elif elem["user"] == user:
                liste_exo_users.append(elem['exercise_name'])
        return liste_exo_users

    #liste des user_ID de l'exo nom_exo
    def filtre_exo_user(nom_exo):
        filtre_liste = []
        for elem in data:
            if elem['exercise_name'] == nom_exo:
                filtre_liste.append(str(elem['user']))
        return filtre_liste

    #liste des upload des users pour un exo
    def dico_upload_exo(nom_exo):
        liste_upload={}
        liste_attemptID = jsonAPI.filtre_exo(nom_exo)
        for elem in data:
            if elem['attemptID'] in liste_attemptID:
                if jsonAPI.get_userID(elem['attemptID']) in liste_upload.keys():
                    liste_upload[jsonAPI.get_userID(elem['attemptID'])].append([ elem['upload'], elem["correct"], elem["date"] ])
                else:
                    liste_upload.update({jsonAPI.get_userID(elem['attemptID']): [ [ elem['upload'], elem["correct"], elem["date"] ] ]})
        return liste_upload
    
    def get_userID(attemptID):
        for elem in data:
            if elem['attemptID'] == attemptID:
                return elem['user']






    """
    ------------------------------------------------------------------------------------------------------------
                                            fonction(s) de test de Anthony
    ------------------------------------------------------------------------------------------------------------
    """

    # Cette fonction prend en entrée l'identifiant d'un exercice ou nom ( jsp c'est quoi cette suite de truc mistique)
    # et retourne les identifiants des étudiants qui ont proposé au moins une réponse pour l'exercice

    def exo_ID_Done(exoID): # implémenter et fonctionnel 
        liste_users = []
        for elem in data:
            if elem['exercise_name'] == exoID:
                if elem["user"] in liste_users:
                    continue
                else:
                    liste_users.append(elem["user"])
            else:
                continue
        return liste_users


    # Cette fonction prend en entrée l'identifiant d'un exercice ou nom
    # et retourne la liste des identifiants des étudiants par tentative
    # par ex :
    # - User 1 tentative 1
    # - user 3 tentative 5
    # - user 1 tentative 2
    # la fonctione retourne ['user 1','user 3', 'user 1']
    # cette fonction facilite le graph1 dans exoID.html

    def exo_ID_Done_v2(exoID):
        liste_users = []
        for elem in data:
            if elem['exercise_name'] == exoID:
                    liste_users.append(elem["user"])
            else:
                continue
        return liste_users



    # Cette fonction prend en entrée l'id d'un étudiant et l'id d'un exercice
    # et compte le nombre de fois que l'etudiant à proposé une solution pour l'exercice
    # et retourne le résultat

    def nbTentative_exo_user(user, exoID): # implémenter et fonctionnel 
        cpt = 0
        for elem in data:
            if elem['user'] == user and elem['exercise_name'] == exoID:
                cpt += 1
        return cpt


    # Entrer : id exo et id étudiant
    # Sortie : les attempts id de l'étudiant sur cette exo

    def attempt_exo_user(user, exoID):
        list_attempt = []
        for elem in data:
            if elem['user'] == user and elem['exercise_name'] == exoID:
                list_attempt.append(elem['attemptID'])
        return list_attempt



    # Cette fonction prend en entrée la liste de toutes les tentatives
    # et retourne la liste de toutes les tentatives correct

    def display_correct_attempt(list_attempt): # fonctionnel
        list_correct_attempt = []
        for elem in data:    
            if elem['correct'] == '1':
                list_correct_attempt.append(elem['attemptID'])
            else:
                    continue
        return list_correct_attempt



    # Cette fonction prend en entrée une tentative
    # et retourne vrai si la tentative est correct sinon faux

    def correct_attempt(attemptID):#pense être fonctionnel ne sait pas si c'est utile
        res = False
        for elem in data:
            if elem['attemptID'] == attemptID and elem['correct'] == '1':
                res = True
            else:
                continue
        return res



    # Cette fonction prend en entrée une liste de tentative
    # et retourne le nombre de tentative correct

    def nb_correct_attempt(liste_attemptID):#pense être fonctionnel ne sait pas si c'est utile
        cpt = 0
        for elem in liste_attemptID:
            if  jsonAPI.correct_attempt(elem) == True:
                cpt += 1
            else:
                continue
        return cpt

    def false_0_true_1(exo_ID):
        res = []
        for elem in data:
            if elem['exercise_name'] == exo_ID:
                res.append(elem['correct'])
        return res
        



    # Cette fonction prend en entrée l'id d'un étudiant et l'id d'un exercice
    # puis compte le nombre de tentative juste et retourne ce nombre
    # En gros compte le nombre de tentative juste d'un étudiant sur un exercice précis

    def nb_correct_attempt_user_exo(user, exoID): # implémenter et fonctionnel
        cpt = 0
        for elem in data:
            if elem['user'] == user and elem['exercise_name'] == exoID:
                if elem['correct'] == '1':
                    cpt += 1
                else:
                    continue
            else:
                continue
        return cpt

    # Cette fonction prend en entrée l'id d'un exercice
    # et retourne le nombre de t'entaive fait par les étudiant sur cette exercice

    def nb_attempt_exo(exoID):
        cpt = 0
        for elem in data:
            if elem['exercise_name'] == exoID:
                cpt += 1
            else:
                continue
        return cpt

    # Cette fonction prend en entrée l'id d'un exercice
    # et retourne le nombre de t'entaive correct fait par les étudiant sur cette exercice

    def nb_attempt_exo_correct(exoID):
        cpt = 0
        for elem in data:
            if elem['exercise_name'] == exoID and elem['correct']=='1':
                cpt += 1
            else:
                continue
        return cpt

    # Cette fonction prend en entrée l'id d'un exercice
    # et retourne le nombre d'étudiant qui ont fait l'exercice 

    def nb_user_exo_done(exoID):
        cpt = 0
        list_user = []
        for elem in data:
            if elem['exercise_name'] == exoID:
                if elem['user'] in list_user:
                    continue
                else:
                    cpt += 1
                    list_user.append(elem['user'])
        return cpt

    # Cette fonction prend en entrée l'id d'un exercice
    # et retourne le nombre d'étudiant qui ont réussit l'exercice

    def nb_user_exo_done_correct(exoID):
        cpt = 0
        list_user = []
        for elem in data:
            if elem['exercise_name'] == exoID and elem['correct']=='1':
                if elem['user'] in list_user:
                    continue
                else:
                    cpt += 1
                    list_user.append(elem['user'])
        return cpt

    # Cette fonction prend en entrée l'id d'un exercice
    # et retourne le nombre d'étudiant qui ont fait l'exercice 

    def nb_user():
        list_user = []
        for elem in data:
            if elem['user'] in list_user:
                continue
            else:
                list_user.append(elem['user'])
        return len(list_user)

    # Cette fonction prend en entrée l'id d'un exercice
    # et retourne le nombre d'étudiant qui n'ont pas fait l'exercice 
    
    def nb_user_exo_dont_done(exoID):
        nb_done = jsonAPI.nb_user_exo_done(exoID)
        nb_user = 0
        list_user = jsonAPI.liste_users()
        for elem in list_user:
            nb_user += 1
        return (nb_user - nb_done)

    def display_correct_attempt_exo(exoID): # fonctionnel
        list_correct_attempt = []
        for elem in data:    
            if jsonAPI.correct_attempt(elem['attemptID']) and elem['exercise_name']== exoID:
                list_correct_attempt.append(elem['attemptID'])
            else:
                    continue
        return list_correct_attempt

        # dico['cle']=(valeur1, valeur2, valeur3)