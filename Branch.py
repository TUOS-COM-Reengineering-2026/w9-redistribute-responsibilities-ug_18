from Staff import Staff


class Branch:
    def __init__(self, location, opening_time: str = "9:00"):
        self._location = location
        self._staff = []
        self._opening_time = opening_time

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_staff(self):
        return self._staff

    def add_staff_member(self, staff: Staff):
        self._staff.append(staff)

    def remove_staff_member(self, staff: Staff):
        self._staff.remove(staff)

    def get_opening_time(self):
        return self._opening_time

    def set_opening_time(self, opening_time):
        self._opening_time = opening_time
