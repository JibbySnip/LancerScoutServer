#!/usr/bin/env python3
import tba

class Team():
    def __init__(self,team_key):
        self.name, self.number = self.query_team(team_key)

    def query_team(self,team_key):
        team_json = tba.request(f"team/{team_key}")
        return team_json["nickname"], team_json["team_number"]

    def __str__(self):
        return self.number
