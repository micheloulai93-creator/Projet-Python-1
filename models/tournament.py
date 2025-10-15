class Tournament:
    """ModÃ¨le reprÃ©sentant un tournoi d'Ã©checs"""

    def __init__(self, name, location, start_date, end_date,
                 number_of_rounds=4, time_control="blitz", description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.time_control = time_control
        self.description = description
        self.rounds = []
        self.players_indices = []
        self.current_round = 0

    def add_player_index(self, player_index):
        """Ajoute l'indice d'un joueur au tournoi"""
        if len(self.players_indices) < 8:
            self.players_indices.append(player_index)
            return True
        return False

    def add_round(self, round_obj):
        """Ajoute un tour au tournoi"""
        self.rounds.append(round_obj)
        self.current_round += 1

    def is_complete(self):
        """VÃ©rifie si le tournoi est terminÃ©"""
        return self.current_round >= self.number_of_rounds

    def __str__(self):
        return f"{self.name} - {self.location} ({self.start_date})"
