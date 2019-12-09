from IO.mainIO import MainIO

class VoyageLL():
    def __init__(self):
        self.mainObject = MainIO()
  
    def listVoyage(self):
        return self.mainObject.getVoyagesIO()

    def addVoyages(self, newFlight):
        return self.mainObject.addNewVoyageIO(newFlight)

    def updateVoyage(self, dataList, staffList):
        return self.mainObject.updateVoyageIO(dataList, staffList)

    def generateFlightNumber(self, flight):
        destination = flight.getArrivingAt()
        destinationList = self.mainObject.getDestinationsIO()
        for dest in destinationList:
            if dest.getCountry() == destination:
                return dest.getDestId()
            else:
                print(destination, "is not a valid destination")
