# PROJET VISUALISATION

## Lancer le serveur
### WINDOWS
1- pip3 install -r requirements.txt    
2- set FLASK_APP=flask_engine.py    
3- flask run    

### LINUX
1- pip3 install -r requirements.txt    
2- export FLASK_APP=flask_engine.py    
3- flask run    

## Dictionnaire des catastrophes

{
"earthquakes":[liste de tremblements de terres comme dans le dataset],

"volcanos":[idem pour les volcans],

"tsunamis":[idem pour les tsunamis]
}


# Presentation
```
Notre utilisateur type a besoins d'informations pour un endroit précis
En premier lieu, il doit rentrer des coordonées

1) Rentrer directement les coordonées
2) Cliquer sur un endroit de la carte
3) Indiquer une adresse et ensuite cliquer sur la carte

32.75 ; 130.75

Page contenant toutes les catastrophes ayant eu lieu dans un rayon autour des coord

En dessous, un historique sur les deux derniers siècles de ces catastrophes

A gauche, un résumé sur le nb de

L'utilisateur peut changer le rayon à sa guise s'il veut une zone + précise et la visu s'adapte

Enfin l'utilisateur peut cliquer sur une catastrophe pour avoir les informations précise de cette catastrophe

Sur un volcan, l'utilisateur aura le nb d'erruptions et il pourra les faire défiler

Dans ce cas ci, risque probable de tremblement de terres car précédent proche et bcp de dégats
=> justification refuser d'aménager ou accepter à conditions de mesures anti-tremblemment de terre
=> présenter la carte et l'annoter s'il faut

Maintenant, si l'utilisateur veut pourvoir comparer avec un autre terrain

33.1 ; 130.75

Il peut comparer les 2 cartes et les 2 lignes du temps + comparaison du nb de volcans,...
Il peut toujours changer le rayon

Il peut ici voir ici que le 2e terrain est plus éloigné des tremblements de terres et est donc probablement moins risqué

S'il a d'autres terrains à comparer, il peut changer le moins bon et garder le meilleur à chaque fois```