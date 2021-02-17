class Team:
    def __init__(self, name):
        self.name = name
        self._team_players = []

    def add_player(self, player):
        if isinstance(player, Player):
            player.team = self.name
            self._team_players.append(player)

    def get_team(self):
        for player in self._team_players:
            print(f'{player.team}: Name: {player.name}, age: {player.age}, '
                  f'height: {player.height}, weight: {player.weight}')


class Player:
    instance_count = 0

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        Player.instance_count += 1

    def get_age(self):
        return f'{self.name} age is {self.age}'

    def get_height(self):
        return f'{self.name} height is {self.height}'

    def get_weight(self):
        return f'{self.name} weight is {self.weight}'

    def get_team(self):
        return self.__dict__.get('team', 'Not a member of the team')


team1 = Team('Team 1')
team2 = Team('Team 2')
player_1 = Player('Ivan', 76, 186, 132)
player_2 = Player('Vasya', 55, 173, 76)
player_3 = Player('Oleg', 42, 156, 77)
player_4 = Player('Kirill', 35, 149, 66)
player_5 = Player('Orest', 21, 174, 65)
team1.add_player(player_1)
team1.add_player(player_2)
team2.add_player(player_3)
team2.add_player(player_4)

team1.get_team()
print()
team2.get_team()

print(player_1.get_team())
print(player_2.get_team())
print(player_3.get_team())
print(player_4.get_team())
print(player_5.get_team())

