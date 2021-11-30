#!/usr/bin/env python3
import requests, os
from dotenv import load_dotenv

load_dotenv()

tba_key = os.environ.get("TBA_API_KEY")


def request(endpoint, headers={}, params={}): # TODO: add error handling
    return requests.get(f"https://www.thebluealliance.com/api/v3/{endpoint}", headers=headers | {"X-TBA-Auth-Key":tba_key, "accept":"application/json"}, params=params).json()
