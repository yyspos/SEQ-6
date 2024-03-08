Pour créer la base de données sur votre serveur :  
--------------------------------
1° - Connectez vous à votre serveur en SSH  
2° - Executer les commande suivante : **python3 init_db.py**  
Votre base de données est à présent opérationnelle (Le fichier database.db à été créé dans votre répertoire sur le serveur)
Vous pouvez, si vous le souhaitez, tappez la commande **ls** dans votre console pour voir la présence de la base de données.

LES ROUTES
-------------------------------------------
/  
Pointe sur le fichier helloWorld d'accueil  

/lecture  
L'accès est conditionner à un contrôle d'accès  

/authentification  
Page d'authentification (admin, password)  

/fiche_client/1  
Permet de faire un filtre sur un client. Vous pouvez changer la valeur de 1 par le N° du client de votre choix  

/consultation/  
Permet de consutler la base de données  

/enregistrer_client  
API pour enregistrer un nouveau client  




