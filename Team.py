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

    def __init__ (self, player):
        self.player = player
        self.load()

    def save (self):
        self.savefile = shelve.open(self.player + "SaveFile")
        self.savefile[name] = self.name
        self.savefile[wins] = self.wins
        self.savefile[losses] = self.losses
        self.savefile[c1] = self.characters[0]
        self.savefile[c2] = self.characters[1]
        self.savefile[c3] = self.characters[2]
        self.savefile[c4] = self.characters[3]
        self.savefile[c5] = self.characters[4]
        self.savefile[c6] = self.characters[5]
        self.savefile.close()

    def load (self):
        self.savefile = shelve.open(self.player + "SaveFile")
        self.name = self.savefile[name]
        self.wins = self.savefile[wins]
        self.losses = self.savefile[losses]
        self.characters[0] = self.savefile[c1]
        self.characters[1] = self.savefile[c2]
        self.characters[2] = self.savefile[c3]
        self.characters[3] = self.savefile[c4]
        self.characters[4] = self.savefile[c5]
        self.characters[5] = self.savefile[c6]
        self.savefile.close()

    def to_string (self):
        all_characters = ""
        i = 1
        for fella in self.characters:
            all_characters += "(" + i + ")\n" + fella.to_string + "\n\n"
        return name + "\n\nWins: " + wins + "\nLosses: " + losses + "\n\n" + all_characters