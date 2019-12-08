from IO.mainIO import MainIO

class VoyageLL:
    def __init__(self):
        self.MainObject = MainIO()

    
    def listVoyage(self):
        return self.MainObject.getVoyagesIO()

    def addVoyages(self, newFlight):
        return self.MainObject.addNewFlightIO(newFlight)

    def listFlights(self):
        return self.MainObject.getFlightsIO()
