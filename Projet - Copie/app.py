from flask import Flask, redirect, url_for, request, render_template
from jsonAPI import jsonAPI
from csvAPI import csvAPI
from TSNE import tsneAPI

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/listeExo')
def liste_exo():
    
    liste_Exercice = []
    chartDico = {}
    liste_Exercice = jsonAPI.liste_exo()

    for elem in liste_Exercice:
        chartDico.update({elem : [jsonAPI.nb_user_exo_done_correct(elem), jsonAPI.nb_user()-jsonAPI.nb_user_exo_done_correct(elem), jsonAPI.nb_attempt_exo_correct(elem), jsonAPI.nb_attempt_exo(elem)-jsonAPI.nb_attempt_exo_correct(elem)]})

    return render_template('/pages/listeExo.html', 
                            chartDico = chartDico, 
                            listeExo = liste_Exercice)

@app.route('/listeUsers')
def liste_Users():
    return render_template('/pages/listeUsers.html', listeUsers = jsonAPI.liste_users())
    
@app.route('/-<user>')
def afficheExoUser(user):
    return render_template('/pages/displayExoUser.html', 
                            list_exo = jsonAPI.liste_exo_users(user), 
                            user = user,
                            nombreTentative = jsonAPI.nbTentative(user))

@app.route('/--<exoUserID>')
def exoUserID(exoUserID):
    
    nb_tentative_correct = []
    nb_tentative = []
    liste_user = []

    liste_user = jsonAPI.exo_ID_Done(exo_ID)
    for elem in liste_user:
        nb_tentative.append(jsonAPI.nbTentative_exo_user(elem, exo_ID))
        nb_tentative_correct.append(jsonAPI.nb_correct_attempt_user_exo(elem, exo_ID))

    #---------------------Construction du datasets---------------------
    liste_0_1 = []
    liste_0_1 = jsonAPI.false_0_true_1(exo_ID)
    dataX_v2 = tsneAPI.abcsisse(exo_ID)
    dataY_v2 = tsneAPI.ordonee(exo_ID)
    Datasets_v2=[]
    labels_v2 = jsonAPI.filtre_exo_user(exo_ID)
    i=0
    for i in range(len(labels_v2)):
        if liste_0_1[i] == '1':
            Datasets_v2.append({ "labelV": labels_v2[i],
                            "data": [{'x':dataX_v2[i],'y':dataY_v2[i]}],
                            "borderColor": 'green',
                            "fill": 'false',
                            "type": "scatter",
                            "backgroundColor":'green',
                            "pointHoverBackgroundColor": 'rgb(100, 148, 237)'})
        else:
            Datasets_v2.append({ "labelF": labels_v2[i],
                            "data": [{'x':dataX_v2[i],'y':dataY_v2[i]}],
                            "borderColor": 'red',
                            "fill": 'false',
                            "type": "scatter",
                            "backgroundColor":'red',
                            "pointHoverBackgroundColor": 'rgb(100, 148, 237)'})
    

    #-------------------------------------------------------------------

    Datasets=[]
    labels = jsonAPI.filtre_exo_user(exo_ID)
    i=0
    Datasets.append({ "label": labels[0],
                    "data": [{'x':dataX_v2[0],'y':dataY_v2[0]}],
                    "borderColor": 'rgb(75, 192, 192)',
                    "fill": 'false',
                    "type": "scatter",
                    "backgroundColor":'rgba(75, 192, 192, 0.2)',
                    "pointHoverBackgroundColor": 'red'})
    labels.remove(labels[0])
    for elem in labels:
        Temp=False
        for x in Datasets:
            if elem == x["label"]:
                x["data"].append({'x':dataX_v2[i+1], 'y': dataY_v2[i+1]})
                Temp=True
                break
        if Temp == False:
            Datasets.append({ "label": labels[i],
                        "data": [{'x':dataX_v2[i+1],'y':dataY_v2[i+1]}],
                        "fill": 'false',
                        "type": "scatter",
                        "borderColor": 'rgb(75, 192, 192)',
                        "backgroundColor":'rgba(75, 192, 192, 0.2)',
                        "pointHoverBackgroundColor": 'red'})
        i+=1
    
    #-----------------------------------
    for elem in Datasets:
        Datasets_v2.append(elem)


    return render_template('/pages/exoID.html', 
                            exoID = exo_ID,
                            exoID_Done = liste_user,
                            nb_tentative = nb_tentative,
                            nb_tentative_correct = nb_tentative_correct,
                            Datasets = Datasets,
                            Datasets_v2 = Datasets_v2,
                            liste_upload = jsonAPI.dico_upload_exo(exo_ID))

@app.route('/<exo_ID>')
def exo_ID(exo_ID):
    
    nb_tentative_correct = []
    nb_tentative = []
    liste_user = []

    liste_user = jsonAPI.exo_ID_Done(exo_ID)
    for elem in liste_user:
        nb_tentative.append(jsonAPI.nbTentative_exo_user(elem, exo_ID))
        nb_tentative_correct.append(jsonAPI.nb_correct_attempt_user_exo(elem, exo_ID))

    #---------------------Construction du datasets---------------------
    liste_0_1 = []
    liste_0_1 = jsonAPI.false_0_true_1(exo_ID)
    dataX_v2 = tsneAPI.abcsisse(exo_ID)
    dataY_v2 = tsneAPI.ordonee(exo_ID)
    Datasets_v2=[]
    labels_v2 = jsonAPI.filtre_exo_user(exo_ID)
    i=0
    if liste_0_1[0] == '1':
        Datasets_v2.append({ "labelV": labels_v2[i],
                        "data": [{'x':dataX_v2[i],'y':dataY_v2[i]}],
                        "borderColor": 'green',
                        "fill": 'false',
                        "type": "scatter",
                        "backgroundColor":'green',
                        "pointHoverBackgroundColor": 'rgb(100, 148, 237)'})
    else:
        Datasets_v2.append({ "labelF": labels_v2[i],
                        "data": [{'x':dataX_v2[i],'y':dataY_v2[i]}],
                        "borderColor": 'red',
                        "fill": 'false',
                        "type": "scatter",
                        "backgroundColor":'red',
                        "pointHoverBackgroundColor": 'rgb(100, 148, 237)'})
    i+=1
    for i in range(len(labels_v2)):
        if liste_0_1[i] == '1':
            Datasets_v2.append({ "labelV": labels_v2[i],
                            "data": [{'x':dataX_v2[i],'y':dataY_v2[i]}],
                            "borderColor": 'green',
                            "fill": 'false',
                            "type": "scatter",
                            "backgroundColor":'green',
                            "pointHoverBackgroundColor": 'rgb(100, 148, 237)'})
        else:
            Datasets_v2.append({ "labelF": labels_v2[i],
                            "data": [{'x':dataX_v2[i],'y':dataY_v2[i]}],
                            "borderColor": 'red',
                            "fill": 'false',
                            "type": "scatter",
                            "backgroundColor":'red',
                            "pointHoverBackgroundColor": 'rgb(100, 148, 237)'})
    

    #-------------------------------------------------------------------

    Datasets=[]
    labels = jsonAPI.filtre_exo_user(exo_ID)
    i=0
    Datasets.append({ "label": labels[0],
                    "data": [{'x':dataX_v2[0],'y':dataY_v2[0]}],
                    "borderColor": 'rgb(75, 192, 192)',
                    "fill": 'false',
                    "type": "scatter",
                    "backgroundColor":'rgba(75, 192, 192, 0.2)',
                    "pointHoverBackgroundColor": 'red'})
    labels.remove(labels[0])
    for elem in labels:
        Temp=False
        for x in Datasets:
            if elem == x["label"]:
                x["data"].append({'x':dataX_v2[i+1], 'y': dataY_v2[i+1]})
                Temp=True
                break
        if Temp == False:
            Datasets.append({ "label": labels[i],
                        "data": [{'x':dataX_v2[i+1],'y':dataY_v2[i+1]}],
                        "fill": 'false',
                        "type": "scatter",
                        "borderColor": 'rgb(75, 192, 192)',
                        "backgroundColor":'rgba(75, 192, 192, 0.2)',
                        "pointHoverBackgroundColor": 'red'})
        i+=1
    
    #-----------------------------------
    for elem in Datasets:
        Datasets_v2.append(elem)


    return render_template('/pages/exoID.html', 
                            exoID = exo_ID,
                            exoID_Done = liste_user,
                            nb_tentative = nb_tentative,
                            nb_tentative_correct = nb_tentative_correct,
                            Datasets = Datasets,
                            Datasets_v2 = Datasets_v2,
                            liste_upload = jsonAPI.dico_upload_exo(exo_ID))

if __name__ == '__main__':
    app.run(debug=True)





                            