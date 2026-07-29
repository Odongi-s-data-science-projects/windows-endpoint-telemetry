from parser import parse_events
from registry_events import analyze_registry_events


events = parse_events("data/sample/events.json")


findings = analyze_registry_events(events)


for finding in findings:
    print(finding)
