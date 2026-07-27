import json


def load_events(file_path):
    """
    Load event data from a JSON file.
    """

    with open(file_path, "r") as file:
        events = json.load(file)

    return events


def validate_event(event):
    """
    Check that an event contains basic required fields.
    """

    required_fields = [
        "event_id",
        "timestamp",
        "source"
    ]

    for field in required_fields:
        if field not in event:
            return False

    return True


def parse_events(file_path):
    """
    Load and validate events.
    """

    events = load_events(file_path)

    valid_events = []

    for event in events:
        if validate_event(event):
            valid_events.append(event)

    return valid_events
