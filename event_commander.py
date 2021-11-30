#!/usr/bin/env python3
import cmd, sys, tba, matches

class EventCommander(cmd.Cmd):
    intro = 'Welcome to LancerScout v0.1. Type "help" or ? to list commands.\n'
    prompt = "> "
    file = None
    self.api_key = os.environ.get("TBA_API_KEY")
    self.event = ()

    def empty_line(self):
        return None

    def do_setapikey(self, *args):
        'Set your local TBA API Key'
        if len(args) != 1:
            requirement_error("setapikey", "TBA API Key")
        else:
            this.api_key = args[0] # TODO: add api key validation
            print("API Key successfully set")

    def do_getevents(self, *args):
        'Find a list of event keys for a given team and a given season: getevents \{team number\} \{competition year\}'
        self.events = []
        if len(args) == 2:
            team_num = args[0]
            year = args[1]
            print(f"Looking for events that team {team_num} participated in during the {year} season...")
            events = tba.request(f"team/frc{team_num}/events/{year}/simple")
            if events[0].get('city','error') == 'error':
                print("Something went wrong. Make sure you have the correct API key, and your team number and season year are valid.")
            else:
                for event in events:
                    self.events.append((event.get("name","N/A")+" "+event.get("year","N/A"), event.get("key","N/A")))
                print(f"Use the selectevent \{index\} command to select the current event:\n")
                for index, event in enumerate(events):
                    print(f"[{index}] {event[0]}")
        else: 
            requirement_error("getevents", "team number", "year")

    def do_selectevent(self, *args):
        "Select event from the list provided by geteventkeys using the given index numbers: selectevent \{index\}"
        if len(args) == 1:
            if self.events is not None:
                try:
                    self.event_title,self.event_key = self.events[int(args[0])]
                    print("Selected {self.event_title}. Loading match schedule...")
                    try:
                        self.match_schedule = self.get_match_schedule(self.event_key)
                        print("Loading team data...")
                        matches.load_teams()
                        print("Successfully loaded all data!\n")
                        print(matches.tabulate_matches(self.match_schedule))
                    except AssertionError:
                        print("Something went wrong. Make sure that you have the correct API key.")
                except TypeError:
                    requirement_error("selectevent", "event index")
            else:
                print("Error: no event data is available. Please run getevents first.")

    def do_currevent(self, *args):
        "Displays the current event, if one is available: currevent"
        if self.event is not None:
            print(self.event[0])

    def get_match_schedule(self,event_key):
        return matches.get_match_schedule(event_key)

            




    def requirement_error(self,method_name,*args):
        needed_params = [f"\{{arg}\}" for arg in args]
        print(f"Error: {method_name} requires parameters: " + ", ".join(needed_params))
