from IO.createIO import CreateIO
from IO.readIO import ReadIO
from IO.updateIO import UpdateIO


class MainIO:

    def __init__(self):
        self.createObject = CreateIO()
        self.readObject = ReadIO()
        self.updateObject = UpdateIO()

    def addNewAirplaneIO(self, newAirplane):
        return self.createObject.addNewAirplane(newAirplane)

    def addNewStaffIO(self, newEmployee):
        return self.createObject.addNewStaff(newEmployee)

    def addNewDestIO(self, newDestination):
        return self.createObject.addNewDest(newDestination)

    def addNewFlightIO(self, newFlight):
        return self.createObject.addNewFlight(newFlight)

    def addNewVoyageIO(self, flightFromKEF, flightToKEF, newVoyage):
        return self.createObject.addNewVoyage(flightFromKEF, flightToKEF, newVoyage)

    def getDestinationsIO(self):
        return self.readObject.getDestinations()

    def getVoyagesIO(self):
        return self.readObject.getVoyages()

    def getStaffIO(self):
        return self.readObject.getStaff()

    def getAirplanesIO(self):
        return self.readObject.getAirplanes()

    def getFlightsIO(self):
        return self.readObject.getFlights()

    def updateDestIO(self, dataList):
        return self.updateObject.updateDest(dataList)

    def addLicenseIO(self, dataList):
        return self.updateObject.addLicense(dataList)