def analyze_network_connections(events):
    """
    Analyze Sysmon network connection events.
    """

    findings = []

    suspicious_ports = [
        4444,
        8080
    ]

    for event in events:

        if event.get("event_id") != 3:
            continue

        process = event.get("image", "").lower()
        destination_ip = event.get("destination_ip")
        destination_port = event.get("destination_port")

        reasons = []

        if destination_port in suspicious_ports:
            reasons.append(
                f"Connection to suspicious port: {destination_port}"
            )

        if process == "powershell.exe":
            reasons.append(
                "PowerShell initiated a network connection"
            )

        if reasons:
            findings.append(
                {
                    "timestamp": event.get("timestamp"),
                    "process": process,
                    "destination_ip": destination_ip,
                    "destination_port": destination_port,
                    "user": event.get("user"),
                    "reasons": reasons
                }
            )

    return findings
