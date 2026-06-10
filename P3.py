class Player:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.runs = [] 
    def add_score(self, runs):
        self.runs.append(runs)
    def total_runs(self):
        return sum(self.runs)
    def matches_played(self):
        return len(self.runs)
    def average(self):
        if self.matches_played() == 0:
            return 0
        return self.total_runs() / self.matches_played()
class Match:
    def __init__(self, match_id):
        self.match_id = match_id
class Tournament:
    def __init__(self, name):
        self.name = name
        self.players = []  
    def add_player(self, pid, name):
        p = Player(pid, name)
        self.players.append(p)
    def add_score(self, pid, runs):
        for p in self.players:
            if p.pid == pid:
                p.add_score(runs)
    def show_stats(self):
        print("Tournament:", self.name)
        for p in self.players:
            print("Player:", p.name)
            print("Total Runs:", p.total_runs())
            print("Matches:", p.matches_played())
            print("Average:", round(p.average(), 2))
            print()
t = Tournament("Summer Cup")
t.add_player("P1", "Virat")
t.add_player("P2", "Rohit")
t.add_score("P1", 50)
t.add_score("P1", 70)
t.add_score("P2", 30)
t.add_score("P2", 80)
t.show_stats()