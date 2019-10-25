# Sam Mayfield - Oct 2019

import shelve
import atexit
from Team import *
from Character import *

class Controller:

    def __init__(self):
        pass

    def identify_player (self, team_string):
        player_list = "[0]: I'm new here. Let's set my team up! \n"
        key_array = []
        key_array.append("create_new_team")

        i = 1
        for p in users:
            player_list += ("[" + i + "] " + p + "\n")
            i += 1
            key_array[i] = p
        while True:
            player_code = input("\n\n----------------------\n" + team_string + "\n----------------------\n\nWho are you?\n" + player_list)
            try:
                player_int = int(player_code)
            except ValueError:
                print("\n\nDoes that look like a number to you?")
                continue
            if player_int > len(key_array):
                print("\n\nThat's not valid... c'mon, son.")
            else:
                return key_array[player_int]

    def team_setup (self, player):
        if player == "create_new_team":
            return self.new_team_setup()
        else:
            return self.load_team(player)

    def new_team_setup (self):
        new_p_name = ""
        new_team_name = ""
        new_characters = []
        while True:
            resp = input("What's your name (not your team's name)?")
            if resp.strip() == "":
                print ("That's not valid... c'mon, son.")
            else:
                new_p_name = resp
                break
        while True:
            resp = input("What's your team's name?")
            if resp.strip() == "":
                print ("That's not valid... c'mon, son.")
            else:
                new_team_name = resp
                break
        i = 0
        while i < 6:
            new_characters.append(self.set_up_character())
            i += 1

    def set_up_character (self):
        print ("--- CHARACTER " + (i + 1) + " ---" + "\n\n")

        while True:
            potential_name = input("Name: ")
            if potential_name.strip() == "":
                print("\n\nThat's not valid... c'mon, son.")
            else:
                name = potential_name
                break

        while True:
            potential_class = input("Class:\n[1]: C\n[2]: T\n[3]: F\n[4]: D")
            try:
                potential_class_int = int(potential_class)
            except ValueError:
                print("\n\nDoes that look like a number to you?")
                continue
            if potential_class_int > 4 or potential_class_int < 1:
                print("\n\nThat's not valid... c'mon, son.")
            else:
                cclass = potential_class_int

    def load_team (self, key):
        team = Team(key)
        return team

global p1_character_turn
global p2_character_turn
global team1_lineup
global team1_lineup_unchanged
global team2_lineup
global team2_lineup_unchanged

users = shelve.open("users")
controller = Controller()

if __name__ == '__main__':
    print("Welcome to The Tourney App! (v2.0)")

    p1_name = controller.identify_player("TEAM 1")
    team1 = controller.team_setup(p1_name)

    p2_name = controller.identify_player("TEAM 2")
    team2 = controller.team_setup(p2_name)

users.close()

def close_dbs ():
    users.close()

atexit.register(close_dbs())