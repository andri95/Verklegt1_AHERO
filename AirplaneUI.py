from airplaneData import AirplaneData
from AirplaneLL import AirplaneLL


class AirplaneUI():
    def __init__(self):
        self.AirplaneLL = AirplaneLL()


    def addAirplane(self):
        planeId = input("Enter Airplane Id: ")
        type = input("Enter Airplane type: ")
        Model = input("Enter Airplane Model: ")
        capacity = input("Enter Airplane Capacity")
        newAirplane = AirplaneData(planeId, type,Model,capacity)

        if self.AirplaneLL.validateAirPlaneData(newAirplane):
            print("PLane stored successfully")
        else:
            print("No success try again")

    def showAirplanes(self):
        pass
        # return "Id:{}\nType:{}\nModel:{}\ncapacity:{}\n".format(planeId, type, Model, self.capacity)
    def showAirplaneStatus(self):
        pass

    def addLicenseToAirplane(self):
        pass

new_airplane = AirplaneUI()
new_airplane.addAirplane()
#print(new_airplane)





