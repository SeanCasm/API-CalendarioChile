from fastapi import FastAPI

from calendar_service import get_events_by_year

app = FastAPI(title="API de Feriados Chile", version="1.0")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/v1/dates/{year}")
def get_dates_by_year(year: int) -> list[dict]:
    return get_events_by_year(year)
