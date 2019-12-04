
class VoyageData:
    def __init__(self, flightDep, flightArr, departureFromKEF, arrivalToKEF, pilot, coPilot, fa1, fa2, airplane):
        self.flightDep = flightDep
        self.flightArr = flightArr
        self.departureFromKEF = departureFromKEF
        self.arrivalToKEF = arrivalToKEF
        self.pilot = pilot
        self.coPilot = coPilot
        self.fa1 = fa1
        self.fa2 = fa2
        self.airplane = airplane


    def getFlightDep(self):
        return self.flightDep

    def getFlightArr(self):
        return self.flightArr

    def getDepartureFromKEF(self):
        return self.departureFromKEF

    def getArrivalToKEF(self):
        return self.arrivalToKEF

    def getPilot(self):
        return self.pilot

    def getCoPilot(self):
        return self.coPilot

    def getFa1(self):
        return self.fa1

    def getFa2(self):
        return self.fa2

    def getAirplane(self):
        return self.airplane



    #def __str__(self):

        #return 'First leg:\n{}\nSecond leg:\n{}'.format(self.flightDep_obj, self.flightArr_obj)


