import csv
from Models.flightData import FlightData
from Models.staffData import StaffData
from Models.voyageData import VoyageData
from Models.flightData import FlightData
from Models.airplaneData import AirplaneData
from Models.destinationData import DestinationData



class CreateIO():
    def __init__(self):
        self.aircraftPath = "../Data/AircraftType.csv"
        self.crewPath = "../Data/Crew.csv"
        self.destinationPath = "../Data/DestinationData.csv"
        self.upcomingFlightsPath = "../Data/UpcomingFlights.csv"
        self.upcomingVoyagesPath = "../Data/UpcomingVoyages.csv"



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
                             "arrivingAt": newFlight.getArrivingAt(), "departure": newFlight.getDeparture(),
                             "arrival": newFlight.getArrival()})


    def addNewVoyage(self, flightFromKEF, flightToKEF, newVoyage):
        flight1 = flightFromKEF.getFlightNumber()
        flight2 = flightToKEF.getFlightNumber()
        departingFrom = flightFromKEF.getDepartingFrom()
        arrivingAt = flightFromKEF.getArrivingAt()
        departureFromKEF = flightFromKEF.getDeparture()
        arrivalToKEF = flightToKEF.getArrival()
        with open(self.upcomingVoyagesPath, "a") as voyageFile:
            fieldnames = ["flightNumber1", "flightNumber2", "departingFrom", "arrivingAt", "departureFromKEF",
                          "arrivalToKEF", "aircraftID","captain", "coPilot", "fa1", "fa2"]
            writer = csv.DictWriter(voyageFile, fieldnames=fieldnames)
            writer.writerow({"flightNumber1": flight1, "flightNumber2": flight2, "departingFrom": departingFrom,
                             "arrivingAt": arrivingAt, "departureFromKEF": departureFromKEF, "arrivalToKEF": arrivalToKEF,
                             "aircraftID": newVoyage.getAirplane(), "captain": newVoyage.getPilot(), "coPilot": newVoyage.getCoPilot(),
                             "fa1": newVoyage.getFa1(), "fa2": newVoyage.getFa2()})








