from staffIO import StaffIO

class StaffLL:

    def __init__(self):
        self.StaffIO = StaffIO()

    def getAllStaffLL(self):
        staffMembersIO = StaffIO()
        return staffMembersIO.getAllStaffIO