from IOLayer.createIO import AirplaneIO

class AirplaneLL():
    def __init__(self):
        self.AirplaneIO = AirplaneIO()



    def validateAirPlaneData(self, new_airplane):
        print(type(new_airplane))
        flag = True
        if flag == True:
            self.AirplaneIO.addNewAirplane(new_airplane)
            return True

    def getAirplanes(self):
        pass

    def getAirplaneStatus(self):
        pass

    def addLicense(self):
        pass

    def __str__(self):
        return"{}".format(self.AirplaneIO)



#print(new_airplane)



