import csv
from airplaneData import AirplaneData
import airplaneData

class AirplaneIO():
    def __init__(self):
        self.aircraftPath = "AircraftType.csv"
        self.crewPath = "Crew.csv"
        self.destinationPath = "Destinations.csv"


    def addNewAirplane(self, newAirplane):
        with open(self.aircraftPath, "a") as airplaneFile:
            fieldnames = ["planeTypeId","planeType","model","capacity"]
            writer = csv.DictWriter(airplaneFile, fieldnames=fieldnames)
            writer.writerow({"planeTypeId": newAirplane.getPlaneId(), "planeType": newAirplane.getType(),
                             "model": newAirplane.getModel(), "capacity": newAirplane.getCapacity()})


    def addNewStaff(self, newEmployee):
        with open(self.crewPath, "a") as crewFile:
            fieldnames = ["ssn", "name", "address", "cellPhone", "phoneNumber", "email", "role", "rank", "license"]
            writer = csv.DictWriter(crewFile, fieldnames=fieldnames)
            writer.writerow({"ssn": newEmployee.getSSN(), "name": newEmployee.getName(), "address": newEmployee.getAddress(),
                             "cellPhone": newEmployee.getCellPhone(), "phoneNumber": newEmployee.getPhoneNumber(),
                             "email": newEmployee.getEmail(), "role": newEmployee.getRole(), "rank": newEmployee.getRank(),
                             "license": newEmployee.getLicense()})








