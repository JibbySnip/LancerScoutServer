#!/usr/bin/env python3
import tba

class Team():
    teams = set()

    def __init__(self,team_key, m_tba):
        self.m_tba = m_tba
        self.name, self.number = self.query_team(team_key)
        Team.teams.add(self)

    def query_team(self,team_key):
        resp = self.m_tba.request(f"team/{team_key}")
        return resp.get("nickname", "n/a"), team_key[3:]

    def __str__(self):
        return self.number

    @staticmethod
    def get_team(key, m_tba):
        for team in Team.teams:
            if team.number == key[3:]:
                return team
        else:
            return Team(key, m_tba)
