import csv
from Models.flightData import FlightData
from Models.staffData import StaffData
from Models.voyageData import VoyageData
from Models.flightData import FlightData
from Models.airplaneData import AirplaneData
from Models.destinationData import DestinationData
from Models.fileHandler import FileHandler
<<<<<<< HEAD
 
 
 
=======


>>>>>>> fe9095908bc8f66a11b58e272557180a41e15d97
class CreateIO():
    def __init__(self):
        self.aircraftPath = "Data/AircraftType.csv"
        self.crewPath = "Data/Crew.csv"
        self.destinationPath = "Data/DestinationData.csv"
        self.upcomingFlightsPath = "Data/UpcomingFlights.csv"
        self.upcomingVoyagesPath = "Data/UpcomingVoyages.csv"
<<<<<<< HEAD
 
 
 
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
 
=======

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
        writer.writerow({field_list[0]: newDestination.getDestName(), field_list[1]: newDestination.getFlightTime(),
                         field_list[2]: newDestination.getDistance(), field_list[3]: newDestination.getPhoneNumber(),
                         field_list[4]: newDestination.getContact()})
        destinationFile.close()

>>>>>>> fe9095908bc8f66a11b58e272557180a41e15d97
    def addNewFlight(self, newFlight):
        #  FileHandler DTO instance created
        fileObject = FileHandler(self.upcomingFlightsPath)
        #  File opend with appendFile()
        flightsFile = fileObject.appendFile()
<<<<<<< HEAD
        fieldnames = ["flightNumber", "departingFrom", "arrivingAt", "departure", "arrival"]
        writer = csv.DictWriter(flightsFile, fieldnames=fieldnames)
        writer.writerow({"flightNumber": newFlight.getFlightNumber(), "departingFrom": newFlight.getDepartingFrom(),
                         "arrivingAt": newFlight.getArrivingAt(), "departure": newFlight.getDeparture(),
                         "arrival": newFlight.getArrival()})
        flightsFile.close()
 
=======
        field_list = fileObject.findFieldNames()
        writer = csv.DictWriter(flightsFile, fieldnames=field_list)
        writer.writerow({field_list[0]: newFlight.getFlightNumber(), field_list[1]: newFlight.getDepartingFrom(),
                         field_list[2]: newFlight.getArrivingAt(), field_list[3]: newFlight.getDeparture(),
                         field_list[4]: newFlight.getArrival()})
        flightsFile.close()

>>>>>>> fe9095908bc8f66a11b58e272557180a41e15d97
    def addNewVoyage(self, flightFromKEF, flightToKEF, newVoyage):
        flight1 = flightFromKEF.getFlightNumber()
        flight2 = flightToKEF.getFlightNumber()
        departingFrom = flightFromKEF.getDepartingFrom()
        arrivingAt = flightFromKEF.getArrivingAt()
        departureFromKEF = flightFromKEF.getDeparture()
        arrivalToKEF = flightToKEF.getArrival()
<<<<<<< HEAD
 
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






=======
>>>>>>> fe9095908bc8f66a11b58e272557180a41e15d97

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