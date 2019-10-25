# Sam Mayfield - Oct 2019

class Character:
    def __init__ (self, name, cclass, health, attack, defense, critical, is_alive, games_played):
        self.name = name
        self.cclass = cclass
        self.health = health
        self.attack = attack
        self.defense = defense
        self.critical = critical
        self.is_alive = is_alive
        self.games_played = games_played

    def to_string (self):
        if self.games_played >= 3:
            status = "UNAVAILABLE (Exhausted)"
        elif not self.is_alive:
            status = "UNAVAILABLE (Dead)\nGames Remaining: " + (3 - self.games_played)
        else:
            status = "AVAILABLE\nGames Remaining: " + (3 - self.games_played)

        return self.name + "\nClass: " + self.cclass + "\nHealth: " + self.health + "\nAttack: " + self.attack + "\nDefense: " + self.defense +\
                "\nCritical: " + self.critical + "\nStatus: " + status

    def simple_string (self):
        return self.name + "\nClass: " + self.cclass + "\nHealth: " + self.health + "\nAttack: " + self.attack + "\nDefense: " + self.defense +\
                "\nCritical: " + self.critical