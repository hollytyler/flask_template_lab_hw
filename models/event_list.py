import datetime
from models.event import Event

event1 = Event("Mob Progamming", datetime.date(2023, 6, 19), 14, "The Classroom", "We are trying to mob this lab.. somehow.")
event2 = Event("Glastonbury", datetime.date(2023, 6, 10), 10000, "The South", "Music, madness and mugs... of beer")
event3 = Event("E3", datetime.date(2023, 9, 30), 8000, "LA", "Gaming Expo. Sounds fun!!")

events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)
