from Staff import Staff
from typing import List


class Branch:
    def __init__(self, location: str, opening_time: str = "9:00"):
        self._location: str = location
        self._staff: List[Staff] = []
        self._opening_time: str = opening_time

    def get_location(self):
        return self._location

    def set_location(self, location: str):
        self._location = location

    def get_staff(self):
        return self._staff
    
    def get_opening_time(self):
        return self._opening_time

    def add_staff(self, staff: Staff):
        self._staff.append(staff)

    def remove_staff(self, staff: Staff):
        self._staff.remove(staff)

    def set_opening_time(self, opening_time: str):
        self._opening_time = opening_time
