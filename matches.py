#!/usr/bin/env python3
import tba, team, colorama
from prettytable import PrettyTable


class Match():

    def __init__(self, red_keys, blue_keys, match_number, m_tba):
        self.red_keys = red_keys
        self.blue_keys = blue_keys
        self.number = match_number
        self.m_tba = m_tba
        self.red_alliance = self.get_teams(red_keys)
        self.blue_alliance = self.get_teams(blue_keys)
        self.red_breakdown = {}
        self.blue_breakdown = {}

    def add_team_data(self, data):
        """Processes and distributes data from a match scout"""
        # TODO: add data validation in function call
        if data.get("alliance_color" == "red"):
            red_breakdown[data.get("team_number")] = data

        else:
            blue_breakdown[data.get("team_number")] = data
        if(len(blue_breakdown) == 3 and len(red_breakdown) == 3):
            self.process_match_data()

    def process_match_data(self):
        # should provide per-team a dict with team score, ind. score, driver
        # score, rps, ranking, undefended_cycle_time, defended_cycle_time,
        # defense_score_loss, and penalty_points

        for team in red_alliance + blue_alliance:
            



    def get_teams(self,keys):
        return [team.Team.get_team(key, self.m_tba) for key in keys]

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

def get_match_schedule(event_key, m_tba):
    """Scrapes match schedule from TBA"""
    matches = []
    for match in m_tba.request(f"event/{event_key}/matches/simple"):
        if match == "Error":
            raise AssertionError("Something went wrong")
        if match["comp_level"] == "qm":
            matches.append(Match(match["alliances"]["red"]["team_keys"], match["alliances"]["blue"]["team_keys"], str(match["match_number"]), m_tba))
    return matches


def tabulate_matches(matches, event_name, team_to_flag = None):
    """Returns table representation of match schedule with option to highlight team"""
    schedule_table = PrettyTable()
    schedule_table.field_names = ["Match","Red","Blue"]
    for match in sorted(matches, key = lambda m: int(m.number)):
        red = match.alliance_to_str(match.red_alliance)
        blue = match.alliance_to_str(match.blue_alliance)
        schedule_table.add_row([
        "Q"+match.number,
        red if not match.red_contains_team(team_to_flag) else colorama.Fore.RED + red + colorama.Style.RESET_ALL,
        blue if not match.blue_contains_team(team_to_flag) else colorama.Fore.BLUE + blue + colorama.Style.RESET_ALL
        ])

    return schedule_table.get_string(title=event_name + " Match Schedule")

if __name__ == "__main__":
    print("\n"*5)
    colorama.init()
    matches = get_match_schedule("2019paphi")
    print(tabulate_matches(matches, "Ramp Riot 2021", 321))
    print("\n"*5)
