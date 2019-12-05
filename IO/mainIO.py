from IO.createIO import CreateIO
from IO.readIO import ReadIO
from IO.updateIO import UpdateIO


class MainIO:

    def __init__(self, dataList = None, model = None, flightFromKEF = None, flightToKEF = None):
        self.dataList = dataList
        self.model = model
        self.flightFromKEF = flightFromKEF
        self.flightToKEF = flightToKEF
        self.createObject = CreateIO()
        self.readObject = ReadIO()
        self.updateObject = UpdateIO()

    def addNewAirplaneIO(self):
        return self.createObject.addNewFlight(self.model)

    def addNewStaffIO(self):
        return self.createObject.addNewStaff(self.model)

    def addNewDestIO(self):
        return self.createObject.addNewDest(self.model)

    def addNewFlightIO(self):
        return self.createObject.addNewFlight(self.model)

    def addNewVoyageIO(self):
        return self.createObject.addNewVoyage(self.flightFromKEF, self.flightToKEF, self.model)

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

    def updateDestIO(self):
        return self.updateObject.updateDest(self.dataList)

    def addLicenseIO(self):
        return self.updateObject.addLicense(self.dataList)

    

    

    