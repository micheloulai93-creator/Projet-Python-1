class Player:
    """ModÃ¨le reprÃ©sentant un joueur d'Ã©checs"""

    def __init__(self, first_name, last_name, birth_date, gender, ranking):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.score = 0

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Classement: {self.ranking})"
