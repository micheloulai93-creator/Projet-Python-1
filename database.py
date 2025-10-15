from tinydb import TinyDB


class Database:
    """Gère la sauvegarde et le chargement des données avec TinyDB"""

    def __init__(self, db_name='db.json'):
        self.db = TinyDB(db_name)
        self.players_table = self.db.table('players')
        self.tournaments_table = self.db.table('tournaments')

    def save_players(self, players):
        """Sauvegarde tous les joueurs"""
        self.players_table.truncate()
        serialized_players = [
            self.serialize_player(player) for player in players
        ]
        if serialized_players:
            self.players_table.insert_multiple(serialized_players)

    def load_players(self):
        """Charge tous les joueurs"""
        from models.player import Player  # noqa: F401
        serialized_players = self.players_table.all()
        return [self.deserialize_player(data) for data in serialized_players]

    def serialize_player(self, player):
        """Convertit un joueur en dictionnaire"""
        return {
            'first_name': player.first_name,
            'last_name': player.last_name,
            'birth_date': player.birth_date,
            'gender': player.gender,
            'ranking': player.ranking,
            'score': player.score
        }

    def deserialize_player(self, data):
        """Convertit un dictionnaire en joueur"""
        from models.player import Player  # noqa: F401
        player = Player(
            first_name=data['first_name'],
            last_name=data['last_name'],
            birth_date=data['birth_date'],
            gender=data['gender'],
            ranking=data['ranking']
        )
        player.score = data.get('score', 0)
        return player

    def save_tournaments(self, tournaments, players):
        """Sauvegarde tous les tournois"""
        self.tournaments_table.truncate()
        serialized_tournaments = [
            self.serialize_tournament(tournament, players)
            for tournament in tournaments
        ]
        if serialized_tournaments:
            self.tournaments_table.insert_multiple(serialized_tournaments)

    def load_tournaments(self, players):
        """Charge tous les tournois"""
        from models.tournament import Tournament  # noqa: F401
        serialized_tournaments = self.tournaments_table.all()
        return [
            self.deserialize_tournament(data, players)
            for data in serialized_tournaments
        ]

    def serialize_tournament(self, tournament, players):
        """Convertit un tournoi en dictionnaire"""
        return {
            'name': tournament.name,
            'location': tournament.location,
            'start_date': tournament.start_date,
            'end_date': tournament.end_date,
            'number_of_rounds': tournament.number_of_rounds,
            'time_control': tournament.time_control,
            'description': tournament.description,
            'players_indices': tournament.players_indices,
            'current_round': tournament.current_round,
            'rounds': [
                self.serialize_round(round_obj, players)
                for round_obj in tournament.rounds
            ]
        }

    def deserialize_tournament(self, data, players):
        """Convertit un dictionnaire en tournoi"""
        from models.tournament import Tournament  # noqa: F401
        tournament = Tournament(
            name=data['name'],
            location=data['location'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            number_of_rounds=data['number_of_rounds'],
            time_control=data['time_control'],
            description=data['description']
        )
        tournament.players_indices = data['players_indices']
        tournament.current_round = data['current_round']
        tournament.rounds = [
            self.deserialize_round(round_data, players)
            for round_data in data['rounds']
        ]
        return tournament

    def serialize_round(self, round_obj, players):
        """Convertit un tour en dictionnaire"""
        start_time = None
        if round_obj.start_time:
            start_time = round_obj.start_time.isoformat()

        end_time = None
        if round_obj.end_time:
            end_time = round_obj.end_time.isoformat()

        return {
            'name': round_obj.name,
            'start_time': start_time,
            'end_time': end_time,
            'matches': [
                self.serialize_match(match, players)
                for match in round_obj.matches
            ]
        }

    def deserialize_round(self, data, players):
        """Convertit un dictionnaire en tour"""
        from models.round import Round  # noqa: F401
        from datetime import datetime

        round_obj = Round(data['name'])

        if data['start_time']:
            round_obj.start_time = datetime.fromisoformat(data['start_time'])

        if data['end_time']:
            round_obj.end_time = datetime.fromisoformat(data['end_time'])

        round_obj.matches = [
            self.deserialize_match(match_data, players)
            for match_data in data['matches']
        ]
        return round_obj

    def serialize_match(self, match, players):
        """Convertit un match en dictionnaire"""
        return {
            'player1_index': players.index(match.player1),
            'player2_index': players.index(match.player2),
            'score1': match.score1,
            'score2': match.score2
        }

    def deserialize_match(self, data, players):
        """Convertit un dictionnaire en match"""
        from models.match import Match  # noqa: F401

        match = Match(
            players[data['player1_index']],
            players[data['player2_index']]
        )
        match.score1 = data['score1']
        match.score2 = data['score2']
        return match
