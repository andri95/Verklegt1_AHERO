
from LL.staffLL import StaffLL
from LL.AirplaneLL import AirplaneLL

class MainLL:

    def __init__(self):
        self.staffObject = StaffLL()
        self.airplaneObject = AirplaneLL()
       

    def getAllStaffLL(self):
        return self.staffObject.getAllStaff()

    def getAirplanesLL(self):
        return self.airplaneObject.getAirplanes()
    def getAllPilotsLL(self):
        return self.staffObject.getAllPilots()

    def getAllCabinCrewLL(self):
        return self.staffObject.getAllCabinCrew()

    def getStaffDataLL(self, dataList):
        return self.staffObject.getStaffData(dataList)

    def addNewStaffLL(self, newEmployee):
        return self.staffObject.addNewStaff(newEmployee)
        
