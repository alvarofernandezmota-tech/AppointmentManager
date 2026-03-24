# 🗺️ ROADMAP — AppointmentManager

> Plan de desarrollo completo. Última actualización: 24 marzo 2026.

---

## 📊 Estado general

| Fase | Nombre | Tareas | Completadas | Estado |
|------|--------|--------|-------------|--------|
| 1 | Arquitectura base | 4 | 4 | ✅ Completa |
| 2 | Persistencia SQLite | 6 | 0 | 🔴 Siguiente |
| 3 | API REST FastAPI | 6 | 0 | 🟡 Planificada |
| 4 | CLI interactivo | 4 | 0 | 🟡 Planificada |
| 5 | Bot Telegram | 5 | 0 | 🟡 Planificada |
| 6 | Dashboard web | 5 | 0 | ⚪ Futuro |
| **TOTAL** | | **30** | **4** | **13%** |

---

## ✅ FASE 1 — Arquitectura base (COMPLETADA)

> Toledo, 19 marzo 2026

- [x] Crear repositorio con estructura de carpetas
- [x] Definir `AbstractLifeManager` (ABC Layer 7)
- [x] Implementar `MemoryLifeManager` (in-memory)
- [x] `app.py` de demostración básica

**Entregable:** Arquitectura base funcional con interfaz abstracta y primera implementación.

---

## 🔴 FASE 2 — Persistencia SQLite (SIGUIENTE — estimado 4-6h)

> Objetivo: Los datos persisten entre sesiones. Sin esto, todo se pierde al cerrar.

- [ ] **Ampliar `AbstractLifeManager`** — añadir `log_sleep()`, `get_sleep()`, `log_metric()`, `get_week_summary()`
- [ ] **Crear `SQLiteLifeManager`** en `impl/sqlite_lifemanager.py`
  - Conexión SQLite con `sqlite3` nativo (sin ORM en esta fase)
  - Tablas: `appointments`, `habits`, `sleep`
  - CRUD completo para cada entidad
- [ ] **Migrar `app.py`** para usar `SQLiteLifeManager` por defecto
- [ ] **Tests unitarios** en `tests/test_memory_lifemanager.py`
- [ ] **Tests de contrato** — mismos tests para Memory y SQLite
- [ ] **`requirements.txt`** con dependencias reales y versiones

**Entregable:** Datos persistentes en `data/life.db`. App funcional entre sesiones.

---

## 🟡 FASE 3 — API REST FastAPI (estimado 6-8h)

> Objetivo: Exponer todos los datos via HTTP. Permite integración con THDORA, dashboards, etc.

- [ ] **Crear `src/api/main.py`** — app FastAPI con CORS
- [ ] **Router `/appointments`**
  - `POST /appointments` — crear cita
  - `GET /appointments/{date}` — citas del día
  - `DELETE /appointments/{id}` — eliminar cita
- [ ] **Router `/habits`**
  - `POST /habits` — registrar hábito
  - `GET /habits/{date}` — hábitos del día
  - `GET /habits/{date}/summary` — resumen con métricas
- [ ] **Router `/summary`**
  - `GET /summary/{date}` — resumen completo del día
  - `GET /summary/week/{start_date}` — resumen semanal
- [ ] **Schemas Pydantic** — validación entrada/salida
- [ ] **Documentación Swagger** automática en `/docs`

**Entregable:** API REST completa. `uvicorn src.api.main:app --reload`

---

## 🟡 FASE 4 — CLI interactivo (estimado 3-4h)

> Objetivo: Usar el sistema desde terminal sin escribir código.

- [ ] **Crear `cli.py`** con `argparse` o `typer`
  - `python cli.py add-appointment --date 2026-03-25 --time 10:00 --type "Médico"`
  - `python cli.py log-habit --date 2026-03-24 --habit sueno --value 7h`
  - `python cli.py summary --date 2026-03-24`
  - `python cli.py week --start 2026-03-24`
- [ ] **Output formateado** — tablas con `rich` o similar
- [ ] **Manejo de errores** — fechas inválidas, hábitos duplicados
- [ ] **Tests CLI** — `pytest` con `subprocess` o `typer.testing`

**Entregable:** CLI usable desde terminal. Demo grabable para portfolio.

---

## 🟡 FASE 5 — Bot Telegram THDORA (estimado 6-8h)

> Objetivo: Gestionar citas y hábitos desde Telegram via THDORA.

- [ ] **Integrar `python-telegram-bot`**
- [ ] **Comando `/cita`** — crear cita conversacionalmente
- [ ] **Comando `/habito`** — registrar hábito del día
- [ ] **Comando `/hoy`** — resumen del día
- [ ] **Comando `/semana`** — resumen semanal con métricas
- [ ] **InlineKeyboards** para confirmaciones y navegación
- [ ] **Conectar con API Fase 3** (bot → API → SQLite)

**Entregable:** THDORA puede gestionar citas y tracking desde Telegram.

---

## ⚪ FASE 6 — Dashboard web (estimado 8-10h)

> Objetivo: Interfaz visual completa en el navegador.

- [ ] **`templates/index.html`** — dashboard principal
- [ ] **Vista calendario** — citas del mes
- [ ] **Vista hábitos** — gráficas de tendencias
- [ ] **Vista tracking** — métricas semanales
- [ ] **CSS moderno** — dark mode, responsive

**Entregable:** App web completa accessible en `http://localhost:8000`

---

## 📅 Timeline estimado

```
Semana 13 (24-30 mar):  Fase 2 — SQLiteLifeManager + tests
Semana 14 (31 mar-6 abr): Fase 3 — API REST FastAPI
Semana 15 (7-13 abr):  Fase 4 — CLI interactivo
Semana 16 (14-20 abr):  Fase 5 — Bot Telegram THDORA
Semana 17+ :             Fase 6 — Dashboard web
```

> ⚠️ Timeline condicionado a avance en Escuela Musk (M5/M6). El proyecto se desarrolla en paralelo, no en sustitución del estudio.

---

## 🏆 Criterios de proyecto completo

- [ ] Datos persisten entre sesiones (SQLite)
- [ ] API REST documentada y funcional
- [ ] Bot Telegram operativo con THDORA
- [ ] Tests con cobertura >70%
- [ ] README + documentación nivel profesional
- [ ] CI/CD con GitHub Actions
- [ ] Demo grabada para portfolio

---

_Creado: 24 marzo 2026 | Revisar y actualizar cada semana_
