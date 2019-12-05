
class VoyageData:
    def __init__(self, flight1, flight2,pilot, coPilot, fa1, fa2, airplane):
        self.flightNumber1 = flight1
        self.flightNumber2 = flight2
        self.pilot = pilot
        self.coPilot = coPilot
        self.fa1 = fa1
        self.fa2 = fa2
        self.airplane = airplane


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

    def __str__(self):
        return 'First leg:\n{}\nSecond leg:\n{}'.format(self.flightDep_obj, self.flightArr_obj)

    def getFlightDep(self):
        return self.flightDep_obj   #  Return flight departure object

    def getFlightArr(self):
        return self.flightArr_obj  #  Return flight array(list) object

    

