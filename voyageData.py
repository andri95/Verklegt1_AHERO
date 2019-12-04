class VoyageData:
    def __init__(self, flightDep_obj, flightArr_obj, pilot, coPilot, fa1, fa2, airplane):
        self.flightDep_obj = flightDep_obj
        self.flightArr_obj = flightArr_obj
        self.pilot = pilot
        self.coPilot = coPilot
        self.fa1 = fa1
        self.fa2 = fa2
        self.airplane = airplane



    def getFlightDep_obj(self):
        return self.flightDep_obj

    def getFlightArr_obj(self):
        return self.flightArr_obj

    def getPilot(self):
        return self.pilot



    #def __str__(self):

        #return 'First leg:\n{}\nSecond leg:\n{}'.format(self.flightDep_obj, self.flightArr_obj)

''' ÓKLÁRAÐ, ÞURFUM AÐ GERA READIO FYRSTt'''
