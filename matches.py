#!/usr/bin/env python3
import tba, teams, colorama
from prettytable import PrettyTable


class Match():
    def __init__(self,red_keys,blue_keys,matchNumber):
        self.red_keys = red_keys
        self.blue_keys = blue_keys
        self.red_alliance = self.get_teams(red_keys)
        self.blue_alliance = self.get_teams(blue_keys)
        self.number = matchNumber

    def get_teams(self,keys):
        return [teams.Team(key) for key in keys]

    def red_contains_team(self,number):
        for team in self.red_alliance:
            if team.number == number:
                return True
        else:
            return False

    def blue_contains_team(self,number):
        for team in self.blue_alliance:
            if team.number == number:
                return True
        else:
            return False

    def alliance_to_str(self, alliance):
        return "  ".join([str(team.number) for team in alliance])

def get_match_schedule(event_key):
    """Scrapes match schedule from TBA"""
    matches = []

    for match in tba.request(f"event/{event_key}/matches/simple"):
        if match == "Error": continue
        if match["comp_level"] == "qm":
            matches.append(Match(match["alliances"]["red"]["team_keys"], match["alliances"]["blue"]["team_keys"], match["match_number"]))

    return matches

def tabulate_matches(matches, team_to_flag = -1):
    """Returns table representation of match schedule with option to highlight team"""
    schedule_table = PrettyTable()
    schedule_table.field_names = ["Match","Red","Blue"]
    for match in matches:
        red = match.alliance_to_str(match.red_alliance)
        blue = match.alliance_to_str(match.blue_alliance)
        schedule_table.add_row([
        match.number,
        red if not match.red_contains_team(team_to_flag) else colorama.Fore.RED + red + colorama.Style.RESET_ALL,
        blue if not match.blue_contains_team(team_to_flag) else colorama.Fore.BLUE + blue + colorama.Style.RESET_ALL
        ])

    schedule_table.sortby = "Match"
    return schedule_table

if __name__ == "__main__":
    print("\n"*5)
    colorama.init()
    matches = get_match_schedule("2021parr")
    print(tabulate_matches(matches, 321).get_string(title="Ramp Riot 2021 Match Schedule"))
    print("\n"*5)
