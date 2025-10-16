# ============================================================================
# controllers/round_controller.py
# ============================================================================
from models.round import Round
from models.match import Match


class RoundController:
    """Contrôleur pour la gestion des tours et matchs"""

    def __init__(self, players, view=None):
        self.players = players
        self.view = view

    def set_view(self, view):
        """Définit la vue pour le contrôleur"""
        self.view = view

    def start_new_round(self, tournament):
        """Démarre un nouveau tour"""
        if tournament.is_complete():
            self.view.display_success("Le tournoi est terminé !")
            return

        if tournament.current_round > 0:
            last_round = tournament.rounds[-1]
            if not last_round.end_time:
                self.view.display_warning("Terminez le tour en cours avant d'en commencer un nouveau !")
                return

        round_number = tournament.current_round + 1
        new_round = Round(f"Round {round_number}")
        new_round.start_round()

        # Générer les paires
        pairs = self.generate_pairs(tournament)

        for player1_idx, player2_idx in pairs:
            match = Match(self.players[player1_idx],
                          self.players[player2_idx])
            new_round.add_match(match)

        tournament.add_round(new_round)
        self.view.display_success(f"{new_round.name} démarré !")
        self.display_round_matches(new_round)

    def generate_pairs(self, tournament):
        """Génère les paires selon le système suisse"""
        player_indices = tournament.players_indices[:]

        if tournament.current_round == 0:
            return self._generate_first_round_pairs(player_indices)
        else:
            return self._generate_subsequent_round_pairs(
                tournament, player_indices
            )

    def _generate_first_round_pairs(self, player_indices):
        """Génère les paires du premier tour"""
        # Premier tour : trier par classement
        player_indices.sort(
            key=lambda idx: self.players[idx].ranking,
            reverse=True
        )

        # Diviser en deux moitiés
        mid = len(player_indices) // 2
        top_half = player_indices[:mid]
        bottom_half = player_indices[mid:]

        pairs = [(top_half[i], bottom_half[i]) for i in range(mid)]
        return pairs

    def _generate_subsequent_round_pairs(self, tournament, player_indices):
        """Génère les paires des tours suivants"""
        # Tours suivants : trier par score puis classement
        player_indices.sort(key=lambda idx: (
            self.players[idx].score,
            self.players[idx].ranking
        ), reverse=True)

        pairs = []
        available = player_indices[:]

        while len(available) >= 2:
            player1 = available.pop(0)

            # Chercher un adversaire non encore affronté
            paired = False
            for i, player2 in enumerate(available):
                if not self.have_played_together(
                        tournament, player1, player2):
                    pairs.append((player1, player2))
                    available.pop(i)
                    paired = True
                    break

            # Si tous déjà affrontés, prendre le premier disponible
            if not paired and available:
                player2 = available.pop(0)
                pairs.append((player1, player2))

        return pairs

    def have_played_together(self, tournament, player1_idx, player2_idx):
        """Vérifie si deux joueurs se sont déjà affrontés"""
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
        if self.view:
            self.view.display_round_summary(round_obj)
        else:
            # Fallback si pas de vue
            print(f"\n=== {round_obj.name} ===")
            for i, match in enumerate(round_obj.matches, 1):
                print(f"Match {i}: {match}")
        self.view.pause()

    def enter_round_results(self, tournament):
        """Saisit les résultats d'un tour"""
        if tournament.current_round == 0:
            self.view.display_warning("Aucun tour n'a été démarré !")
            self.view.pause()
            return

        current_round = tournament.rounds[-1]
        if current_round.end_time:
            self.view.display_warning("Ce tour est déjà terminé !")
            self.view.pause()
            return

        self.view.print_section(f"SAISIE DES RÉSULTATS - {current_round.name}")

        for i, match in enumerate(current_round.matches, 1):
            # Afficher le match avec la vue professionnelle
            self.view.display_match_pairing(i, match.player1, match.player2)
            
            options = {
                "1": f"Victoire de {match.player1.first_name}",
                "2": f"Victoire de {match.player2.first_name}", 
                "3": "Match nul"
            }
            
            choice = self.view.get_choice(options, "Résultat du match")
            
            if choice == "1":
                match.set_result(1, 0)
                match.player1.score += 1
                self.view.display_success(f"Victoire de {match.player1.first_name} !")
            elif choice == "2":
                match.set_result(0, 1)
                match.player2.score += 1
                self.view.display_success(f"Victoire de {match.player2.first_name} !")
            elif choice == "3":
                match.set_result(0.5, 0.5)
                match.player1.score += 0.5
                match.player2.score += 0.5
                self.view.display_info("Match nul enregistré")
            else:
                self.view.display_error("Choix invalide !")
                continue

        current_round.end_round()
        self.view.display_success(f"{current_round.name} terminé !")
        self.view.pause()

    def display_tournament_standings(self, tournament):
        """Affiche le classement du tournoi"""
        if not tournament.players_indices:
            self.view.display_warning("Aucun joueur dans ce tournoi")
            self.view.pause()
            return

        # Créer une liste de joueurs avec leurs scores
        players_with_scores = []
        for player_idx in tournament.players_indices:
            player = self.players[player_idx]
            players_with_scores.append(player)

        # Trier par score (décroissant)
        players_with_scores.sort(key=lambda p: p.score, reverse=True)

        # Afficher avec la vue professionnelle
        self.view.display_tournament_standings(players_with_scores, f"CLASSEMENT - {tournament.name}")
        self.view.pause()