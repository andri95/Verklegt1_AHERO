import csv
from Models.staffData import StaffData
from Models.voyageData import VoyageData
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
             field_list[8]: newEmployee.getLicense()})
        crewFile.close()

    def addNewDest(self, newDestination):
        #  FileHandler DTO instance created
        fileObject = FileHandler(self.destinationPath)
        #  File opend with appendFile()
        destinationFile = fileObject.appendFile()
        field_list = fileObject.findFieldNames()
        writer = csv.DictWriter(destinationFile, fieldnames=field_list)
        writer.writerow({field_list[0]: newDestination.getCountry(), field_list[1]: newDestination.getFlightTime(),
                         field_list[2]: newDestination.getContact(),field_list[3]: newDestination.getEmergencyNumber(),
                         field_list[4]: newDestination.getDestId()})
        destinationFile.close()

    def addNewVoyage(self, newVoyage):
        #  FileHandler DTO instance created
        fileObject = FileHandler(self.upcomingVoyagesPath)
        #  File opend with appendFile()
        voyageFile = fileObject.appendFile()
        field_list = fileObject.findFieldNames()
        writer = csv.DictWriter(voyageFile, fieldnames=field_list)
        writer.writerow({field_list[0]: newVoyage.getFlightNumber(), field_list[1]: newVoyage.getDepartingFrom(),
                         field_list[2]: newVoyage.getArrivingAt(),
                         field_list[3]: newVoyage.getDepartureTime(),field_list[4]: newVoyage.getArrivalTime(), field_list[5]: newVoyage.getAircraftId(),
                         field_list[6]: newVoyage.getCaptain(),field_list[7]: newVoyage.getCoPilot(),
                         field_list[8]: newVoyage.getFa1(),field_list[9]: newVoyage.getFa2()})

        voyageFile.close()