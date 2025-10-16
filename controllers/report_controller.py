# ============================================================================
# controllers/report_controller.py
# ============================================================================

class ReportController:
    """Contrôleur pour la génération des rapports"""

    def __init__(self, players, tournaments, view):
        self.players = players
        self.tournaments = tournaments
        self.view = view

    def display_reports(self):
        """Affiche le menu des rapports"""
        while True:
            choice = self.view.display_reports_menu()

            if choice == "1":
                self.report_all_players_alpha()
            elif choice == "2":
                self.report_all_players_ranking()
            elif choice == "3":
                self.report_tournament_players()  # ← CORRIGÉ : Était report_controller.display_reports()
            elif choice == "4":
                self.report_all_tournaments()  # ← CORRIGÉ : Était _display_all_tournaments()
            elif choice == "5":
                self.report_tournament_rounds()
            elif choice == "6":
                self.report_tournament_matches()
            elif choice == "7":
                break
            else:
                self.view.display_error("Option invalide !")

    def report_all_players_alpha(self):
        """Liste tous les joueurs par ordre alphabétique"""
        if not self.players:
            self.view.display_warning("Aucun joueur enregistré.")
            self.view.pause()
            return

        sorted_players = sorted(
            self.players,
            key=lambda p: (p.last_name.lower(), p.first_name.lower())
        )
        self.view.display_players_list(sorted_players, "JOUEURS - ORDRE ALPHABÉTIQUE")
        self.view.pause()

    def report_all_players_ranking(self):
        """Liste tous les joueurs par classement"""
        if not self.players:
            self.view.display_warning("Aucun joueur enregistré.")
            self.view.pause()
            return

        sorted_players = sorted(
            self.players,
            key=lambda p: p.ranking,
            reverse=True
        )
        self.view.display_players_list(sorted_players, "JOUEURS - PAR CLASSEMENT")
        self.view.pause()

    def report_tournament_players(self):
        """Liste les joueurs d'un tournoi"""
        if not self.tournaments:
            self.view.display_warning("Aucun tournoi créé.")
            self.view.pause()
            return

        tournament = self._select_tournament()
        if not tournament:
            return

        # Menu de tri pour les joueurs du tournoi
        options = {
            "1": "Ordre alphabétique",
            "2": "Par classement"
        }
        choice = self.view.get_choice(options, "Mode de tri")

        tournament_players = [self.players[idx] for idx in tournament.players_indices]

        if choice == "1":
            tournament_players.sort(key=lambda p: (p.last_name.lower(), p.first_name.lower()))
            title = f"JOUEURS - {tournament.name} - ALPHABÉTIQUE"
        elif choice == "2":
            tournament_players.sort(key=lambda p: p.ranking, reverse=True)
            title = f"JOUEURS - {tournament.name} - PAR CLASSEMENT"
        else:
            self.view.display_error("Option invalide !")
            return

        self.view.display_players_list(tournament_players, title)
        self.view.pause()

    def report_all_tournaments(self):
        """Affiche tous les tournois"""
        if not self.tournaments:
            self.view.display_warning("Aucun tournoi créé.")
            self.view.pause()
            return

        self.view.print_section("LISTE DE TOUS LES TOURNOIS")
        for i, tournament in enumerate(self.tournaments, 1):
            self.view.display_tournament_card(tournament, i)
        self.view.pause()

    def report_tournament_rounds(self):
        """Liste les tours d'un tournoi"""
        if not self.tournaments:
            self.view.display_warning("Aucun tournoi créé.")
            self.view.pause()
            return

        tournament = self._select_tournament()
        if not tournament:
            return

        if not tournament.rounds:
            self.view.display_warning("Aucun tour dans ce tournoi")
            self.view.pause()
            return

        self.view.print_section(f"TOURS - {tournament.name}")
        for round_obj in tournament.rounds:
            self.view.display_round_summary(round_obj)
        self.view.pause()

    def report_tournament_matches(self):
        """Liste tous les matchs d'un tournoi"""
        if not self.tournaments:
            self.view.display_warning("Aucun tournoi créé.")
            self.view.pause()
            return

        tournament = self._select_tournament()
        if not tournament:
            return

        self.view.print_section(f"TOUS LES MATCHS - {tournament.name}")
        
        total_matches = 0
        for round_num, round_obj in enumerate(tournament.rounds, 1):
            if hasattr(round_obj, 'matches') and round_obj.matches:
                self.view.print_section(f"{round_obj.name}")
                for match_num, match in enumerate(round_obj.matches, 1):
                    self.view.display_match_result(match, match_num)
                    total_matches += 1
            else:
                self.view.display_info(f"Aucun match dans {round_obj.name}")
        
        if total_matches == 0:
            self.view.display_warning("Aucun match enregistré dans ce tournoi")
        
        self.view.pause()

    def _select_tournament(self):
        """Sélectionne un tournoi dans la liste"""
        self.report_all_tournaments()  # Affiche la liste des tournois
        
        try:
            choice = self.view.get_input("Numéro du tournoi (ou 'q' pour annuler)")
            if choice.lower() == 'q':
                return None
                
            index = int(choice) - 1
            if 0 <= index < len(self.tournaments):
                return self.tournaments[index]
            else:
                self.view.display_error("Numéro invalide !")
                return None
        except ValueError:
            self.view.display_error("Entrée invalide !")
            return None

    def _display_tournament_players_sorted(self, tournament):
        """Affiche les joueurs d'un tournoi triés (méthode helper)"""
        # Cette méthode n'est plus utilisée, remplacée par report_tournament_players()
        pass