from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from views.menu_view import MenuView
from database import Database


class MainController:
    """ContrÃ´leur principal de l'application"""

    def __init__(self):
        self.players = []
        self.tournaments = []
        self.view = MenuView()
        self.db = Database()
        self.load_data()

    def run(self):
        """Boucle principale du programme"""
        while True:
            choice = self.view.display_main_menu()

            if choice == "1":
                self.manage_players()
            elif choice == "2":
                self.manage_tournaments()
            elif choice == "3":
                self.display_reports()
            elif choice == "4":
                self.save_data()
            elif choice == "5":
                self.save_data()
                print("Au revoir !")
                break
            else:
                print("Option invalide !")

    def load_data(self):
        """Charge les donnÃ©es depuis la base de donnÃ©es"""
        try:
            self.players = self.db.load_players()
            self.tournaments = self.db.load_tournaments(self.players)
            if self.players or self.tournaments:
                print(f"\n Donnees charges : {len(self.players)} joueurs, "
                      f"{len(self.tournaments)} tournois")
        except Exception as e:
            print(f"\n  Erreur lors du chargement : {e}")
            print("Demarrage avec des donnees vides.")

    def save_data(self):
        """Sauvegarde les donnÃ©es dans la base de donnÃ©es"""
        try:
            self.db.save_players(self.players)
            self.db.save_tournaments(self.tournaments, self.players)
            print("\n Donnees sauvegardes avec succes¨s !")
        except Exception as e:
            print(f"\n  Erreur lors de la sauvegarde : {e}")

    def manage_players(self):
        """Gestion des joueurs"""
        while True:
            choice = self.view.display_player_menu()

            if choice == "1":
                self.add_player()
            elif choice == "2":
                self.add_multiple_players()
            elif choice == "3":
                self.update_player_ranking()
            elif choice == "4":
                self.display_all_players()
            elif choice == "5":
                break
            else:
                print("Option invalide !")

    def add_player(self):
        """Ajoute un nouveau joueur"""
        info = self.view.get_player_info()
        first_name, last_name, birth_date, gender, ranking = info
        player = Player(first_name, last_name, birth_date, gender, ranking)
        self.players.append(player)
        print(f"\n“ Joueur {player} ajoutee avec success!!")

    def add_multiple_players(self):
        """Ajoute plusieurs joueurs rapidement"""
        players_data = self.view.get_multiple_players_info()

        for first_name, last_name, birth_date, gender, ranking in players_data:
            player = Player(first_name, last_name, birth_date, gender, ranking)
            self.players.append(player)

        print(f"\n {len(players_data)} joueurs ajoutees avec success!!")

    def update_player_ranking(self):
        """Modifie le classement d'un joueur"""
        if not self.players:
            print("\nAucun joueur enregistre.")
            return

        self.display_all_players()
        try:
            index = int(input("\nNumero du joueur a  modifier : ")) - 1
            if 0 <= index < len(self.players):
                new_ranking = int(input("Nouveau classement : "))
                self.players[index].ranking = new_ranking
                print(f"\n Classement mis a  jour pour {self.players[index]}")
            else:
                print("Numero invalide !")
        except ValueError:
            print("Entree invalide !")

    def display_all_players(self):
        """Affiche tous les joueurs"""
        if not self.players:
            print("\nAucun joueur enregistre.")
            return

        print("\n=== LISTE DES JOUEURS ===")
        for i, player in enumerate(self.players, 1):
            print(f"{i}. {player}")

    def manage_tournaments(self):
        """Gestion des tournois"""
        while True:
            choice = self.view.display_tournament_menu()

            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.select_and_manage_tournament()
            elif choice == "3":
                self.display_all_tournaments()
            elif choice == "4":
                break
            else:
                print("Option invalide !")

    def create_tournament(self):
        """CrÃ©e un nouveau tournoi"""
        if len(self.players) < 8:
            print(f"\n  Vous devez avoir au moins 8 joueurs. "
                  f"Vous en avez {len(self.players)}.")
            return

        tournament_info = self.view.get_tournament_info()
        tournament = Tournament(*tournament_info)

        # SÃ©lectionner 8 joueurs
        print("\n=== SELECTION DES 8 JOUEURS ===")
        self.display_all_players()

        for i in range(8):
            while True:
                try:
                    player_num = int(input(f"\nJoueur {i + 1}/8 - "
                                           f"Entrez le numero : ")) - 1
                    if 0 <= player_num < len(self.players):
                        if player_num not in tournament.players_indices:
                            tournament.add_player_index(player_num)
                            print(f" {self.players[player_num]} "
                                  f"ajoutee au tournoi")
                            break
                        else:
                            print("Ce joueur est deja  selectionne !")
                    else:
                        print("Numero invalide !")
                except ValueError:
                    print("Entree invalide !")

        self.tournaments.append(tournament)
        print(f"\n Tournoi '{tournament.name}' creer avec succes¨s !")

    def select_and_manage_tournament(self):
        """SÃ©lectionne un tournoi et le gÃ¨re"""
        if not self.tournaments:
            print("\nAucun tournoi creer.")
            return

        self.display_all_tournaments()
        try:
            index = int(input("\nNumero du tournoi a  gerer : ")) - 1
            if 0 <= index < len(self.tournaments):
                self.manage_single_tournament(self.tournaments[index])
            else:
                print("Numero invalide !")
        except ValueError:
            print("Entree invalide !")

    def manage_single_tournament(self, tournament):
        """GÃ¨re un tournoi spÃ©cifique"""
        while True:
            choice = self.view.display_single_tournament_menu(tournament)

            if choice == "1":
                self.start_new_round(tournament)
            elif choice == "2":
                self.enter_round_results(tournament)
            elif choice == "3":
                self.display_tournament_status(tournament)
            elif choice == "4":
                break
            else:
                print("Option invalide !")

    def start_new_round(self, tournament):
        """DÃ©marre un nouveau tour"""
        if tournament.is_complete():
            print("\n Le tournoi est termine !")
            return

        if tournament.current_round > 0:
            last_round = tournament.rounds[-1]
            if not last_round.end_time:
                print("\n  Terminez le tour en cours avant d'en "
                      "commencer un nouveau !")
                return

        round_number = tournament.current_round + 1
        new_round = Round(f"Round {round_number}")
        new_round.start_round()

        # GÃ©nÃ©rer les paires
        pairs = self.generate_pairs(tournament)

        for player1_idx, player2_idx in pairs:
            match = Match(self.players[player1_idx],
                          self.players[player2_idx])
            new_round.add_match(match)

        tournament.add_round(new_round)
        print(f"\n {new_round.name} demarrer !")
        self.display_round_matches(new_round)

    def generate_pairs(self, tournament):
        """GÃ©nÃ¨re les paires selon le systÃ¨me suisse"""
        player_indices = tournament.players_indices[:]

        if tournament.current_round == 0:
            # Premier tour : trier par classement
            player_indices.sort(
                key=lambda idx: self.players[idx].ranking,
                reverse=True
            )

            # Diviser en deux moitiÃ©s
            mid = len(player_indices) // 2
            top_half = player_indices[:mid]
            bottom_half = player_indices[mid:]

            pairs = [(top_half[i], bottom_half[i]) for i in range(mid)]
        else:
            # Tours suivants : trier par score puis classement
            player_indices.sort(key=lambda idx: (
                self.players[idx].score,
                self.players[idx].ranking
            ), reverse=True)

            pairs = []
            available = player_indices[:]

            while len(available) >= 2:
                player1 = available.pop(0)

                # Chercher un adversaire non encore affrontÃ©
                paired = False
                for i, player2 in enumerate(available):
                    if not self.have_played_together(
                            tournament, player1, player2):
                        pairs.append((player1, player2))
                        available.pop(i)
                        paired = True
                        break

                # Si tous dÃ©jÃ  affrontÃ©s, prendre le premier disponible
                if not paired and available:
                    player2 = available.pop(0)
                    pairs.append((player1, player2))

        return pairs

    def have_played_together(self, tournament, player1_idx, player2_idx):
        """VÃ©rifie si deux joueurs se sont dÃ©jÃ  affrontÃ©s"""
        for round_obj in tournament.rounds[:-1]:
            for match in round_obj.matches:
                p1 = self.players.index(match.player1)
                p2 = self.players.index(match.player2)
                if ((p1 == player1_idx and p2 == player2_idx) or
                        (p1 == player2_idx and p2 == player1_idx)):
                    return True
        return False

    def display_round_matches(self, round_obj):
        """Affiche les matchs d'un tour"""
        print(f"\n=== {round_obj.name} ===")
        for i, match in enumerate(round_obj.matches, 1):
            print(f"Match {i}: {match}")

    def enter_round_results(self, tournament):
        """Saisit les rÃ©sultats d'un tour"""
        if tournament.current_round == 0:
            print("\n  Aucun tour n'a ete demarrer !")
            return

        current_round = tournament.rounds[-1]
        if current_round.end_time:
            print("\n  Ce tour est deja  terminer !")
            return

        print(f"\n=== SAISIE DES RÃ‰SULTATS - {current_round.name} ===")

        for i, match in enumerate(current_round.matches, 1):
            print(f"\nMatch {i}: {match.player1} vs {match.player2}")
            print("1. Victoire de", match.player1.first_name)
            print("2. Victoire de", match.player2.first_name)
            print("3. Match nul")

            while True:
                choice = input("Resultat : ")
                if choice == "1":
                    match.set_result(1, 0)
                    match.player1.score += 1
                    break
                elif choice == "2":
                    match.set_result(0, 1)
                    match.player2.score += 1
                    break
                elif choice == "3":
                    match.set_result(0.5, 0.5)
                    match.player1.score += 0.5
                    match.player2.score += 0.5
                    break
                else:
                    print("Choix invalide !")

        current_round.end_round()
        print(f"\n“ {current_round.name} termine !")

    def display_tournament_status(self, tournament):
        """Affiche l'Ã©tat du tournoi"""
        print(f"\n=== {tournament.name} ===")
        print(f"Lieu : {tournament.location}")
        print(f"Tours : {tournament.current_round}/{tournament.number_of_rounds}")
        print(f"ContrÃ´le du temps : {tournament.time_control}")

        print("\n--- Classement actuel ---")
        players_with_scores = [
            (self.players[idx], self.players[idx].score)
            for idx in tournament.players_indices
        ]
        players_with_scores.sort(
            key=lambda x: (x[1], x[0].ranking),
            reverse=True
        )

        for i, (player, score) in enumerate(players_with_scores, 1):
            print(f"{i}. {player} - {score} points")

    def display_all_tournaments(self):
        """Affiche tous les tournois"""
        if not self.tournaments:
            print("\nAucun tournoi creer.")
            return

        print("\n=== LISTE DES TOURNOIS ===")
        for i, tournament in enumerate(self.tournaments, 1):
            status = "Termine" if tournament.is_complete() else "En cours"
            print(f"{i}. {tournament} - {status}")

    def display_reports(self):
        """Affiche le menu des rapports"""
        while True:
            choice = self.view.display_reports_menu()

            if choice == "1":
                self.report_all_players_alpha()
            elif choice == "2":
                self.report_all_players_ranking()
            elif choice == "3":
                self.report_tournament_players()
            elif choice == "4":
                self.display_all_tournaments()
            elif choice == "5":
                self.report_tournament_rounds()
            elif choice == "6":
                self.report_tournament_matches()
            elif choice == "7":
                break
            else:
                print("Option invalide !")

    def report_all_players_alpha(self):
        """Liste tous les joueurs par ordre alphabetique"""
        if not self.players:
            print("\nAucun joueur enregistree.")
            return

        sorted_players = sorted(
            self.players,
            key=lambda p: (p.last_name, p.first_name)
        )
        print("\n=== JOUEURS (ordre alphabetique) ===")
        for player in sorted_players:
            print(player)

    def report_all_players_ranking(self):
        """Liste tous les joueurs par classement"""
        if not self.players:
            print("\nAucun joueur enregistrer.")
            return

        sorted_players = sorted(
            self.players,
            key=lambda p: p.ranking,
            reverse=True
        )
        print("\n=== JOUEURS (par classement) ===")
        for player in sorted_players:
            print(player)

    def report_tournament_players(self):
        """Liste les joueurs d'un tournoi"""
        if not self.tournaments:
            print("\nAucun tournoi creer.")
            return

        self.display_all_tournaments()
        try:
            index = int(input("\nNumero du tournoi : ")) - 1
            if 0 <= index < len(self.tournaments):
                tournament = self.tournaments[index]
                print(f"\n=== JOUEURS DU TOURNOI '{tournament.name}' ===")
                print("1. Ordre alphabetique")
                print("2. Par classement")
                choice = input("Choix : ")

                tournament_players = [
                    self.players[idx]
                    for idx in tournament.players_indices
                ]

                if choice == "1":
                    tournament_players.sort(
                        key=lambda p: (p.last_name, p.first_name)
                    )
                elif choice == "2":
                    tournament_players.sort(
                        key=lambda p: p.ranking,
                        reverse=True
                    )

                for player in tournament_players:
                    print(player)
            else:
                print("Numero invalide !")
        except ValueError:
            print("Entrer invalide !")

    def report_tournament_rounds(self):
        """Liste les tours d'un tournoi"""
        if not self.tournaments:
            print("\nAucun tournoi creer.")
            return

        self.display_all_tournaments()
        try:
            index = int(input("\nNumero du tournoi : ")) - 1
            if 0 <= index < len(self.tournaments):
                tournament = self.tournaments[index]
                print(f"\n=== TOURS DU TOURNOI '{tournament.name}' ===")
                for round_obj in tournament.rounds:
                    print(round_obj)
            else:
                print("Numero invalide !")
        except ValueError:
            print("Entrer invalide !")

    def report_tournament_matches(self):
        """Liste tous les matchs d'un tournoi"""
        if not self.tournaments:
            print("\nAucun tournoi creer.")
            return

        self.display_all_tournaments()
        try:
            index = int(input("\nNumero du tournoi : ")) - 1
            if 0 <= index < len(self.tournaments):
                tournament = self.tournaments[index]
                print(f"\n=== MATCHS DU TOURNOI '{tournament.name}' ===")
                for round_obj in tournament.rounds:
                    print(f"\n{round_obj.name}:")
                    for match in round_obj.matches:
                        print(f"  {match}")
            else:
                print("Numero invalide !")
        except ValueError:
            print("Entrer invalide !")
