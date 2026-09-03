from datetime import date, timedelta

from events import build_event
from holiday_rules import get_easter_sunday, get_evangelical_holiday, get_winter_solstice, move_to_monday_if_required


def get_events_by_year(year: int) -> list[dict]:
    """Return the historical dates and holidays for a given year."""
    events = [
        build_event(date(year, 1, 1), "Año Nuevo", "Nacional", "Cultural", True, True),
        build_event(date(year, 2, 12), "Fundación de Santiago", "Comunal", "Histórica"),
        build_event(date(year, 2, 14), "Día del Amor y la Amistad", "Internacional", "Cultural"),
        build_event(date(year, 3, 8), "Día Internacional de la Mujer", "Internacional", "Conmemorativa"),
        build_event(get_easter_sunday(year) - timedelta(days=2), "Viernes Santo", "Nacional", "Cultural", True),
        build_event(date(year, 4, 27), "Día de Carabineros de Chile", "Nacional", "Conmemorativa"),
        build_event(date(year, 5, 1), "Día Nacional del Trabajo", "Nacional", "Conmemorativa", True, True),
        build_event(date(year, 5, 21), "Día de las Glorias Navales", "Nacional", "Histórica", True),
        build_event(date(year, 6, 7), "Asalto y Toma del Morro de Arica", "Regional", "Histórica", True),
        build_event(get_winter_solstice(year), "Día Nacional de los Pueblos Indígenas", "Nacional", "Cultural", True),
        build_event(move_to_monday_if_required(date(year, 6, 29)), "San Pedro y San Pablo", "Nacional", "Cultural", True),
        build_event(date(year, 7, 9), "Día Nacional de la Bandera", "Nacional", "Histórica"),
        build_event(date(year, 7, 16), "Día de la Virgen del Carmen", "Nacional", "Cultural", True),
        build_event(date(year, 8, 10), "Día del Minero y la Minera", "Nacional", "Conmemorativa"),
        build_event(date(year, 8, 15), "Asunción de la Virgen", "Nacional", "Cultural", True),
        build_event(date(year, 8, 20), "Natalicio de Bernardo O'Higgins (Chillán y Chillán Viejo)", "Comunal", "Histórica", True),
        build_event(date(year, 9, 18), "Independencia Nacional", "Nacional", "Histórica", True, True),
        build_event(date(year, 9, 19), "Día de las Glorias del Ejército", "Nacional", "Histórica", True, True),
        build_event(date(year, 10, 4), "Día de la Música y de los Músicos Chilenos", "Nacional", "Cultural"),
        get_evangelical_holiday(year),
        build_event(move_to_monday_if_required(date(year, 10, 12)), "Encuentro de Dos Mundos", "Nacional", "Histórica", True),
        build_event(date(year, 11, 1), "Día de Todos los Santos", "Nacional", "Cultural", True),
        build_event(date(year, 12, 8), "Inmaculada Concepción", "Nacional", "Cultural", True),
        build_event(date(year, 12, 25), "Navidad", "Nacional", "Cultural", True, True),
        build_event(date(year, 12, 31), "Víspera de Año Nuevo", "Nacional", "Cultural"),
    ]
    return sorted(events, key=lambda event: event["date"])
