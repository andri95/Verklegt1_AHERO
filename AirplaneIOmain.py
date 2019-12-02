import csv
from AirplaneLLmain import new_airplane
from airplaneData import AirplaneData

class AirplaneIO():
    def __init__(self):

        self.path = "AircraftType.csv"

    def writeNewAirplane(self):
        with open(self.path, "a") as airplaneFile:
            writer = csv.writer(airplaneFile)
            #writer.writerow(newAirplaneList)
            return




