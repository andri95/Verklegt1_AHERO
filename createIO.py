import csv
from flightData import FlightData
from staffData import StaffData


class CreateIO():
    def __init__(self):
        self.aircraftPath = "AircraftType.csv"
        self.crewPath = "Crew.csv"
        self.destinationPath = "DestinationData.csv"
        self.upcomingFlightsPath = "UpcomingFlights.csv"
        self.upcomingVoyagesPath = "UpcomingVoyages.csv"



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
                             "license": newEmployee.getLicence()})

    def addNewDest(self, newDestination):
        with open(self.destinationPath, "a") as destinationFile:
            fieldnames = ["destName","flightTime","distance","contact","phoneNumber"]
            writer = csv.DictWriter(destinationFile, fieldnames=fieldnames)
            writer.writerow({"destName": newDestination.getDestName(),"flightTime": newDestination.getFlightTime(),
                             "distance": newDestination.getDistance(),"contact": newDestination.getPhoneNumber(),
                             "phoneNumber": newDestination.getContact()})


    def addNewFlight(self, newFlight):
        with open(self.upcomingFlightsPath, "a") as flightsFile:
            fieldnames = ["flightNumber", "departingFrom", "arrivingAt", "departure", "arrival"]
            writer = csv.DictWriter(flightsFile, fieldnames=fieldnames)
            writer.writerow({"flightNumber": newFlight.getFlightNumber(), "departingFrom": newFlight.getDepartingFrom(),
                             "arrivingAt": newFlight.getDrrivingAt(), "departure": newFlight.getDeparture(),
                             "arrival": newFlight.getArrival()})

    def addNewVoyage(self, newVoyage):
        with open(self.upcomingVoyagesPath, "a") as voyageFile:
            fieldnames = ["flightNumber", "departingFrom", "arrivingAt", "departure", "arrival", "aircraftID",
                          "captain", "copilot", "fa1", "fa2"]
            writer = csv.DictWriter(voyageFile, fieldnames=fieldnames)
            writer.writerow(
                {"flightNumber": newVoyage.getFlightDep_obj().getFlightNumber(), "departingFrom": newVoyage.(),
                 "arrivingAt": newVoyage.(),
                 "departure": newVoyage.(), "arrival": newVoyage.(), "aircraftID": newVoyage.(),
                 "captain": newVoyage.(), "copilot": newVoyage.(), "fa1": newVoyage.(),
                 "fa2": newVoyage.()})



newFlight = FlightData("NAN911", "MARS", "EARTH", "NOW", "NEVER")
CreateIO().addNewFlight(newFlight)

newAircraft = StaffData("1", "2", "3", "4", "5", "6", "7", "8")
CreateIO().addNewStaff(newAircraft)







