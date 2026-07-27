from parser import parse_events


events = parse_events("data/sample/events.json")


for event in events:
    print(event)
