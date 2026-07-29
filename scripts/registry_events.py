def analyze_registry_events(events):
    """
    Analyze Sysmon registry modification events.
    """

    findings = []

    persistence_locations = [
        "\\currentversion\\run\\",
        "\\currentversion\\runonce\\"
    ]

    for event in events:

        if event.get("event_id") != 13:
            continue

        target = event.get("target_object", "").lower()

        reasons = []

        for location in persistence_locations:

            if location in target:
                reasons.append(
                    "Registry persistence location modified"
                )

        if reasons:
            findings.append(
                {
                    "timestamp": event.get("timestamp"),
                    "process": event.get("image"),
                    "target": event.get("target_object"),
                    "details": event.get("details"),
                    "user": event.get("user"),
                    "reasons": reasons
                }
            )

    return findings
