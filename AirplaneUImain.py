from airplaneData import AirplaneData
from AirplaneLLmain import AirplaneLL


class AirplaneUI:
    def __init__(self):
        self.AirplaneLL = AirplaneLL()

    def addAirplane(self):
        planeId = input("Enter Airplane Id: ")
        type = input("Enter Airplane type: ")
        manufacturer = input("Enter Airplane manufacturer: ")
        capacity = input("Enter Airplane Capacity")
        newAirplane = AirplaneData(planeId, type,manufacturer,capacity)

        if AirplaneLL.validate_plane(newAirplane):
            print("PLane stored successfully")
        else:
            print("No success try again")

    def showAirplanes(self):
        pass

    def showAirplaneStatus(self):
        pass

    def addLicenseToAirplane(self):
        pass


    #def __str__(self):
        #return "Id:{}\nType:{}\nmanufacturer:{}\ncapacity:{}\n".format(planeId, type, manufacturer, self.capacity)




