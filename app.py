from datetime import date
from impl.memory_lifemanager import MemoryLifeManager

mgr = MemoryLifeManager()

mgr.create_appointment(date(2026,3,19), "12:00", "Asociacion Thea")
mgr.create_appointment(date(2026,3,19), "14:00", "Burger King mama")
mgr.log_habit(date(2026,3,19), "sueno", "8h")
mgr.log_habit(date(2026,3,19), "THC", "0")

if __name__ == "__main__":
    print("Summary 19/03:")
    print(mgr.get_day_summary(date(2026,3,19)))
    print("AppointmentManager v1.0 Layer 7 ready")
