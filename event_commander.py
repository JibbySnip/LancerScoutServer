#!/usr/bin/env python3
import cmd, sys, tba, matches, os

class EventCommander(cmd.Cmd):
    intro = 'Welcome to LancerScout v0.1. Type "help" or ? to list commands.\n'
    prompt = "> "
    file = None
    def __init__(self):
        super().__init__()
        self.event = ()
        self.m_tba = tba.TbaRequestSender()
        self.m_team = "321"
        self.events = []

    def empty_line(self):
        return None

    def do_setapikey(self, arg):
        'Set your local TBA API Key'
        if len(arg.split(" ")) != 1:
            self.requirement_error("setapikey", "TBA API Key")
        else:
            self.m_tba.set_api_key(arg) # TODO: add api key validation
            print("API Key successfully set")

    def do_getevents(self, arg):
        'Find a list of event keys for a given team and a given season -- getevents {team number} {competition year}'
        print()
        self.events = []
        if len(arg.split(" ")) == 2:
            team_num, year = arg.split(" ")
            self.m_team = team_num
            print(f"Looking for events that team {team_num} participated in during the {year} season...")
            events = self.m_tba.request(f"team/frc{team_num}/events/{year}/simple")
            if len(events) != 0:
                if events[0].get('city','error') == 'error':
                    print("Something went wrong. Make sure you have the correct API key, and your team number and season year are valid.")
                else:
                    for event in events:
                        self.events.append({
                        "name":event.get("name","N/A"),
                        "year": str(event.get("year","N/A")),
                        "key": event.get("key","N/A")})
                    print("Use the setevent {index} command to select the current event:\n")
                    for index, event in enumerate(events):
                        print(f"[{index}] {event['name']}")
                    print()
            else:
                print(f"Team {team_num} didn't compete at any events in {year}.\n")
        else:
            self.requirement_error("getevents", "team number", "year")

    def do_setevent(self, arg):
        "Select event from the list provided by geteventkeys using the given index numbers --  setevent {index}"
        if len(arg.split(" ")) == 1: # TODO: arg filtering
            if self.events != []:
                try:
                    event_entry = self.events[int(arg)]
                    self.event_name = event_entry["name"]
                    self.event_key = event_entry["key"]
                    self.event_year = event_entry["year"]
                    print(f"Selected {self.event_name} {self.event_year}. Loading match schedule...")
                    try:
                        self.match_schedule = self.get_match_schedule(self.event_key)
                        print("Successfully loaded all data!\n")
                        print(matches.tabulate_matches(self.match_schedule, self.event_name, self.m_team))
                    except AssertionError:
                        print("Something went wrong. Make sure that you have the correct API key.")
                    # except KeyError:
                        print("There was an error retrieving the data. Is TBA down?")
                except AssertionError:
                    self.requirement_error("setevent", "event index")
            else:
                print("Error: no event data is available. Please run getevents first.")

    def do_currevent(self, arg):
        "Displays the current event, if one is available -- currevent"
        if self.event_set():
            print(self.event['name'])
        else:
            print("No event has been set.")

    def do_haskey(self, arg):
        "Check if api key is registered -- haskey"
        print("Key is registered!" if self.m_tba.api_key is not None else "No key found...")

    def do_exit(self, arg):
        "Close the program -- exit"
        print("Exiting...")
        exit()

    def get_match_schedule(self,event_key):
        return matches.get_match_schedule(event_key, self.m_tba)

    def event_set(self):
        return self.event is not None






    def requirement_error(self,method_name,*args):
        needed_params = ["{"+arg+"}" for arg in args]
        print(f"Error: {method_name} requires parameters: " + " ".join(needed_params))
