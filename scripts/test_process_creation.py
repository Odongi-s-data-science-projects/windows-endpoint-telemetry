from parser import parse_events
from process_creation import analyze_process_creation


events = parse_events("data/sample/events.json")


findings = analyze_process_creation(events)


for finding in findings:
    print(finding)
