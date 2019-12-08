from IO.mainIO import MainIO



class AirplaneLL:
    def __init__(self):
        self.mainObject = MainIO()


    def validateAirPlaneData(self, new_airplane):
        print(type(new_airplane))
        flag = True
        if flag == True:
            #self.AirplaneIO.addNewAirplane(new_airplane)
            return True

    def addAirplane(self, newAirplane):
        return self.mainObject.addNewAirplaneIO(newAirplane)

    def getAirplanes(self):
        return self.mainObject.getAirplanesIO()

    def getAirplaneStatus(self):
        pass

    def addLicense(self):
        pass

    def __str__(self):
        return
        #return"{}".format(self.AirplaneIO)



#print(new_airplane)



