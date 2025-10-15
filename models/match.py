class Match:
    """ModÃ¨le reprÃ©sentant un match entre deux joueurs"""

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def set_result(self, score1, score2):
        """DÃ©finit le rÃ©sultat du match (1-0, 0-1, ou 0.5-0.5)"""
        self.score1 = score1
        self.score2 = score2

    def get_match_tuple(self):
        """Retourne le match sous forme de tuple"""
        return ([self.player1, self.score1], [self.player2, self.score2])

    def __str__(self):
        return f"{self.player1} ({self.score1}) vs {self.player2} ({self.score2})"
