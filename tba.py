#!/usr/bin/env python3
import requests, dotenv, os

class TbaRequestSender():
    def __init__(self):
        dotenv.load_dotenv()
        self.api_key = os.environ.get("TBA_API_KEY")

    def set_api_key(self, key):
        self.api_key = key

    def request(self,endpoint, headers={}, params={}): # TODO: add error handling
        return requests.get(f"https://www.thebluealliance.com/api/v3/{endpoint}", headers = headers | {"X-TBA-Auth-Key":self.api_key, "accept":"application/json"}, params=params).json()
