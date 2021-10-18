class SoccerPlayer:
    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists

    def score(self, count_score=1):
        self.goals += count_score

    def make_assist(self, count_assists=1):
        self.assists += count_assists

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')
