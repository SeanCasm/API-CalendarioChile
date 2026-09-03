from datetime import date, timedelta

from events import build_event

FIRST_SUPPORTED_YEAR = 2026
LAST_SUPPORTED_YEAR = 2099
JUNE_21_SOLSTICES = frozenset({2026, 2027, 2030, 2031, 2034, 2035, 2038, 2039, 2042, 2043, 2046, 2047, 2051, 2055, 2059, 2063, 2067, 2071, 2075})


def get_winter_solstice(year: int) -> date:
    if not FIRST_SUPPORTED_YEAR <= year <= LAST_SUPPORTED_YEAR:
        raise ValueError(f"El año debe estar entre {FIRST_SUPPORTED_YEAR} y {LAST_SUPPORTED_YEAR}.")
    return date(year, 6, 21 if year in JUNE_21_SOLSTICES else 20)


def get_evangelical_holiday(year: int) -> dict:
    event_date = date(year, 10, 31)
    if event_date.weekday() == 1:
        event_date -= timedelta(days=4)
    elif event_date.weekday() == 2:
        event_date += timedelta(days=2)
    return build_event(event_date, "Día Nacional de las Iglesias Evangélicas y Protestantes", "Nacional", "Religioso")


def get_easter_sunday(year: int) -> date:
    """Return Easter Sunday for the Gregorian calendar."""
    a = year % 19; b = year // 100; c = year % 100; d = b // 4; e = b % 4
    f = (b + 8) // 25; g = (b - f + 1) // 3; h = (19 * a + b - d - g + 15) % 30
    i = c // 4; k = c % 4; l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451; month = (h + l - 7 * m + 114) // 31
    return date(year, month, ((h + l - 7 * m + 114) % 31) + 1)


def move_to_monday_if_required(event_date: date) -> date:
    weekday = event_date.weekday()
    if weekday in (1, 2, 3):
        return event_date - timedelta(days=weekday)
    if weekday == 4:
        return event_date + timedelta(days=3)
    return event_date
