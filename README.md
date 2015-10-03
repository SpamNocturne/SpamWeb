# _*SpamWeb*_ [![Build Status](https://travis-ci.org/SpamNocturne/SpamWeb.svg?branch=master)](https://travis-ci.org/SpamNocturne/SpamWeb)
### LE site web du *Spam Nocturne* !   
![Engagement Qualité !](http://verandas-tahon.fr/wp-content/uploads/2013/02/Fotolia_38099128_XS-e1362571952133.jpg)
![Engagement Qualité !](http://verandas-tahon.fr/wp-content/uploads/2013/02/Fotolia_38099128_XS-e1362571952133.jpg)

## Objectifs
SpamWeb est un projet communautaire dont les objectifs principaux sont :
* Calculs SpamMistiques (statistiques du Spam).
* Gestion des SpamMembres (membres du Spam).
* Planification des SpamEvents (évènements organisés par et pour le spam).
* Jauge de pinte de chouffe à boire chaque semaine.
* Quantité de tacos ingurgités
* Système de régulation de comptes entre membres (en UDI)
* Partage d'idées avec votes et commentaires
* ...
* Tout ce dont le spam a besoin pour manquer de sérieux en amphi ! 

## Techs
Le site est développé grâce à [Python3](https://www.python.org/) et au Framework [Django](http://www.django-fr.org/).   
La  base de donnée utilise MySql.  
Design basé sur [AdminLTE](https://almsaeedstudio.com/)   
Avec l'utilisation de [Bootstrap](http://getbootstrap.com/), [JQuery](https://jquery.com/) et [JQueryUI](http://jqueryui.com/)


## Liens utiles 
* **Video explicative** pour **l'installation** de Python et Django sur Windows : [ici](https://www.youtube.com/watch?v=Zn6dx8v8x_w).   
  *NB:* (_Loïc_) La partie dans la vidéo concernant les wsgi.so ne semble pas obligatoire.
* **Tutoriels/TP** sur Django : [ici](http://django-story.readthedocs.org/en/latest/).   
  *NB:* Ce tutoriel est écrit par le même auteur que le tuto d'openclassroom, mais il est ici plus complet.   
* **Tutoriels** sur Python : [ici](https://openclassrooms.com/courses/apprenez-a-programmer-en-python).   
* **Documentation** Française pour Django 1.8 : [ici](https://docs.djangoproject.com/fr/1.8/).
* **IDE PyCharm** Meilleur IDE Python & Django (gratuit :) ): [ici](https://www.jetbrains.com/pycharm/download/).    
 *NB:* La version professional est **gratuite** pour les étudiants, avec le mail INSA ! Pour ça inscrivez vous [ici](https://www.jetbrains.com/student/)   


## Lancer le site en local
A la racine du projet :
* Lancer le serveur : `python manage.py runserver PORC`   
  où _PORC_ est le port (_ex:8081_) de connection au site. Par défaut 8000 si non renseigné.


## Installation (testé sur windows7)
###Python et Django
* installer python anaconda (python + pas mal de package dont django sont installés) : [anaconda](http://continuum.io/downloads#py34)

ou bien 

* Installer [Python3](https://www.python.org/)
  *NB:* Pensez a mettre a jour la variable **PATH** pour lui ajouter les chemins `C:\Python34\Scripts` et `C:\Python34`.   
* Executer [ez_setup.py](https://pypi.python.org/pypi/ez_setup)   
* Executer `easy_install pip` : pip étant le gestionnaire de packages, à utiliser pour les téléchargements de packages
* Obtenir Django avec : `pip install django`   
* Telecharger le client mysql, qui fournira la DB API driver : `pip install mysqlclient`   
* Si vous avez des problèmes sous Windaub et mysql : suivre le tuto [ici](http://stackoverflow.com/questions/28251314/error-microsoft-visual-c-10-0-is-required-unable-to-find-vcvarsall-bat)
pour pouvoir installer mysql python

###Base de données
Vous avez le choix : 
* pour MySQL, il suffit d'aller ici : [MySQL](https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-web-community-5.6.25.0.msi)
* Suivre les instructions
* Créer une base de données (schema en mysql)

## Configuration 
### Base de donnée
Le fichier `settings.py`étant versionné, nous devons respecter certaines conditions c'est à dire.
Vous devez créer un fichier `SpamWeb/databases.py` dans lequel vous mettrez la configuration de votre base
de données en vous inspirant du fichier `databases-example.py`.

Il faut ensuite executer une la commande `python manage.py migrate` une première fois. Cela va créer les tables nécessaires aux applications installées par défaut.

### librairies
* Utiliser Pip pour installer oauth : ``pip install --upgrade oauth2client`` [oauth2](https://github.com/google/oauth2client)
* Ensuite installer  Google APIs Client Library for Python : ``pip install --upgrade google-api-python-client`` [lien](https://developers.google.com/api-client-library/python/start/installation?hl=fr)
* /!\ pour python3 : appliquer la correction de ce commit : [lien](https://github.com/SpamNocturne/SpamWeb/commit/94094aa29d6002b76962df2953aa24a425f067ed)

* Pour le SpamAlyzer, lxml est nécessaire. Très simple à installer sur les systèmes UNIX. Un peu tricky à installer sur Windows, je conseille de passer sur Anaconda et de ne pas se prendre la tête. Sinon ``pip install lxml	``.

### Super utilisateur
Pour acceder à l'interface d'administration et se connecter sur le site avec un premier utilisateur, il faut créer un super administrateur :
Grâce à la commande : `python manage.py createsuperuser`

* super-user spamadmin pour accéder au spammusic :)

--------------------------------------------------------------------

## Fonctionnement et commandes de Django :
### *Pour modifier le modèle et la base de donnée :*   
* Modifiez les modèles (dans `models.py`).   
* Exécutez `python manage.py makemigrations` pour créer des migrations correspondant à ces changements.   
* Exécutez `python manage.py migrate` pour appliquer ces modifications à la base de données.   


## Développer une nouvelle fonctionnalité :
### Participez au développement du site ! :D
Pour vous aider a créer un nouvelle application (*monApp*) sur le site voici quelques conseils :    
1. Créer l'application avec `python manage.py startapp monApp`  
2. Mettre *monApp* dans la variable `INSTALLED_APPS` pour l'ajouter au site dans le fichier **SpamWeb/setting.py**  
3. Ajouter une route de base du type `url(r'^maroute/', include('monApp.urls', namespace='monApp'))` dans **SpamWeb/urls.py** auteur = models.ForeignKey(User, related_name='idees')  
4. Développer *monApp*  
  
* *Pour les* **modèles** *:*  
 * Vous pouvez établir des relations avec les utilisateurs en définissant une clé étrangère sur la classe `User`, importés comme ceci : `from django.contrib.auth.models import User`  
 * Pour établir cette relation penser à nommer la relation inverse c'est plus pratique, comme ceci : `Class Pouce(models.Model):` puis `user = models.ForeignKey(User, related_name='pouces')`  
  
* *Pour les* **vues** *(contrôleurs)* :  
  * Penser à ajouter le décorateur `@login_required` au dessus de vos actions, les utilisateurs déconnectés seront directement redirigés vers la page de connexion  
  * Ajouter une route vers votre action et nommez la dans **monApp/urls.py** (créez le fichier si besoin) comme ceci : `urlpatterns = [ url(r'^', views.index, name='index'),]`  
  
* *Pour les* **templates** *:*  
  * Copier le fichier **LTE/templates/LTE/starter.html**, et le renommer en **layout.html** dans **monApp/templates/monApp/**  
  * Adapter et redéfinir tout les blocks du **layout.html** pour *monApp*  
  * Ce fichier **layout.html** sera la base de votre application, toutes vos pages seront basées dessus  
  * Créer maintenant un *nouveau* template basé sur le fichier **LTE/templates/LTE/page.html**   
  * Faire donc hériter le nouveau template de **monApp/templates/monApp/layout.html**   
  * Modifier le contenu de ce fichier pour qu'il corresponde à votre page   
  * *C'est bon !* Le templating en 3 couches (Base / Layout / Page) est terminé ! 
  * Si vous utilisez de l'**AJAX** passez par l'app ajax qui centralise ces requetes. Un **jeton csrf** est obligatoire même en ajax ! Infos [ici](https://docs.djangoproject.com/fr/1.7/ref/contrib/csrf/#csrf-ajax).   

### Bonne chance ! :)

