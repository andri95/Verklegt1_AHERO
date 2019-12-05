
from IO.mainIO import MainIO

class StaffLL:

    def __init__(self):
        self.mainObject = MainIO()       

    def getAllStaff(self):
        return self.mainObject.getStaffIO()
