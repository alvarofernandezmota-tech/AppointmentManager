# 📋 CHANGELOG — AppointmentManager

Todos los cambios notables de este proyecto se documentan aquí.

Formato basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/)  
Versionado semántico: [SemVer](https://semver.org/lang/es/)

---

## [Unreleased]

### Planned
- SQLiteLifeManager — persistencia real
- Tests unitarios y de contrato
- requirements.txt completo

---

## [0.1.0] — 2026-03-19

### Added
- Estructura inicial del repositorio
- `AbstractLifeManager` — interfaz abstracta ABC Layer 7
  - `create_appointment()` — crear cita con UUID
  - `get_appointments()` — consultar citas por fecha
  - `log_habit()` — registrar hábito diario
  - `get_habits()` — consultar hábitos por fecha
  - `get_day_summary()` — resumen diario completo
- `MemoryLifeManager` — implementación en memoria
- `app.py` — script de demostración
- Estructura de carpetas: `src/interfaces/`, `impl/`

### Notes
- Creado en Toledo, 19 marzo 2026
- Primer commit: arquitectura base Layer 7

---

## [0.2.0] — 2026-03-24 (docs)

### Added
- `README.md` completo a nivel profesional
- `ARCHITECTURE.md` — diseño técnico detallado con diagramas
- `ROADMAP.md` — plan de desarrollo completo (6 fases, 30 tareas)
- `CHANGELOG.md` — este archivo
- `.gitignore` — Python estándar

### Changed
- Estructura documentada completamente

---

_[Unreleased]: https://github.com/alvarofernandezmota-tech/AppointmentManager/compare/v0.2.0...HEAD_  
_[0.2.0]: https://github.com/alvarofernandezmota-tech/AppointmentManager/compare/v0.1.0...v0.2.0_  
_[0.1.0]: https://github.com/alvarofernandezmota-tech/AppointmentManager/releases/tag/v0.1.0_
