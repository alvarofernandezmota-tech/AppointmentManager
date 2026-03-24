# 🏗️ ARCHITECTURE — AppointmentManager

> Diseño técnico completo del sistema. Última actualización: 24 marzo 2026.

---

## 🎯 Filosofía de diseño

AppointmentManager sigue el principio **"Define el contrato primero, implementa después"**. La interfaz abstracta `AbstractLifeManager` es el núcleo del sistema — todas las implementaciones deben respetarla, lo que permite intercambiar backends sin tocar el código cliente.

Esto permite:
- Usar `MemoryLifeManager` en tests (rápido, sin dependencias)
- Usar `SQLiteLifeManager` en producción local (persistente)
- Usar `APILifeManager` en producción remota (escalable)
- El código cliente **nunca cambia** — solo cambia el manager que se inyecta

---

## 🧱 Capas del sistema (Layer 7)

```
┌─────────────────────────────────────────────────────┐
│                   CAPA CLIENTE                      │
│         app.py / CLI / Bot Telegram / API           │
└─────────────────────┬───────────────────────────────┘
                      │ usa
┌─────────────────────▼───────────────────────────────┐
│              AbstractLifeManager (ABC)               │
│           src/interfaces/abstract_lifemanager.py     │
│                                                     │
│  + create_appointment(date, time, type, notes) → UUID│
│  + get_appointments(date) → List[Dict]              │
│  + log_habit(date, habit, value) → bool             │
│  + get_habits(date) → Dict[str, str]                │
│  + get_day_summary(date) → Dict                     │
└──────┬──────────────┬──────────────┬────────────────┘
       │              │              │
┌──────▼──────┐ ┌─────▼──────┐ ┌────▼───────────┐
│   Memory    │ │   SQLite   │ │   API REST     │
│LifeManager  │ │LifeManager │ │  LifeManager   │
│  (impl/)    │ │  (impl/)   │ │   (impl/)      │
│             │ │            │ │                │
│ In-memory   │ │ SQLAlchemy │ │ httpx/requests │
│ dict-based  │ │  + SQLite  │ │  FastAPI client│
│ ✅ Done     │ │ 🔴 WIP     │ │ 🟡 Planned     │
└─────────────┘ └────────────┘ └────────────────┘
```

---

## 📐 Interfaz abstracta — `AbstractLifeManager`

```python
class AbstractLifeManager(ABC):
    """Super interfaz Layer 7 — Appointments + Habits"""

    # --- CITAS ---
    @abstractmethod
    def create_appointment(self, date: date, time: str,
                           type: str, notes: str = "") -> UUID:
        """Crear cita. Devuelve UUID único."""

    @abstractmethod
    def get_appointments(self, date: date) -> List[Dict]:
        """Obtener todas las citas de un día."""

    # --- HÁBITOS ---
    @abstractmethod
    def log_habit(self, date: date, habit: str, value: str) -> bool:
        """Registrar valor de un hábito para un día."""

    @abstractmethod
    def get_habits(self, date: date) -> Dict[str, str]:
        """Obtener todos los hábitos de un día."""

    # --- RESUMEN ---
    @abstractmethod
    def get_day_summary(self, date: date) -> Dict:
        """Resumen completo: citas + hábitos de un día."""
```

---

## 🔮 Interfaz ampliada — Fase 2 (planificada)

En Fase 2 se ampliarán los métodos para cubrir el tracking completo:

```python
# Sueño
def log_sleep(self, date: date, bedtime: str,
              wake_time: str, quality: str) -> bool: ...
def get_sleep(self, date: date) -> Dict: ...

# Métricas extendidas
def log_metric(self, date: date, key: str, value: str) -> bool: ...
def get_metrics(self, date: date) -> Dict[str, str]: ...

# Resumen semanal
def get_week_summary(self, start_date: date) -> Dict: ...

# Búsqueda
def search_appointments(self, query: str) -> List[Dict]: ...
```

---

## 🗄️ Modelo de datos — SQLiteLifeManager (Fase 2)

### Tabla `appointments`
```sql
CREATE TABLE appointments (
    id          TEXT PRIMARY KEY,  -- UUID
    date        TEXT NOT NULL,     -- YYYY-MM-DD
    time        TEXT NOT NULL,     -- HH:MM
    type        TEXT NOT NULL,
    notes       TEXT DEFAULT '',
    created_at  TEXT NOT NULL
);
```

### Tabla `habits`
```sql
CREATE TABLE habits (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT NOT NULL,     -- YYYY-MM-DD
    habit       TEXT NOT NULL,     -- 'sueno', 'THC', 'ejercicio'...
    value       TEXT NOT NULL,
    logged_at   TEXT NOT NULL,
    UNIQUE(date, habit)
);
```

### Tabla `sleep` (Fase 2+)
```sql
CREATE TABLE sleep (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT NOT NULL UNIQUE,
    bedtime     TEXT,
    wake_time   TEXT,
    hours       REAL,
    quality     TEXT,
    notes       TEXT DEFAULT ''
);
```

---

## 🔄 Flujo de datos

```
1. Cliente instancia un LifeManager concreto
   mgr = SQLiteLifeManager(db_path="data/life.db")

2. Cliente usa la interfaz abstracta
   mgr.create_appointment(today, "10:00", "Médico")
   mgr.log_habit(today, "sueno", "7h")

3. La implementación concreta maneja la persistencia
   SQLiteLifeManager → INSERT INTO appointments...
   MemoryLifeManager → self.appointments[date].append(...)

4. El cliente obtiene datos
   summary = mgr.get_day_summary(today)
   → {'date': '...', 'appointments': [...], 'habits': {...}}
```

---

## 🧪 Estrategia de tests

```
tests/
├── test_memory_lifemanager.py    # Tests unitarios MemoryLifeManager
├── test_sqlite_lifemanager.py    # Tests unitarios SQLiteLifeManager
├── test_interface_contract.py   # Tests de contrato (mismos tests, distinto impl)
└── conftest.py                  # Fixtures compartidas
```

Todos los managers pasan el mismo **test de contrato** — garantía de que cualquier implementación es intercambiable.

---

## 📦 Dependencias

| Paquete | Versión | Uso |
|---------|---------|-----|
| `python` | ≥3.10 | Runtime |
| `pytest` | ≥7.0 | Testing |
| `sqlalchemy` | ≥2.0 | ORM SQLite (Fase 2) |
| `fastapi` | ≥0.100 | API REST (Fase 3) |
| `uvicorn` | ≥0.20 | Servidor ASGI (Fase 3) |
| `pydantic` | ≥2.0 | Validación datos (Fase 3) |
| `python-telegram-bot` | ≥20.0 | Bot Telegram (Fase 5) |

---

## 🔐 Decisiones de diseño

| Decisión | Alternativa descartada | Razón |
|----------|----------------------|-------|
| ABC para interfaz | Protocol (structural) | ABC es más explícita y fuerza implementación |
| UUID para IDs de citas | Integer autoincrement | Portabilidad entre backends |
| Dict como valor de retorno | Dataclass/Pydantic | Simplicidad inicial; migrar a Pydantic en Fase 3 |
| SQLite como primera DB | PostgreSQL | Sin dependencias externas, portátil |
| Fecha como `date` object | String | Type safety desde el origen |

---

_Creado: 24 marzo 2026 | Actualizar con cada cambio arquitectónico significativo_
