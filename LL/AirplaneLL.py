from IO.readIO import ReadIO
from LL.AirplaneLL import AirplaneLL


class AirplaneLL():
    def __init__(self):
        self.readIo = ReadIO()

    def validateAirPlaneData(self, new_airplane):
        print(type(new_airplane))
        flag = True
        if flag == True:
            #self.AirplaneIO.addNewAirplane(new_airplane)
            return True

    def getAirplanes(self):
        return self.readIo.getAirplanes()

    def getAirplaneStatus(self):
        pass

    def addLicense(self):
        pass

    def __str__(self):
        return
        #return"{}".format(self.AirplaneIO)



#print(new_airplane)



