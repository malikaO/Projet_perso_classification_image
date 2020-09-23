# Projet_perso_classification_image

Projet de classification d'image avec un modèle non supervisé.
Data set: MINST 


L'objectif de ce projet était de faire une classification d'image avec un algorithme non supervisé.
Il fallait:
- un algorithme d'apprentissage non supervisé
- une application
- une automatisation de notification
- en bonus mettre les images dans une base de données.


Le choix des images a été la première difficulté, plus précisément comment s'y prendre pour créer un dataset sans label comment l'algo va reconnaître les classes?
Les rares exemples de classifications d'images en non supervisé sont sur MINST ou digits de sklearn parce qu'il est facile de séparer les targets des features et
on peut ensuite comparer les prédictions des labels réels. Je me suis alors dirigé vers le dataset MINST. 

Du coup avec les dataset MINST, il n'est pas utile ce créer de base de donnée sur mongodb car les images ne sont pas en local.

Ensuite l'automatisation des notifs a pris beaucoup de temps.  J'ai été confronté au problème d'autorisation des boîtes mails.
Le code fonctionne mais gmail bloque l'api même si je spécifie que c'est mon action. J'ai créé un compte Outlook je n'ai pas réussit à détourner les autorisations.
Il y a un moyen d'après mes recherches d'une part c'est bien compliqué et d'une autre part j'ai surtout peur que ça déjoue la sécurité des boîtes mails.
Il semblerait que ça soit déconseillé. Du coup j'ai chercher une autre façon de faire et j'ai trouver une petite perle (notify) qui envoie des notifs 
sur l'ordi ou sur le téléphone. Et c'est simple à installer!!!

Pour l'application streamlit finalement j'ai dû utiliser opencv pour redimensionner les nouvelles images à prédire.

Pour conclure, les nouvelles prédictions ne sont pas satisfaisantes. Soit mon modèle est à revoir et/ou c'est un problème d'écriture manuscrite.
N'étant pas entraîné sur mon écriture est ce que le modèle a du mal à reconnaître les nombre correctement. Le modèle est-il aussi sensible à l'écriture manuscrite?
C'est une question à creuser! Où tout simplement que le modèle non supervisé n'est pas adapté et qu'un modèle CNN aurait était plus pertinent.


Soures:
https://notify.run/

https://python.doctor/page-python-envoyer-mail-smtp

https://stackabuse.com/how-to-send-emails-with-gmail-using-python/

https://towardsdatascience.com/automatic-notification-to-email-with-python-810fd357d89c

https://medium.com/datadriveninvestor/k-means-clustering-for-imagery-analysis-56c9976f16b6
