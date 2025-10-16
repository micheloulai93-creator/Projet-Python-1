Projet Python : Gestionnaire de Tournoi Suisse (Chess Swiss Tournament Manager)


Description du Projet

  Ce projet est une application autonome en console, développée en Python, pour gérer des tournois d'échecs en utilisant le Système Suisse d'appariement. Conçu pour fonctionner entièrement hors ligne, il résout les problèmes de fiabilité et de connexion Internet lente rencontrés avec les solutions existantes.

  L'architecture du programme suit le modèle Modèle-Vue-Contrôleur (MVC) pour garantir un code propre, maintenable et évolutif.


Fonctionnalités Clés

  Gestion des Joueurs : Ajout et mise à jour manuelle des  classements des joueurs dans une base de données interne.

  Création de Tournois : Configuration complète (Nom, Lieu, Date, Contrôle du temps, Description).

  Système Suisse Automatisé : Appariement automatique des joueurs basé sur l'algorithme spécifié (classement initial pour le Tour 1, points/classement pour les tours suivants).

  Saisie des Résultats : Enregistrement des scores (1, 0.5, 0) par match.

  Rapports Détaillés : Affichage des listes de joueurs (triées alphabétiquement ou par classement), des tournois, des tours et des matchs.

  Persistance des Données : Sauvegarde et chargement de l'état complet du programme (Joueurs et Tournois) à l'aide de TinyDB.


Prérequis et Installation

  Pour exécuter ce programme, vous devez avoir Python 3.x installé sur votre système (Windows, macOS, ou Linux).

  1. Cloner le Dépôt
  Bash: git clone [URL_DE_VOTRE_DEPOT]
        cd tournoi_echecs_suisse
  2. Créer et Activer l'Environnement Virtuel

     Il est fortement recommandé d'utiliser un environnement virtuel (venv) pour isoler les dépendances du projet.
     Système d'exploitation 
     
     Création de l'environnement
     
     Activation
     
     Linux/macOS: python3 -m venv venv
     
     source venv/bin/activate
     
     Windows:python -m venv venv
     
     venv\Scripts\activate

    3. Installer les Dépendances
     Les dépendances sont listées dans requirements.txt et incluent tinydb pour la persistance des données et flake8 pour l'analyse de code.

     Bash
     pip install -r requirements.txt

Utilisation
     Une fois l'environnement activé et les dépendances installées, le programme est lancé via le point d'entrée principal.

    Bash :python main.py

     L'utilisateur sera accueilli par un menu principal en console, lui permettant d'effectuer les actions suivantes :

     1.Gérer les joueurs (Ajouter, Modifier le classement).

     2.Gérer les tournois (Créer, Ajouter des joueurs, Générer des tours, Saisir les résultats).

     3.Afficher les rapports.

     5.Quitter (avec sauvegarde automatique).

     Note sur la persistance : Le programme sauvegarde automatiquement l'état (joueurs et tournois) dans un fichier db.json lors de l'exécution et le charge au démarrage.