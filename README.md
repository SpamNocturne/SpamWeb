# _*SpamWeb*_
LE site web du Spam Nocturne !
![Engagement Qualité !](http://verandas-tahon.fr/wp-content/uploads/2013/02/Fotolia_38099128_XS-e1362571952133.jpg)

## Objectifs
SpamWeb est un projet communautaire dont les objectifs principaux sont :
* Calculs SpamMistiques (statistiques du Spam).
* Gestion des SpamMembres (membres du Spam).
* Planification des SpamEvents (évènements organisés par et pour le spam).
* Jauge de pinte de chouffe à boire chaque semaine.
* ...
* Tout ce dont le spam a besoin pour manquer de sérieux en amphi ! 

## Techs
Le site est développé grâce à [Python3](https://www.python.org/) et au Framework [Django](http://www.django-fr.org/).   
La  base de donnée utilise MySql.   


## Liens utiles 
* **Video explicative** pour **l'installation** de Python et Django sur Windows : [ici](https://www.youtube.com/watch?v=Zn6dx8v8x_w).   
  *NB:* (_Loïc_) La partie dans la vidéo concernant les wsgi.so ne semble pas obligatoire.
* **Tutoriels/TP** sur Django : [ici](http://django-story.readthedocs.org/en/latest/).   
  *NB:* Ce tutoriel est écrit par le même auteur que le tuto d'openclassroom, mais il est ici plus complet.   
* **Tutoriels** sur Python : [ici](https://openclassrooms.com/courses/apprenez-a-programmer-en-python).   
* **Documentation** Française pour Django 1.8 : [ici](https://docs.djangoproject.com/fr/1.8/).
* **IDE PyCharm** Meilleur IDE Python (gratuit :) ): [ici](https://www.jetbrains.com/pycharm/download/).


## Lancer le site en local
A la racine du projet :
* Lancer le serveur : `python manage.py runserver PORC`   
  où _PORC_ est le port (_ex:8081_) de connection au site.


## Installation (testé sur windows7)
* Installer [Python3](https://www.python.org/)   
  *NB:* Pensez a mettre a jour la variable **PATH** pour lui ajouter les chemins `C:\Python34\Scripts` et `C:\Python34`.   
* Executer [ez_setup.py](https://pypi.python.org/pypi/ez_setup)   
* Executer `easy_install pip` : pip étant le gestoinnaire de package, à utiliser pour les téléchargements de packages
* Obtenir Django avec : `pip install django`   
* Telecharger le client mysql, qui fournira la DB API driver : `pip install mysqlclient`   

## Configuration 
Le fichier `settings.py`étant versionné, nous devons respecter ses conditions c'est à dire :   
* Avoir créé une Base de donnée MySQL :   
 * Nom de la base : `webspam-bdd`   
 * Utilisateur : `root`  
 * Mot de passe : *(vide)*   
 * Host : *(defaut localhost)*   

Il faut ensuite executer une la commande `python manage.py migrate` une première fois. Cela va créer les tables nécessaires aux applications installées par défaut.
