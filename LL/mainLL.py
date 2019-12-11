
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
        
    def getAirplaneByIdLL(self,ID):  #Er eitthva ad ruglast
        return self.airplaneObject.getAirplaneByID(ID)  # var ad breyta

    def getVoyageLL(self):
        return self.voyageObject.listVoyage()

    def getAllPilotsLL(self):
        return self.staffObject.getAllPilots()
    
    def getLicenseDictLL(self):  # Er eitthvad ad ruglast
        return self.airplaneObject.getLicenseDict()

    def getAllCabinCrewLL(self):
        return self.staffObject.getAllCabinCrew()

    def addAirplaneLL(self, newAirplane):
        return self.airplaneObject.addAirplane(newAirplane)

    def getAirplaneStatusLL(self, date, time):
        return self.airplaneObject.getAirplaneStatus(date, time)

    def getStaffDataLL(self, dataList):
        return self.staffObject.getStaffData(dataList)

    def addNewStaffLL(self, newEmployee):
        return self.staffObject.addNewStaff(newEmployee)
        
    def getAllDestinationsLL(self):
        return self.destinationObject.getDestination()

    def addNewDestinationLL(self, newDestination):
        return self.destinationObject.addNewDestination(newDestination)

    def addNewVoyageLL(self, newFlight):
        return self.voyageObject.addVoyages(newFlight)

    def updateVoyageLL(self, dataList, staffList):
        return self.voyageObject.updateVoyage(dataList, staffList)

    def updateDestinationLL(self, dataList):
        return self.destinationObject.updateDestination(dataList)

    def addLicenseLL(self, dataList):
        return self.airplaneObject.addLicense(dataList)

    def workScheduleLL(self, workDay):
        return self.staffObject.getWorkSchedule(workDay)

    def workScheduleAvailableLL(self, workDay):
        return self.staffObject.getWorkSchedlueAvailable(workDay)

    def generateFlightNumberLL(self, flight):
        return self.voyageObject.generateFlightNumber(flight)

    def availableDatesLL(self):
        return self.voyageObject.availableDates()
    
    def workWeekLL(self, dataList):
        return self.voyageObject.getWorkWeek(dataList)
