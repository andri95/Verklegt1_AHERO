
from IO.mainIO import MainIO

class StaffLL:

    def __init__(self):
        self.mainObject = MainIO()       

    def getAllStaff(self):
        return self.mainObject.getStaffIO()

    def getAllPilots(self):
        staffObject_list = self.mainObject.getStaffIO()
        pilotObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRole() == 'Pilot':
                pilotObject_list.append(staffMember)
        return pilotObject_list

    def getAllCabinCrew(self):
        staffObject_list = self.mainObject.getStaffIO()
        cabinCrewObject_list = []
        for staffMember in staffObject_list:
            if staffMember.getRole() == 'Cabincrew':
                cabinCrewObject_list.append(staffMember)
        return cabinCrewObject_list

    def getStaffData(self, dataList):
        staffObject_list = self.mainObject.getStaffIO()
        for staffMember in staffObject_list:
            if staffMember.getSSN() == dataList[0]:
                return staffMember

    

