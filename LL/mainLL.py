
from LL.staffLL import StaffLL
from LL.AirplaneLL import AirplaneLL

class MainLL:

    def __init__(self, dataList = None, model = None, flightFromKEF = None, flightToKEF = None):
        self.dataList = dataList
        self.model = model
        self.flightFromKEF = flightFromKEF
        self.flightToKEF = flightToKEF
        self.staffObject = StaffLL()
        self.airplaneObject = AirplaneLL()
        #self.airplaneObject = AirplaneLL()

    def getAllStaffLL(self):
        return self.staffObject.getAllStaff()

    def getAirplanesLL(self):
        return self.airplaneObject.getAirplanes()
    def getAllPilotsLL(self):
        return self.staffObject.getAllPilots()

    def getAllCabinCrewLL(self):
        return self.staffObject.getAllCabinCrew()
