from parser import parse_events
from network_analysis import analyze_network_connections


events = parse_events("data/sample/events.json")


findings = analyze_network_connections(events)


for finding in findings:
    print(finding)
