from datetime import datetime


class Round:
    """ModÃ¨le reprÃ©sentant un tour du tournoi"""

    def __init__(self, name):
        self.name = name
        self.matches = []
        self.start_time = None
        self.end_time = None

    def start_round(self):
        """Marque le dÃ©but du tour"""
        self.start_time = datetime.now()

    def end_round(self):
        """Marque la fin du tour"""
        self.end_time = datetime.now()

    def add_match(self, match):
        """Ajoute un match au tour"""
        self.matches.append(match)

    def __str__(self):
        if self.end_time:
            status = "TerminÃ©"
        elif self.start_time:
            status = "En cours"
        else:
            status = "Pas commencÃ©"
        return f"{self.name} - {status} - {len(self.matches)} matchs"
