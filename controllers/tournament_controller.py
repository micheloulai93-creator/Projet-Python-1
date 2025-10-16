# ============================================================================
# controllers/tournament_controller.py
# ============================================================================
from models.tournament import Tournament


class TournamentController:
    """Contrôleur pour la gestion des tournois"""

    def __init__(self, players, tournaments, view, round_controller):
        self.players = players
        self.tournaments = tournaments
        self.view = view
        self.round_controller = round_controller

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
                self.delete_tournament()
            elif choice == "5":
                break
            else:
                print("❌ Option invalide !")

    def create_tournament(self):
        """Crée un nouveau tournoi"""
        if len(self.players) < 8:
            print(f"⚠ Vous devez avoir au moins 8 joueurs. Vous en avez {len(self.players)}.")
            input("Appuyez sur Entrée pour continuer...")
            return  # ← CORRIGÉ : BIEN ALIGNÉ

        tournament_info = self.view.get_tournament_info()
        tournament = Tournament(*tournament_info)

        # Sélectionner 8 joueurs
        if self._select_tournament_players(tournament):
            self.tournaments.append(tournament)
            print(f"✓ Tournoi '{tournament.name}' créé avec succès !")
        else:
            print("❌ Création du tournoi annulée")

    def _select_tournament_players(self, tournament):
        """Sélectionne les 8 joueurs pour un tournoi"""
        print("\n" + "="*50)
        print("SELECTION DES 8 JOUEURS")
        print("="*50)
        
        selected_count = 0
        while selected_count < 8:
            # Afficher les joueurs disponibles
            available_players = []
            for i, player in enumerate(self.players):
                if i not in tournament.players_indices:
                    available_players.append((i, player))
            
            if not available_players:
                print("❌ Plus de joueurs disponibles !")
                return False

            # Afficher les joueurs disponibles
            print("\n--- JOUEURS DISPONIBLES ---")
            for idx, player in available_players:
                print(f"{idx + 1}. {player.first_name} {player.last_name} - Classement: {player.ranking}")
            
            try:
                player_choice = input(f"\nJoueur {selected_count + 1}/8 - Entrez le numéro (ou 'q' pour annuler): ")
                if player_choice.lower() == 'q':
                    return False
                    
                player_num = int(player_choice) - 1
                original_idx = available_players[player_num][0] if 0 <= player_num < len(available_players) else -1
                
                if 0 <= player_num < len(available_players) and original_idx not in tournament.players_indices:
                    tournament.add_player_index(original_idx)
                    selected_player = self.players[original_idx]
                    print(f"✓ {selected_player.first_name} {selected_player.last_name} ajouté au tournoi")
                    selected_count += 1
                else:
                    print("❌ Numéro invalide ou joueur déjà sélectionné !")
            except (ValueError, IndexError):
                print("❌ Entrée invalide !")

        return True

    def select_and_manage_tournament(self):
        """Sélectionne un tournoi et le gère"""
        if not self.tournaments:
            print("⚠ Aucun tournoi créé.")
            input("Appuyez sur Entrée pour continuer...")
            return

        self.display_all_tournaments()
        
        try:
            choice = input("\nNuméro du tournoi à gérer (ou 'q' pour annuler): ")
            if choice.lower() == 'q':
                return
                
            index = int(choice) - 1
            if 0 <= index < len(self.tournaments):
                self.manage_single_tournament(self.tournaments[index])
            else:
                print("❌ Numéro invalide !")
        except ValueError:
            print("❌ Entrée invalide !")

    def manage_single_tournament(self, tournament):
        """Gère un tournoi spécifique"""
        while True:
            choice = self.view.display_single_tournament_menu(tournament)

            if choice == "1":
                self.round_controller.start_new_round(tournament)
            elif choice == "2":
                self.round_controller.enter_round_results(tournament)
            elif choice == "3":
                self.display_tournament_status(tournament)
            elif choice == "4":
                break
            else:
                print("❌ Option invalide !")

    def display_tournament_status(self, tournament):
        """Affiche l'état du tournoi"""
        print(f"\n=== ÉTAT DU TOURNOI - {tournament.name} ===")
        
        # Informations générales
        print(f"Description: {tournament.description or 'Aucune description'}")
        print(f"Lieu: {tournament.location}")
        print(f"Dates: {tournament.start_date} - {tournament.end_date}")
        print(f"Tours: {tournament.current_round}/{tournament.number_of_rounds}")
        print(f"Contrôle du temps: {tournament.time_control.upper()}")
        print(f"Statut: {'Terminé' if tournament.is_complete() else 'En cours'}")
        
        # Classement actuel
        if tournament.players_indices:
            players_with_scores = []
            for idx in tournament.players_indices:
                player = self.players[idx]
                players_with_scores.append(player)
            
            # Trier par score
            players_with_scores.sort(key=lambda p: p.score, reverse=True)
            
            # Afficher le classement
            print(f"\n--- CLASSEMENT ---")
            for i, player in enumerate(players_with_scores, 1):
                print(f"{i}. {player.first_name} {player.last_name} - {player.score} points")
        else:
            print("⚠ Aucun joueur dans ce tournoi")
        
        input("\nAppuyez sur Entrée pour continuer...")

    def display_all_tournaments(self):
        """Affiche tous les tournois"""
        if not self.tournaments:
            print("ℹ Aucun tournoi créé.")
            input("Appuyez sur Entrée pour continuer...")
            return

        print("\n=== LISTE DES TOURNOIS ===")
        
        # Afficher sous forme simple
        for i, tournament in enumerate(self.tournaments, 1):
            status = "Terminé" if tournament.is_complete() else "En cours"
            print(f"{i}. {tournament.name} - {tournament.location} - {status}")
        
        print()

    def delete_tournament(self):
        """Supprime un tournoi"""
        if not self.tournaments:
            print("⚠ Aucun tournoi créé.")
            input("Appuyez sur Entrée pour continuer...")
            return

        # Afficher la liste des tournois
        self.display_all_tournaments()
        
        try:
            choice = input("\nNuméro du tournoi à supprimer (ou 'q' pour annuler): ")
            if choice.lower() == 'q':
                return
                
            index = int(choice) - 1
            if 0 <= index < len(self.tournaments):
                tournament = self.tournaments[index]
                
                # Vérifier si le tournoi est en cours
                if not tournament.is_complete():
                    print("⚠ Attention : ce tournoi n'est pas terminé !")
                
                # Confirmation simple
                confirm = input(f"Supprimer le tournoi '{tournament.name}' ? (o/n): ")
                if confirm.lower() in ['o', 'oui', 'y']:
                    deleted_tournament = self.tournaments.pop(index)
                    print(f"✓ Tournoi '{deleted_tournament.name}' supprimé avec succès !")
                else:
                    print("ℹ Suppression annulée")
            else:
                print("❌ Numéro invalide !")
        except ValueError:
            print("❌ Entrée invalide !")
        input("Appuyez sur Entrée pour continuer...")

    def _display_all_players(self):
        """Affiche tous les joueurs (méthode helper)"""
        if not self.players:
            print("ℹ Aucun joueur enregistré.")
            return
        
        print("\n=== LISTE DES JOUEURS ===")
        for i, player in enumerate(self.players, 1):
            print(f"{i}. {player.first_name} {player.last_name} - Classement: {player.ranking}")