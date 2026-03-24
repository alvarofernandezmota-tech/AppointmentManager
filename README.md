# 📅 AppointmentManager

> **Life Management System** — Gestión centralizada de citas, hábitos y métricas personales con arquitectura modular y extensible.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Layer%207%20ABC-green.svg)](./ARCHITECTURE.md)
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange.svg)](./ROADMAP.md)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](./LICENSE)

---

## 🎯 ¿Qué es AppointmentManager?

AppointmentManager es un sistema de gestión de vida personal construido sobre una **arquitectura abstracta de capas** (Layer 7). Permite gestionar citas, registrar hábitos y obtener resúmenes diarios a través de múltiples backends de persistencia que comparten la misma interfaz.

### 🌟 Características principales

- **Arquitectura modular** — Interfaz abstracta `AbstractLifeManager` que permite múltiples implementaciones (memoria, SQLite, API REST...)
- **Gestión de citas** — Crear, consultar y organizar citas por fecha
- **Tracking de hábitos** — Registrar y consultar hábitos diarios (sueño, tabaco, THC, ejercicio...)
- **Resumen diario** — Vista consolidada de citas + hábitos de cualquier día
- **Extensible** — Fácil añadir nuevas implementaciones sin cambiar la interfaz

---

## 🏗️ Arquitectura

```
AbstractLifeManager (ABC)          ← Contrato único
        │
        ├── MemoryLifeManager      ← In-memory (testing/desarrollo)
        ├── SQLiteLifeManager      ← Persistencia local [WIP]
        └── APILifeManager         ← REST API client [PLANNED]
```

Ver [ARCHITECTURE.md](./ARCHITECTURE.md) para el diseño completo.

---

## 🚀 Instalación rápida

### Requisitos
- Python 3.10+
- pip

### Setup

```bash
# Clonar el repositorio
git clone https://github.com/alvarofernandezmota-tech/AppointmentManager.git
cd AppointmentManager

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecución rápida

```bash
python app.py
```

---

## 📖 Uso básico

```python
from datetime import date
from impl.memory_lifemanager import MemoryLifeManager

# Inicializar manager
mgr = MemoryLifeManager()

# Crear una cita
mgr.create_appointment(date(2026, 3, 24), "16:00", "Consulta médica", notes="Llevar analítica")

# Registrar hábitos
mgr.log_habit(date(2026, 3, 24), "sueno", "7h")
mgr.log_habit(date(2026, 3, 24), "ejercicio", "no")
mgr.log_habit(date(2026, 3, 24), "THC", "0")

# Obtener resumen del día
summary = mgr.get_day_summary(date(2026, 3, 24))
print(summary)
# {
#   'date': '2026-03-24',
#   'appointments': [{'id': '...', 'time': '16:00', 'type': 'Consulta médica', 'notes': 'Llevar analítica'}],
#   'habits': {'sueno': '7h', 'ejercicio': 'no', 'THC': '0'}
# }
```

---

## 📁 Estructura del proyecto

```
AppointmentManager/
├── README.md                        # Este archivo
├── ARCHITECTURE.md                  # Diseño técnico detallado
├── ROADMAP.md                       # Plan de desarrollo
├── CHANGELOG.md                     # Historial de versiones
├── requirements.txt                 # Dependencias Python
├── .gitignore                       # Archivos ignorados por git
├── app.py                           # Punto de entrada / demo
├── src/
│   └── interfaces/
│       ├── __init__.py
│       └── abstract_lifemanager.py  # Contrato ABC Layer 7
├── impl/
│   ├── __init__.py
│   └── memory_lifemanager.py        # Implementación en memoria
└── tests/                           # Tests (WIP)
    └── ...
```

---

## 🧪 Tests

```bash
pip install pytest
pytest tests/ -v
```

> ⚠️ Tests en desarrollo — ver [ROADMAP.md](./ROADMAP.md) Fase 2.

---

## 🗺️ Roadmap

| Fase | Descripción | Estado |
|------|-------------|--------|
| ✅ Fase 1 | Interfaz abstracta + MemoryLifeManager | Completada |
| 🔴 Fase 2 | SQLiteLifeManager + persistencia real | En desarrollo |
| 🔴 Fase 3 | API REST FastAPI | Planificada |
| 🟡 Fase 4 | CLI interactivo | Planificada |
| 🟡 Fase 5 | Bot Telegram integrado | Planificada |

Ver [ROADMAP.md](./ROADMAP.md) para el plan completo.

---

## 🤝 Contribuir

1. Fork del repositorio
2. Crear rama: `git checkout -b feature/nueva-implementacion`
3. Commit con convencion: `feat: descripcion`, `fix: descripcion`, `docs: descripcion`
4. Pull Request con descripción detallada

---

## 👤 Autor

**Álvaro Fernández Mota**  
🔗 [GitHub](https://github.com/alvarofernandezmota-tech)  
📍 Guadalajara, España  

---

## 📄 Licencia

MIT License — ver [LICENSE](./LICENSE)

---

_Creado: 19 marzo 2026 | Última actualización: 24 marzo 2026_
