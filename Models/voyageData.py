
class VoyageData:
    def __init__(self, flightNumber, departingFrom, arrivingAt, departureTime, arrivalTime,
    aircraftId, captain="", coPilot="", fa1="", fa2=""):
        self.departingFrom = departingFrom
        self.arrivingAt = arrivingAt
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.aircraftId = aircraftId
        self.captain = captain
        self.coPilot = coPilot
        self.fa1 = fa1
        self.fa2 = fa2
        self.flightNumber = flightNumber

    def getFlightNumber(self):
        return self.flightNumber

    def getDepartingFrom(self):
        return self.departingFrom

    
    def getArrivingAt(self):
        return self.arrivingAt

    def getDepartureTime(self):
        return self.departureTime

    def getArrivalTime(self):
        return self.arrivalTime

    def getAircraftId(self):
        return self.aircraftId

    def getCaptain(self):
        return self.captain

    def getCoPilot(self):
        return self.coPilot

    def getFa1(self):
        return self.fa1

    def getFa2(self):
        return self.fa2

    def setCaptain(self, captain):
        self.captain = captain

    def setCoPilot(self, coPilot):
        self.coPilot = coPilot

    def setFa1(self, fa1):
        self.fa1 = fa1

    def setFa2(self, fa2):
        self.fa2 = fa2

    def setFlightNumber(self, flightNumber):
        self.flightNumber = flightNumber


    

