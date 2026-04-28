from Staff import Staff


class Branch:

    def __init__(self, location, opening_time="9:00"):
        self._location = location
        self._staff = []
        self.opening_time = opening_time

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_staff(self):
        return self._staff
    
    def add_staff(self, staff):
        self.staff.append(staff)

    def remove_staff(self, staff):
        self.staff.remove(staff)

    def set_branch_opening_time(self, opening_time):
        self.opening_time = opening_time