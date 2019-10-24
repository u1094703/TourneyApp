# Sam Mayfield - Oct 2019
import shelve
from Character import *

class Team:
    def __init__ (self, characters, name, wins, losses, player):
        self.characters = characters
        self.name = name
        self.wins = wins
        self.losses = losses
        self.player = player

    def save (self):
        savefile = shelve.open(player + "SaveFile")
        savefile[name] = name
        savefile[wins] = wins
        savefile[losses] = losses
        savefile[c1] = characters[0]
        savefile[c2] = characters[1]
        savefile[c3] = characters[2]
        savefile[c4] = characters[3]
        savefile[c5] = characters[4]
        savefile[c6] = characters[5]
        savefile.close()

    def load (self):
        savefile = shelve.open(player + "SaveFile")
        name = savefile[name]
        wins = savefile[wins]
        losses = savefile[losses]
        characters[0] = savefile[c1]
        characters[1] = savefile[c2]
        characters[2] = savefile[c3]
        characters[3] = savefile[c4]
        characters[4] = savefile[c5]
        characters[5] = savefile[c6]
        savefile.close()

    def to_string (self):
        all_characters = ""
        i = 1
        for fella in characters:
            all_characters += "(" + i + ")\n" + fella.to_string + "\n\n"
        return name + "\n\nWins: " + wins + "\nLosses: " + losses + "\n\n" + all_characters