from uuid import uuid4, UUID
from datetime import date
from src.interfaces.abstract_lifemanager import AbstractLifeManager
from typing import List, Dict

class MemoryLifeManager(AbstractLifeManager):
    def __init__(self):
        self.appointments = {}
        self.habits = {}

    def create_appointment(self, date: date, time: str, type: str, notes: str = "") -> UUID:
        apt_id = uuid4()
        date_str = str(date)
        if date_str not in self.appointments:
            self.appointments[date_str] = []
        self.appointments[date_str].append({
            'id': str(apt_id),
            'time': time,
            'type': type,
            'notes': notes
        })
        return apt_id

    def get_appointments(self, date: date) -> List[Dict]:
        return self.appointments.get(str(date), [])

    def log_habit(self, date: date, habit: str, value: str) -> bool:
        date_str = str(date)
        if date_str not in self.habits:
            self.habits[date_str] = {}
        self.habits[date_str][habit] = value
        return True

    def get_habits(self, date: date) -> Dict[str, str]:
        return self.habits.get(str(date), {})

    def get_day_summary(self, date: date) -> Dict:
        return {
            'date': str(date),
            'appointments': self.get_appointments(date),
            'habits': self.get_habits(date)
        }
