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
        self.destinationPath = "Data/Destinations.csv"
        self.upcomingFlightsPath = "Data/UpcomingFlights.csv"
        self.upcomingVoyagesPath = "Data/UpcomingVoyages.csv"

    def addNewAirplane(self, newAirplane):
        #  FileHandler DTO instance created
        fileObject = FileHandler(self.aircraftPath)

        #  File opend with appendFile()
        airplaneFile = fileObject.appendFile()
        field_list = fileObject.findFieldNames()
        writer = csv.DictWriter(airplaneFile, fieldnames=field_list)
        writer.writerow({field_list[0]: newAirplane.getPlaneId(), field_list[1]: newAirplane.getType(),
                         field_list[2]: newAirplane.getModel(), field_list[3]: newAirplane.getCapacity()})
        airplaneFile.close()

    def addNewStaff(self, newEmployee):
        #  FileHandler DTO instance created
        fileObject = FileHandler(self.crewPath)

        #  File opend with appendFile()
        crewFile = fileObject.appendFile()
        field_list = fileObject.findFieldNames()
        writer = csv.DictWriter(crewFile, fieldnames=field_list)
        writer.writerow(
            {field_list[0]: newEmployee.getSSN(), field_list[1]: newEmployee.getName(), field_list[2]: newEmployee.getAddress(),
             field_list[3]: newEmployee.getCellPhone(), field_list[4]: newEmployee.getPhoneNumber(),
             field_list[5]: newEmployee.getEmail(), field_list[6]: newEmployee.getRole(), field_list[7]: newEmployee.getRank(),
             field_list[8]: newEmployee.getLicence()})
        crewFile.close()

    def addNewDest(self, newDestination):
        #  FileHandler DTO instance created
        fileObject = FileHandler(self.destinationPath)
        #  File opend with appendFile()
        destinationFile = fileObject.appendFile()
        field_list = fileObject.findFieldNames()
        writer = csv.DictWriter(destinationFile, fieldnames=field_list)
        writer.writerow({field_list[0]: newDestination.getCountry(), field_list[1]: newDestination.getFlightTime()
                         ,field_list[2]: newDestination.getContact(),field_list[3]: newDestination.getEmergencyNumber()})
        destinationFile.close()

    def addNewFlight(self, newFlight):
        #  FileHandler DTO instance created
        fileObject = FileHandler(self.upcomingFlightsPath)
        #  File opend with appendFile()
        flightsFile = fileObject.appendFile()
        field_list = fileObject.findFieldNames()
        writer = csv.DictWriter(flightsFile, fieldnames=field_list)
        writer.writerow({field_list[0]: newFlight.getFlightNumber(), field_list[1]: newFlight.getDepartingFrom(),
                         field_list[2]: newFlight.getArrivingAt(), field_list[3]: newFlight.getDeparture(),
                         field_list[4]: newFlight.getArrival()})
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
        field_list = fileObject.findFieldNames()
        writer = csv.DictWriter(voyageFile, fieldnames=field_list)
        writer.writerow({field_list[0]: flight1,field_list[1]: flight2,field_list[2]: departingFrom,
                         field_list[3]: arrivingAt,field_list[4]: departureFromKEF,field_list[5]: arrivalToKEF,
                         field_list[6]: newVoyage.getAirplane(),field_list[7]: newVoyage.getPilot(),
                         field_list[8]: newVoyage.getCoPilot(),field_list[9]: newVoyage.getFa1(),
                         field_list[10]: newVoyage.getFa2()})