# ============================================================================
# controllers/player_controller.py
# ============================================================================
from models.player import Player


class PlayerController:
    """Contrôleur pour la gestion des joueurs"""

    def __init__(self, players, view, tournaments=None):
        self.players = players
        self.view = view
        self.tournaments = tournaments or []

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
                self.delete_player()
            elif choice == "6":
                break
            else:
                self.view.display_error("Option invalide !")

    def add_player(self):
        """Ajoute un nouveau joueur"""
        info = self.view.get_player_info()
        first_name, last_name, birth_date, gender, ranking = info
        player = Player(first_name, last_name, birth_date, gender, ranking)
        self.players.append(player)
        self.view.display_success(f"Joueur {player} ajouté avec succès!")

    def add_multiple_players(self):
        """Ajoute plusieurs joueurs rapidement"""
        players_data = self.view.get_multiple_players_info()

        for first_name, last_name, birth_date, gender, ranking in players_data:
            player = Player(first_name, last_name, birth_date, gender, ranking)
            self.players.append(player)

        self.view.display_success(f"{len(players_data)} joueurs ajoutés avec succès!")

    def update_player_ranking(self):
        """Modifie le classement d'un joueur"""
        if not self.players:
            self.view.display_warning("Aucun joueur enregistré.")
            self.view.pause()
            return

        self.display_all_players()
        try:
            choice = self.view.get_input("Numéro du joueur à modifier (ou 'q' pour annuler)")
            if choice.lower() == 'q':
                return
                
            index = int(choice) - 1
            if 0 <= index < len(self.players):
                new_ranking_input = self.view.get_input("Nouveau classement")
                new_ranking = int(new_ranking_input)
                self.players[index].ranking = new_ranking
                self.view.display_success(f"Classement mis à jour pour {self.players[index]}")
            else:
                self.view.display_error("Numéro invalide !")
        except ValueError:
            self.view.display_error("Entrée invalide !")
        self.view.pause()

    def display_all_players(self):
        """Affiche tous les joueurs"""
        if not self.players:
            self.view.display_info("Aucun joueur enregistré.")
            self.view.pause()
            return

        self.view.display_players_list(self.players, "LISTE DES JOUEURS")
        self.view.pause()

    def delete_player(self):
        """Supprime un joueur"""
        if not self.players:
            self.view.display_warning("Aucun joueur enregistré.")
            self.view.pause()
            return

        # Afficher la liste des joueurs
        self.display_all_players()
        
        try:
            choice = self.view.get_input("Numéro du joueur à supprimer (ou 'q' pour annuler)")
            if choice.lower() == 'q':
                return
                
            index = int(choice) - 1
            if 0 <= index < len(self.players):
                player = self.players[index]
                
                # Vérifier si le joueur est utilisé dans des tournois
                if self._is_player_in_tournament(player):
                    self.view.display_error("Impossible de supprimer ce joueur : il participe à un ou plusieurs tournois.")
                    self.view.pause()
                    return
                
                # Confirmation
                if self.view.confirm(f"Supprimer définitivement {player.first_name} {player.last_name} ?", False):
                    deleted_player = self.players.pop(index)
                    self.view.display_success(f"Joueur {deleted_player.first_name} {deleted_player.last_name} supprimé avec succès !")
                else:
                    self.view.display_info("Suppression annulée")
            else:
                self.view.display_error("Numéro invalide !")
        except ValueError:
            self.view.display_error("Entrée invalide !")
        self.view.pause()

    def _is_player_in_tournament(self, player):
        """Vérifie si un joueur est utilisé dans des tournois"""
        try:
            player_index = self.players.index(player)
            
            # Parcourir tous les tournois pour vérifier si le joueur y participe
            for tournament in self.tournaments:
                if player_index in tournament.players_indices:
                    return True
            return False
        except ValueError:
            return False