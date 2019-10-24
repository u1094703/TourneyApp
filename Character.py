# Sam Mayfield - Oct 2019

class Character:
    def __init__(self, name, cclass, health, attack, defense, critical, is_alive, games_played):
        self.name = name
        self.cclass = cclass
        self.health = health
        self.attack = attack
        self.defense = defense
        self.critical = critical
        self.is_alive = is_alive
        self.games_played = games_played

    def to_string (self):
        if games_played >= 3:
            status = "UNAVAILABLE (Exhausted)"
        elif not is_alive:
            status = "UNAVAILABLE (Dead)\nGames Remaining: " + 3 - games_played
        else:
            status = "AVAILABLE\nGames Remaining: " + 3 - games_played

        return name + "\nClass: " + cclass + "\nHealth: " + health + "\nAttack: " + attack + "\nDefense: " + defense +\
                "\nCritical: " + critical + "\nStatus: " + status

    def simple_string (self):
        return name + "\nClass: " + cclass + "\nHealth: " + health + "\nAttack: " + attack + "\nDefense: " + defense +\
                "\nCritical: " + critical

