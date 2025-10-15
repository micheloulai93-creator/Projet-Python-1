class MenuView:
    """GÃ¨re l'affichage des menus"""

    @staticmethod
    def display_main_menu():
        print("\n" + "=" * 50)
        print("=== GESTIONNAIRE DE TOURNOIS D'ECHECS ===")
        print("=" * 50)
        print("1. Gestion des joueurs")
        print("2. Gestion des tournois")
        print("3. Rapports")
        print("4. Sauvegarder les donnes")
        print("5. Quitter")
        return input("\nChoisissez une option : ")

    @staticmethod
    def display_player_menu():
        print("\n=== GESTION DES JOUEURS ===")
        print("1. Ajouter un joueur")
        print("2. Ajouter 8 joueurs rapidement")
        print("3. Modifier le classement d'un joueur")
        print("4. Afficher tous les joueurs")
        print("5. Retour au menu principal")
        return input("\nChoisissez une option : ")

    @staticmethod
    def get_player_info():
        """Demande les informations d'un nouveau joueur"""
        print("\n=== NOUVEAU JOUEUR ===")
        first_name = input("Prenom : ")
        last_name = input("Nom : ")
        birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
        gender = input("Sexe (M/F) : ")
        ranking = int(input("Classement : "))
        return first_name, last_name, birth_date, gender, ranking

    @staticmethod
    def get_multiple_players_info(count=8):
        """Demande les informations de plusieurs joueurs rapidement"""
        print(f"\n=== AJOUT RAPIDE DE {count} JOUEURS ===")
        players_data = []

        for i in range(count):
            print(f"\n--- Joueur {i + 1}/{count} ---")
            first_name = input("Prenom : ")
            last_name = input("Nom : ")
            birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
            gender = input("Sexe (M/F) : ")
            ranking = int(input("Classement : "))

            players_data.append((first_name, last_name, birth_date, gender, ranking))

        return players_data

    @staticmethod
    def display_tournament_menu():
        print("\n=== GESTION DES TOURNOIS ===")
        print("1. Creer un nouveau tournoi")
        print("2. Gerer un tournoi existant")
        print("3. Afficher tous les tournois")
        print("4. Retour au menu principal")
        return input("\nChoisissez une option : ")

    @staticmethod
    def get_tournament_info():
        """Demande les informations d'un nouveau tournoi"""
        print("\n=== NOUVEAU TOURNOI ===")
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        start_date = input("Date de debut (JJ/MM/AAAA) : ")
        end_date = input("Date de fin (JJ/MM/AAAA) : ")
        number_of_rounds = input("Nombre de tours (defaut 4) : ")
        number_of_rounds = int(number_of_rounds) if number_of_rounds else 4

        print("\nContrÃ´le du temps :")
        print("1. Bullet")
        print("2. Blitz")
        print("3. Rapid")
        time_choice = input("Choix : ")
        time_control = {
            "1": "bullet",
            "2": "blitz",
            "3": "rapid"
        }.get(time_choice, "blitz")

        description = input("Description (optionnel) : ")

        return (name, location, start_date, end_date,
                number_of_rounds, time_control, description)

    @staticmethod
    def display_single_tournament_menu(tournament):
        print(f"\n=== GESTION DU TOURNOI : {tournament.name} ===")
        print(f"Tour actuel : {tournament.current_round}/{tournament.number_of_rounds}")
        print("\n1. Demarrer un nouveau tour")
        print("2. Entrer les resultats du tour en cours")
        print("3. Afficher l'etat du tournoi")
        print("4. Retour")
        return input("\nChoisissez une option : ")

    @staticmethod
    def display_reports_menu():
        print("\n=== RAPPORTS ===")
        print("1. Tous les joueurs (alphabetique)")
        print("2. Tous les joueurs (par classement)")
        print("3. Joueurs d'un tournoi")
        print("4. Tous les tournois")
        print("5. Tours d'un tournoi")
        print("6. Matchs d'un tournoi")
        print("7. Retour au menu principal")
        return input("\nChoisissez une option : ")