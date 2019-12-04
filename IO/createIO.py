import csv
from Models.flightData import FlightData
from Models.staffData import StaffData
from Models.voyageData import VoyageData
from Models.flightData import FlightData
from Models.airplaneData import AirplaneData
from Models.destinationData import DestinationData
from Models.fileHandler import FileHandler



class CreateIO():
    def __init__(self):
        self.aircraftPath = "Data/AircraftType.csv"
        self.crewPath = "Data/Crew.csv"
        self.destinationPath = "Data/DestinationData.csv"
        self.upcomingFlightsPath = "Data/UpcomingFlights.csv"
        self.upcomingVoyagesPath = "Data/UpcomingVoyages.csv"



    def addNewAirplane(self, newAirplane):
        #  FileHandler DTO instance created
        fileObject = FileHandler(self.aircraftPath)

        #  File opend with appendFile()
        airplaneFile = fileObject.appendFile()
        fieldnames = ["planeTypeId","planeType","model","capacity"]
        writer = csv.DictWriter(airplaneFile, fieldnames=fieldnames)
        writer.writerow({"planeTypeId": newAirplane.getPlaneId(), "planeType": newAirplane.getType(),
                        "model": newAirplane.getModel(), "capacity": newAirplane.getCapacity()})
        airplaneFile.close()


    def addNewStaff(self, newEmployee):
        #  FileHandler DTO instance created
        fileObject = FileHandler(self.crewPath)

        #  File opend with appendFile()
        crewFile = fileObject.appendFile()
        fieldnames = ["ssn", "name", "address", "cellPhone", "phoneNumber", "email", "role", "rank", "license"]
        writer = csv.DictWriter(crewFile, fieldnames=fieldnames)
        writer.writerow({"ssn": newEmployee.getSSN(), "name": newEmployee.getName(), "address": newEmployee.getAddress(),
                        "cellPhone": newEmployee.getCellPhone(), "phoneNumber": newEmployee.getPhoneNumber(),
                        "email": newEmployee.getEmail(), "role": newEmployee.getRole(), "rank": newEmployee.getRank(),
                        "license": newEmployee.getLicence()})
        crewFile.close()

    def addNewDest(self, newDestination):
        #  FileHandler DTO instance created
        fileObject = FileHandler(self.destinationPath)

        #  File opend with appendFile()
        destinationFile = fileObject.appendFile()
        fieldnames = ["destName","flightTime","distance","contact","phoneNumber"]
        writer = csv.DictWriter(destinationFile, fieldnames=fieldnames)
        writer.writerow({"destName": newDestination.getDestName(),"flightTime": newDestination.getFlightTime(),
                        "distance": newDestination.getDistance(),"contact": newDestination.getPhoneNumber(),
                        "phoneNumber": newDestination.getContact()})
        destinationFile.close()

    def addNewFlight(self, newFlight):
        #  FileHandler DTO instance created
        fileObject = FileHandler(self.upcomingFlightsPath)
        #  File opend with appendFile()
        flightsFile = fileObject.appendFile()
        fieldnames = ["flightNumber", "departingFrom", "arrivingAt", "departure", "arrival"]
        writer = csv.DictWriter(flightsFile, fieldnames=fieldnames)
        writer.writerow({"flightNumber": newFlight.getFlightNumber(), "departingFrom": newFlight.getDepartingFrom(),
                         "arrivingAt": newFlight.getArrivingAt(), "departure": newFlight.getDeparture(),
                         "arrival": newFlight.getArrival()})
        flightsFile.close()

    def addNewVoyage(self, flightFromKEF, flightToKEF, newVoyage):
        flight1 = flightFromKEF.getFlightNumber()
        flight2 = flightToKEF.getFlightNumber()
        departingFrom = flightFromKEF.getDepartingFrom()
        arrivingAt = flightFromKEF.getArrivingAt()
        departureFromKEF = flightFromKEF.getDeparture()
        arrivalToKEF = flightToKEF.getArrival()

        #  FileHandler DTO instance created
        fileObject = FileHandler(self.upcomingVoyagesPath)
        #  File opend with appendFile()
        voyageFile = fileObject.appendFile()        
        fieldnames = ["flightNumber1", "flightNumber2", "departingFrom", "arrivingAt", "departureFromKEF",
                        "arrivalToKEF", "aircraftID","captain", "coPilot", "fa1", "fa2"]
        writer = csv.DictWriter(voyageFile, fieldnames=fieldnames)
        writer.writerow({"flightNumber1": flight1, "flightNumber2": flight2, "departingFrom": departingFrom,
                         "arrivingAt": arrivingAt, "departureFromKEF": departureFromKEF, "arrivalToKEF": arrivalToKEF,
                         "aircraftID": newVoyage.getAirplane(), "captain": newVoyage.getPilot(), "coPilot": newVoyage.getCoPilot(),
                         "fa1": newVoyage.getFa1(), "fa2": newVoyage.getFa2()})
