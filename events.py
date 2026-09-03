from datetime import date


def build_event(event_date: date, title: str, scope: str, category: str, is_holiday: bool = False, irrenunciable: bool = False) -> dict:
    """Create a calendar event with validated holiday attributes."""
    if irrenunciable and not is_holiday:
        raise ValueError("Un evento irrenunciable debe estar marcado como feriado.")
    return {"date": event_date, "title": title, "scope": scope, "category": category, "is_holiday": is_holiday, "irrenunciable": irrenunciable}
