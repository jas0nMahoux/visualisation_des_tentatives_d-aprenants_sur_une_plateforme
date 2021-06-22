import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from csvAPI import csvAPI



class tsneAPI:

    # fonction qui retourne la liste des abscisses des tentatives associé à l'execice exo
    def abcsisse(exo):
        samples = csvAPI.liste_vecteur(exo) # fonction qui récupere les vecteurs à 100 dimensions associé à l'exercice exo  

        model = TSNE(learning_rate=50)

        transformed = model.fit_transform(samples)

        xs = transformed[:,0]
        x = []
        for elem in xs:
            x.append(elem)
        return x
    
    # fonction qui retourne la liste des ordonées des tentatives associé à l'execice exo
    def ordonee(exo):
        samples = csvAPI.liste_vecteur(exo) # fonction qui récupere les vecteurs à 100 dimensions associé à l'exercice exo

        model = TSNE(learning_rate=50)

        transformed = model.fit_transform(samples)

        ys = transformed[:,1]
        y = []
        for elem in ys:
            y.append(elem)
        return y

    def abcsisse_ordonee(nom_exo):
        coordonee_final = []
        x = tsneAPI.abcsisse(nom_exo)
        y = tsneAPI.ordonee(nom_exo)
        for i in range(len(x)):
            coordonee_final.append([])
        cpt=0
        for elem in coordonee_final:
            elem.append(x[cpt])
            elem.append(y[cpt])
            cpt+=1
        return coordonee_final






    def list_attempt_abcsisse(list_attempt_vector):

        samples = list_attempt_vector

        model = TSNE(learning_rate=50)

        transformed = model.fit_transform(samples)

        xs = transformed[:,0]
        x = []
        for elem in xs:
            x.append(elem)
        return x

    def list_attempt_ordonee(list_attempt_vector):
        samples = list_attempt_vector

        model = TSNE(learning_rate=50)

        transformed = model.fit_transform(samples)

        ys = transformed[:,1]
        y = []
        for elem in ys:
            y.append(elem)
        return y
    
    def liste_coord_final(liste_X, liste_Y):
        coordonee_final = []
        for i in range(len(liste_X)):
            coordonee_final.append([])
        cpt=0
        for elem in coordonee_final:
            elem.append(liste_X[cpt])
            elem.append(liste_Y[cpt])
            cpt+=1
        return coordonee_final



#plt.show()


#"2864c9e5861229d2ff32570f6bc944fb" "70ae7ad6cf504e0fa8cedebd8e8a825f"
#"908defc05cefcce7d5707781c7f9e500"
