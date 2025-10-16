# ============================================================================
# controllers/main_controller.py
# ============================================================================
from views.menu_view import MenuView
from database import Database
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from controllers.round_controller import RoundController


class MainController:
    """Contrôleur principal de l'application"""

    def __init__(self):
        self.players = []
        self.tournaments = []
        self.view = MenuView()
        self.db = Database()

        # Initialisation des sous-contrôleurs - CORRIGÉ
        self.player_controller = PlayerController(self.players, self.view, self.tournaments)  # ← AJOUT de self.tournaments
        self.round_controller = RoundController(self.players, self.view)  # ← AJOUT de self.view
        self.tournament_controller = TournamentController(
            self.players,
            self.tournaments,
            self.view,
            self.round_controller
        )
        self.report_controller = ReportController(
            self.players,
            self.tournaments,
            self.view
        )

        self.load_data()

    def run(self):
        """Boucle principale du programme"""
        while True:
            choice = self.view.display_main_menu()

            if choice == "1":
                self.player_controller.manage_players()
            elif choice == "2":
                self.tournament_controller.manage_tournaments()
            elif choice == "3":
                self.report_controller.display_reports()
            elif choice == "4":
                self.save_data()
            elif choice == "5":
                self.save_data()
                print("Au revoir !")
                break
            else:
                print("Option invalide !")

    def load_data(self):
        """Charge les données depuis la base de données"""
        try:
            self.players = self.db.load_players()
            self.tournaments = self.db.load_tournaments(self.players)

            # Mise à jour des références dans les contrôleurs
            self._update_controller_references()

            if self.players or self.tournaments:
                print(f"\n✓ Données chargées : {len(self.players)} joueurs, "
                      f"{len(self.tournaments)} tournois")
        except Exception as e:
            print(f"\n⚠ Erreur lors du chargement : {e}")
            print("Démarrage avec des données vides.")

    def save_data(self):
        """Sauvegarde les données dans la base de données"""
        try:
            print(f"\n💾 Sauvegarde en cours...")
            print(f"📊 {len(self.players)} joueurs à sauvegarder")
            print(f"🏆 {len(self.tournaments)} tournois à sauvegarder")
            
            # Sauvegarde réelle
            self.db.save_players(self.players)
            self.db.save_tournaments(self.tournaments, self.players)
            
            # Message de confirmation FORCÉ
            print(f"\n✅ DONNÉES SAUVEGARDÉES AVEC SUCCÈS !")
            print(f"✅ {len(self.players)} joueurs sauvegardés")
            print(f"✅ {len(self.tournaments)} tournois sauvegardés")
            
            # Vérification fichier
            import os
            if os.path.exists('db.json'):
                file_size = os.path.getsize('db.json')
                print(f"📁 Fichier: db.json ({file_size} octets)")
            else:
                print("❌ Fichier db.json non trouvé")
                
            input("\n↵ Appuyez sur ENTREE pour continuer...")
            
        except Exception as e:
            print(f"\n❌ ERREUR LORS DE LA SAUVEGARDE : {e}")
            import traceback
            traceback.print_exc()
            input("\n↵ Appuyez sur ENTREE pour continuer...")

    def _update_controller_references(self):
        """Met à jour les références des listes dans les contrôleurs"""
        self.player_controller.players = self.players
        self.player_controller.tournaments = self.tournaments  # ← AJOUTÉ
        self.round_controller.players = self.players
        self.tournament_controller.players = self.players
        self.tournament_controller.tournaments = self.tournaments
        self.report_controller.players = self.players
        self.report_controller.tournaments = self.tournaments