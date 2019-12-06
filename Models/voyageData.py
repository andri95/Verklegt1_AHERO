
class VoyageData:
    def __init__(self, flightNumber, departingFrom, arrivingAt, departureTime, arrivalTime, aircraftId, captain=None, coPilot=None, fa1=None, fa2=None):
        self.flightNumber = flightNumber
        self.departingFrom = departingFrom
        self.arrivingAt = arrivingAt
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.aircraftId = aircraftId
        self.captain = captain
        self.coPilot = coPilot
        self.fa1 = fa1
        self.fa2 = fa2

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




    def __str__(self):
        return f"Pilot: {self.pilot} Co-pilot. {self.coPilot} Flight attendants: {self.fa1} {self.fa2} Airplane: {self.airplane}"




    def __str__(self):
        return 'First leg:\n{}\nSecond leg:\n{}'.format(self.flightDep_obj, self.flightArr_obj)

    def getFlightDep(self):
        return self.flightDep_obj   #  Return flight departure object

    def getFlightArr(self):
        return self.flightArr_obj  #  Return flight array(list) object

    

