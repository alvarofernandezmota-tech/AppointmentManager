from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import date
from uuid import UUID

class AbstractLifeManager(ABC):
    """Super interfaz Layer 7 - Appointments + Habits"""

    @abstractmethod
    def create_appointment(self, date: date, time: str, type: str, notes: str = "") -> UUID:
        """Crear cita -> ID unico"""
        pass

    @abstractmethod
    def get_appointments(self, date: date) -> List[Dict]:
        """Citas del dia"""
        pass

    @abstractmethod
    def log_habit(self, date: date, habit: str, value: str) -> bool:
        """THC/tabaco/sueno"""
        pass

    @abstractmethod
    def get_habits(self, date: date) -> Dict[str, str]:
        pass

    @abstractmethod
    def get_day_summary(self, date: date) -> Dict:
        """Appointments + Habits dia completo"""
        pass
