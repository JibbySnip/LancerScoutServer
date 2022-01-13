#!/usr/bin/env python3
import tba

class Team():

    teams = set()

    def __init__(self,team_key, m_tba):
        self.m_tba = m_tba
        self.name, self.number = self.query_team(team_key)
        Team.teams.add(self)
        self.matches = []

    def init_fields(self):
        self.team_scores = []
        self.alliance_scores = []
        self.driver_scores = []
        self.rps = 0
        self.qual_rank = -1
        self.undefended_cycle_time = []
        self.defended_cycle_time = []
        self.defended_score_loss = []
        self.defense_score_loss = []

        # Seasonal fields
        # Cargo fields are lists of Pos_2ds
        self.taxi_success = []
        self.auto_cargo_scored = {
        "high": [],
        "low": []
        }
        self.auto_cargo_missed = {
        "high": [],
        "low": []
        }
        self.auto_hp_shot_landed = []
        self.tele_cargo_scored = {
        "high": [],
        "low": []
        }
        self.tele_cargo_missed = {
        "high": [],
        "low": []
        }
        self.opp_team_cargo_scored = {
        "high":[],
        "low":[]
        }
        self.penalties = {
        "launchpad_contact": [],
        "control_limit": [],
        "pinning": [],
        "catching": [],
        "other": []
        }
        self.hang_time = []
        self.hang_bar = []
        self.hang_fail = []


    def add_match(self, match):
        self.matches.append(match)

    def add_match_data(self, data):
        self.team_scores.append(data.get("team_score", None))
        self.alliance_scores.append(data.get("team_score", None))
        self.driver_scores.append(data.get("driver_score"), None)
        self.rps += data.get("rps", 0)
        self.ranking = data.get("ranking", -1)
        # TODO: Add on-season objective breakdowns
        self.undefended_cycle_time.append(data.get("undefended_cycle_time", None)) # this can be expanded per-objective
        self.defended_cycle_time.append(data.get("defended_cycle_time", None)) #this can be expanded per-objective
        # TODO: Consider adding something that measures how much a team
        # tends to make other teams take over their average defended cycle time
        self.defended_score_loss.append(data.get("defended_score_loss", None))
        self.defense_score_loss.append(data.get("defense_score_loss", None)) # When defending
        self.penalty_points.append(data.get("penalty_points", 0))


        """Adds the team-specific data from a match."""
        # self.match_data.append({
        # "match_number":
        # "offensive_data": {
        #     "team_score": ,
        #     "alliance_score": ,
        #     "driver_score": data.get("calculated_driver_score", None),
        #     "rps": data.get("rps", None)
        #     # Any other season-specific offensive attributes can be added here,
        #     # including cycle time, number of elements scored
        # },
        # "defensive_data": {
        #     # calculated average decrease in cycle time, maybe effectiveness ranking
        # }
        # })

    # def add_pit_data(self, data):
    #     self.team_picture =

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
