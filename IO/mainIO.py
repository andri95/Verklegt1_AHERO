from IO.createIO import CreateIO
from IO.readIO import ReadIO
from IO.updateIO import UpdateIO


class MainIO:
    '''The class contains functions that call the correct IO class depending on if it has to read, create or update. If it needs to
    read, then there are no parameters necessary. If it needs to create Then a instance is necessary. '''
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

    def addNewVoyageIO(self, newVoyage):
        return self.createObject.addNewVoyage(newVoyage)

    def getDestinationsIO(self):
        return self.readObject.getDestinations()

    def getVoyagesIO(self):
        return self.readObject.getVoyages()

    def getStaffIO(self):
        return self.readObject.getStaff()

    def getAirplanesIO(self):
        return self.readObject.getAirplanes()

    def updateVoyageIO(self, dataList, staffList):
        '''When updating a voyage, we need the voyage and the staff that was assigned to the voyage'''
        return self.updateObject.updateVoyage(dataList, staffList)

    def updateDestIO(self, dataList):
        return self.updateObject.updateDest(dataList)

    def addLicenseIO(self, dataList):
        return self.updateObject.addLicense(dataList)