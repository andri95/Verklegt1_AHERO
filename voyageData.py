from flightData import FlightData

class VoyageData:
    def __init__(self, flightDep_obj, flightArr_obj, pilot, coPilot, f1, f2):
        self.flightDep_obj = flightDep_obj
        self.flightArr_obj = flightArr_obj
        self.pilot = pilot
        self.coPilot = coPilot
        self.f1 = f1
        self.f2 = f2


    def getFlightDep_obj(self):
        pass
    def __str__(self):

        return 'First leg:\n{}\nSecond leg:\n{}'.format(self.flightDep_obj, self.flightArr_obj)

''' ÓKLÁRAÐ, ÞURFUM AÐ GERA READIO FYRST'''