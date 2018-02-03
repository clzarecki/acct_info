from datetime import datetime
import json

class Database:

    date_format = "%Y-%m-%d"

    @staticmethod
    def str_to_date(datestr):
        return datetime.strptime(datestr, "%Y-%m-%d")

    def __init__(self):
        self.customers = {}

    def event_more_recent(self, event):
        id = event["account_id"]
        existing_date = Database.str_to_date(self.customers[id]["event_date"])
        new_date = Database.str_to_date(event["event_date"])
        return new_date > existing_date

    def add_event(self, event):
        id = event["account_id"]
        if id in self.customers:
            if self.event_more_recent(event):
                self.customers[id] = event
        else:
            self.customers[id] = event

    def add_event_str(self, events_str):
        events = json.loads(events_str)
        if isinstance(events, list):
            for event in events:
                self.add_event(event)
        elif isinstance(events, dict):
             self.add_event(event)

    def query_account(self, id) :
        if id in self.customers:
            return self.customers[id]["account_information"]
        return None
