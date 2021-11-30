#!/usr/bin/env python3
import cmd, sys, tba

class CommandProcessor(cmd.Cmd):
    intro = 'Welcome to LancerScout v0.1. Type "help" or ? to list commands.\n'
    prompt = "> "
    file = None
    self.api_key = os.environ.get("TBA_API_KEY")

    def empty_line(self):
        return None

    def do_setapikey(self, *args):
        'Set your local TBA API Key'
        if len(args) != 1:
            requirement_error("setapikey", "TBA API Key")
        else:
            this.api_key = args[0] # TODO: add api key validation
            print("API Key successfully set")

    def do_geteventkeys(self, *args):
        self.events = []
        'Find a list of event keys for a given team and a given season: geteventkeys \{team number\} \{competition year\}'
        team_num = args[0]
        year = args[1]
        print(f"Looking for events that team {team_num} participated in during the {year} season...")
        events = tba.request(f"team/frc{team_num}/events/{year}/simple")
        if events[0].get('city','error') == 'error':
            print("Something went wrong. Make sure you have the correct API key, and your team number and season year are valid.")
        else:
            for event in events:
                self.events.append((event.get("name","Error")+" "+event.get("year","Error"), event.get("key","Error")))

            print(f"Use the selectevent \{index\} command to select the current event:")
            for index, event in enumerate(events):
                print(f"[{index}] {event[0]}")

    def do_selectevent(self, *args):
        if len(args) == 1:
            try:
                self.event_title,self.event_key = self.events[int(args[0])]
                print("Selected")
            ex

    def requirement_error(self,method_name,*args):
        needed_params = [f"\{{arg}\}" for arg in args]
        print(f"Error: {method_name} requires parameters: " + ", ".join(needed_params))
