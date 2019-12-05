
from LL.staffLL import StaffLL

class MainLL:

    def __init__(self, dataList = None, model = None, flightFromKEF = None, flightToKEF = None):
        self.dataList = dataList
        self.model = model
        self.flightFromKEF = flightFromKEF
        self.flightToKEF = flightToKEF
        self.staffObject = StaffLL()
        #self.airplaneObject = AirplaneLL()

    def getAllStaffLL(self):
        return self.staffObject.getAllStaff()

    def getAllPilotsLL(self):
        return self.staffObject.getAllPilots()

    def getAllCabinCrewLL(self):
        return self.staffObject.getAllCabinCrew()

    def getStaffDataLL(self):
        return self.staffObject.getStaffData(self.dataList)