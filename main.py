#!/usr/bin/env python3
import requests, cmd, sys
import tba
from event_commander import EventCommander

# def find_event_key(team):


if __name__ == "__main__":
    m_event = EventCommander()
    m_event.cmdloop()