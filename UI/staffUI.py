#from StaffData import StaffData
from staffLL import StaffLL

class StaffUI:

    def __init__(self):
        self.StaffLL = StaffLL()

    def getAllStaff(self):
        staffMembers = StaffLL()
        return staffMembers.getAllStaffLL


staff = StaffUI()
staff.getAllStaff()