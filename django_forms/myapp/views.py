from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def contact(request):    #Fonction qui va determiner ce que je dois afficher à l'utilisateur
    (form,listAvis) = recoverData(request)      
    if request.method == 'GET':     #Dans le cas d'un GET, je dois afficher le formulaire
        return render(request, 'form.html', {'form' : form} )
    if request.method == 'POST':    #Dans le cas d'un Post, je dois afficher la liste de tous les avis trouvés
        return displayResult(listAvis)

def recoverData(request):      #Fonction qui va récupérer les infos du formulaire
    listAvis = []       
    wordToSeek = None
    if request.method == 'POST':
        form = ContactForm(request.POST)    #Je récupère les données du formulaire
        if form.is_valid():
            wordToSeek = form.cleaned_data['Mot_a_chercher']    #Je récupère le mot rentré par l'utilisateur
            listAvis = seekWord(wordToSeek)     #J'appelle la fonction qui me renvoie la liste des avis qui correspondent au mot
    form = ContactForm()
    return (form, listAvis)

def seekWord(word):     #Fonction qui va chercher le mot rentré par l'utilisateur dans la base de données.
    wordFound = []        #Liste qui va stocker les avis
    file = open('DataBase/avis.txt', "r")   #J'ouvre la base de données
    line = file.readline()
    wordLower = word.lower()    #Ici je met le mot en minuscule pour ne manquer aucun mot
    while line:     #Pour chaque ligne je vais voir si je trouve le mot dans l'avis
        (author,avis) = line.split(':', 1)      
        if wordLower in avis.lower():    #Dans le cas où je l'ai trouvé je l'ajoute à ma liste
            wordFound.append((author,avis))
        line = file.readline()
    file.close()
    return wordFound

def displayResult(listAvis):    #Fonction qui va m'afficher le réultat de la recherche
    lenListAvis = len(listAvis)     #longueur de la liste des avis trouvés
    if lenListAvis == 0:
        return HttpResponse('<h1>Aucun avis trouvé</h1>')
    elif lenListAvis > 1:
        response = "<title>Web App</title><h1>" + str(lenListAvis) + " avis ont été trouvé:</h1><br>"
    else:
        response = "<title>Web App</title><h1>" + str(lenListAvis) + " avis a été trouvé:</h1><br>"
    for i in range(0,lenListAvis):     #Pour chaque avis de la liste je vais afficher son autheur ainsi que son message
        name,avis = listAvis[i]
        response += name + " a dit: " + avis + "<br>"
    return HttpResponse(response)