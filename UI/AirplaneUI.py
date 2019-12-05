from Models.airplaneData import AirplaneData
from LL.mainLL import MainLL

class AirplaneMenu:
    def __init__(self):
        self.mainObject = MainLL()


    def addAirplane(self):
        planeId = input("Enter Airplane Id: ")
        type = input("Enter Airplane type: ")
        Model = input("Enter Airplane Model: ")
        capacity = input("Enter Airplane Capacity")
        newAirplane = AirplaneData(planeId, type,Model,capacity)
        self.mainObject.addNewAirplaneLL(newAirplane)
        print("PLane stored successfully")
        

    def showAirplanes(self):
        pass
        # return "Id:{}\nType:{}\nModel:{}\ncapacity:{}\n".format(planeId, type, Model, self.capacity)
    def showAirplaneStatus(self):
        pass

    def addLicenseToAirplane(self):
        pass





