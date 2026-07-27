# Investigation Methodology

## Purpose

This project follows a structured digital forensic workflow for analyzing Windows Endpoint telemetry. The objective is to identify potentially malicious activity using Windows Event Logs and Sysmon telemetry while maintaining a repeatable investigation process.

---

## Investigation Workflow

1. Define the investigation scope.
2. Collect Windows Event Logs and Sysmon telemetry.
3. Validate log integrity and availability.
4. Parse raw event data into structured records.
5. Normalize timestamps and event fields.
6. Filter events relevant to the investigation.
7. Correlate related events across multiple log sources.
8. Build a chronological timeline of activity.
9. Identify suspicious behaviors and indicators of compromise (IOCs).
10. Document findings and produce an investigation report.

---

## Investigation Principles

- Preserve data integrity.
- Maintain chronological accuracy.
- Correlate evidence before drawing conclusions.
- Base conclusions on observable evidence.
- Document every significant finding.

---

## Expected Outputs

- Parsed event datasets
- Authentication analysis
- Process creation analysis
- PowerShell activity analysis
- Registry modification analysis
- Network connection analysis
- Investigation timeline
- Final forensic report