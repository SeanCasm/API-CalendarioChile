# API de Feriados Chile

API HTTP que entrega feriados y fechas conmemorativas de Chile para un año determinado.

## Ejecución

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

La API queda disponible en `http://127.0.0.1:8000`.

## Endpoints

### Estado del servicio

`GET /health`

Respuesta:

```json
{
  "status": "ok"
}
```

### Calendario anual

`GET /api/v1/dates/{year}`

Devuelve las fechas del año indicado, ordenadas cronológicamente. Incluye feriados nacionales, regionales, comunales, conmemoraciones y fechas internacionales consideradas por la aplicación.

El parámetro `year` debe ser un entero entre **2026** y **2099**.

Ejemplo:

```bash
curl http://127.0.0.1:8000/api/v1/dates/2026
```

Respuesta parcial:

```json
[
  {
    "date": "2026-01-01",
    "title": "Año Nuevo",
    "scope": "Nacional",
    "category": "Cultural",
    "is_holiday": true,
    "irrenunciable": true
  }
]
```

Cada elemento contiene:

| Campo | Descripción |
| --- | --- |
| `date` | Fecha en formato ISO 8601 (`YYYY-MM-DD`). |
| `title` | Nombre de la fecha o evento. |
| `scope` | Alcance: nacional, regional, comunal o internacional. |
| `category` | Clasificación del evento. |
| `is_holiday` | Indica si es feriado legal. |
| `irrenunciable` | Indica si es un feriado irrenunciable. Siempre implica `is_holiday: true`. |

## Documentación interactiva

FastAPI expone la especificación y una interfaz para probar los endpoints en:

`http://127.0.0.1:8000/docs`
