# Sam Mayfield - Oct 2019

import shelve
from Team import *
from Character import *
users = shelve.open("users")

class AppUI:

    global team1
    global team2
    global p1_character_turn
    global p2_character_turn
    global team1_lineup
    global team1_lineup_unchanged
    global team2_lineup
    global team2_lineup_unchanged
    global p1_name
    global p2_name
    users = shelve.open("users")

    if __name__ == '__main__':
        main()

    def main(self):
        print("Welcome to The Tourney App! (v2.0)")

        player1 = input("\n\n----------------------\nTEAM 1\n----------------------\n\nWho are you?\n")
        self.set_team(player1, team1)

        player2 = input("\n\nAnd who are you?\n")
        self.set_team(player2, team2)

        users.close()

    def team_setup (self, player, team):
        if users.__contains__(player):
            self.load_team(player, team1)
        else:
            new_player = input("Looks like you're new here. Wanna set up a new team?\n\n[Y]es I do!\n[N]ope, take me back.")
            if new_player.upper().startswith("Y"):
                self.new_team_setup()

    def new_team_setup (self):
        new_name = input("What's your name (not your team's name)?")

    def load_team(self, key, team):
        team = Team(key)