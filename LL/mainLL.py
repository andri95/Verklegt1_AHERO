
from LL.staffLL import StaffLL
from LL.airplaneLL import AirplaneLL
from LL.destinationLL import DestinationLL
from LL.voyageLL import VoyageLL

class MainLL:

    def __init__(self):
        self.staffObject = StaffLL()
        self.airplaneObject = AirplaneLL()
        self.destinationObject = DestinationLL()
        self.voyageObject = VoyageLL()
       

    def getAllStaffLL(self):
        return self.staffObject.getAllStaff()
    
    def getStaffByIDLL(self, ssn):
        return self.staffObject.getStaffByID(ssn)

    def getAirplanesLL(self):
        return self.airplaneObject.getAirplanes()

    def getVoyageLL(self):
        return self.voyageObject.listVoyage()

    def getAllPilotsLL(self):
        return self.staffObject.getAllPilots()

    def getAllCabinCrewLL(self):
        return self.staffObject.getAllCabinCrew()

    def addAirplaneLL(self, newAirplane):
        return self.airplaneObject.addAirplane(newAirplane)

    def getStaffDataLL(self, dataList):
        return self.staffObject.getStaffData(dataList)

    def addNewStaffLL(self, newEmployee):
        return self.staffObject.addNewStaff(newEmployee)
        
    def getAllDestinationsLL(self):
        return self.destinationObject.getDestination()

    def addNewDestinationLL(self, newDestination):
        return self.destinationObject.addNewDestination(newDestination)

    def addNewVoyage(self, newFlight):
        return self.voyageObject.addVoyages(newFlight)

    def updateVoyage(self, dataList, staffList):
        return self.voyageObject.updateVoyage(dataList, staffList)


