import csv
from airplaneData import AirplaneData
import airplaneData

class AirplaneIO():
    def __init__(self):

        self.path = "AircraftType.csv"


    def makeDataList(self):
        pass
    def writeNewAirplane(self, newAirplane):

        with open(self.path, "a") as airplaneFile:
            fieldnames = ["planeTypeId","planeType","model","capacity","emptyWeight","maxTakeoffWeight","unitThrust","serviceCeiling","length","height","wingspan"]
            writer = csv.DictWriter(airplaneFile, fieldnames=fieldnames)
            writer.writerow({"planeTypeId": newAirplane.getPlaneId(), "planeType": newAirplane.getType() })
            #writer.writerow(newAirplaneList)





