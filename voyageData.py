from flightData import FlightData

class VoyageData:
    def __init__(self, flightDep_obj, flightArr_obj):
        self.flightDep_obj = flightDep_obj
        self.flightArr_obj = flightArr_obj

    def __str__(self):
        return 'First leg:\n{}\nSecond leg:\n{}'.format(self.flightDep_obj, self.flightArr_obj)

    def getFlightDep(self):
        return self.flightDep_obj   #  Return flight departure object

    def getFlightArr(self):
        return self.flightArr_obj  #  Return flight array(list) object

    
