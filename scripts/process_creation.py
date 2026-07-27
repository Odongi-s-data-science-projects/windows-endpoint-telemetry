def analyze_process_creation(events):
    """
    Analyze process creation events for suspicious activity.
    """

    findings = []

    for event in events:

        if event.get("event_id") != 1:
            continue

        process = event.get("image", "").lower()
        command = event.get("command_line", "").lower()

        suspicious = False
        reasons = []

        if "powershell.exe" in process:
            suspicious = True
            reasons.append("PowerShell execution detected")

        suspicious_terms = [
            "-executionpolicy bypass",
            "-encodedcommand",
            "iex"
        ]

        for term in suspicious_terms:
            if term in command:
                suspicious = True
                reasons.append(f"Suspicious command indicator: {term}")

        if suspicious:
            findings.append(
                {
                    "timestamp": event.get("timestamp"),
                    "process": process,
                    "user": event.get("user"),
                    "reasons": reasons
                }
            )

    return findings
