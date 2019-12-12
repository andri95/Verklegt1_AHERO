import csv
from Models.destinationData import DestinationData
from Models.staffData import StaffData
from Models.voyageData import VoyageData
from Models.fileHandler import FileHandler

class UpdateIO:
 
    def __init__(self):
        self.destinationPath = 'Data/Destinations.csv'
        self.licensePath = 'Data/Crew.csv'
        self.upcomingVoyagePath = 'Data/Voyages.csv'

    def updateVoyage(self, dataList, staffList):
        # FileHandler DTO instance created
        fileObject = FileHandler(self.upcomingVoyagePath)

        upcomingVoyageFile = fileObject.readFile()
        reader = csv.DictReader(upcomingVoyageFile)
        field_list = fileObject.findFieldNames()
        voyage_list = []
        for row in reader:
            voyage_list.append(VoyageData(row[field_list[0]], row[field_list[1]], row[field_list[2]], row[field_list[3]], row[field_list[4]], row[field_list[5]], row[field_list[6]], row[field_list[7]], row[field_list[8]], row[field_list[9]]))
        upcomingVoyageFile.close()
        upcomingVoyageFile = fileObject.writeFile()
        fieldnames = field_list
        writer = csv.DictWriter(upcomingVoyageFile, fieldnames=fieldnames)
        writer.writeheader()
        upcomingVoyageFile.close()
        upcomingVoyageFile = fileObject.appendFile()
        fieldnames = field_list
        writer = csv.DictWriter(upcomingVoyageFile, fieldnames=fieldnames)

        i = 0
        while i < len(voyage_list):
            if dataList[0].getFlightNumber() == voyage_list[i].getFlightNumber():
                voyage_list[i].setCaptain(staffList[0])
                voyage_list[i].setCoPilot(staffList[1])
                voyage_list[i].setFa1(staffList[2])
                voyage_list[i].setFa2(staffList[3])
                voyage_list[i+1].setCaptain(staffList[0])
                voyage_list[i+1].setCoPilot(staffList[1])
                voyage_list[i+1].setFa1(staffList[2])
                voyage_list[i+1].setFa2(staffList[3])
            writer.writerow({field_list[0]: voyage_list[i].getFlightNumber(), field_list[1]: voyage_list[i].getDepartingFrom(),
                             field_list[2]: voyage_list[i].getArrivingAt(), field_list[3]: voyage_list[i].getDepartureTime(),
                             field_list[4]: voyage_list[i].getArrivalTime(), field_list[5]: voyage_list[i].getAircraftId(),
                             field_list[6]: voyage_list[i].getCaptain(), field_list[7]: voyage_list[i].getCoPilot(),
                             field_list[8]: voyage_list[i].getFa1(), field_list[9]: voyage_list[i].getFa2()})
            writer.writerow(
                {field_list[0]: voyage_list[i+1].getFlightNumber(), field_list[1]: voyage_list[i+1].getDepartingFrom(),
                 field_list[2]: voyage_list[i+1].getArrivingAt(), field_list[3]: voyage_list[i+1].getDepartureTime(),
                 field_list[4]: voyage_list[i+1].getArrivalTime(), field_list[5]: voyage_list[i+1].getAircraftId(),
                 field_list[6]: voyage_list[i+1].getCaptain(), field_list[7]: voyage_list[i+1].getCoPilot(),
                 field_list[8]: voyage_list[i+1].getFa1(), field_list[9]: voyage_list[i+1].getFa2()})
            i+=2

        upcomingVoyageFile.close()
    
    def updateDest(self, dataList):

        # FileHandler DTO instance created
        fileObject = FileHandler(self.destinationPath)

        # File opened with readFile()
        destinationsFile = fileObject.readFile()
        reader = csv.DictReader(destinationsFile)
        field_list = fileObject.findFieldNames()
        destinations_list = []
        for row in reader:
            destinations_list.append(DestinationData(row[field_list[0]], row[field_list[1]], row[field_list[2]], row[field_list[3]], row[field_list[4]]))
 
        # File closed
        destinationsFile.close()
 
        # File opened with writeFile()
        destinationsFile = fileObject.writeFile()
        fieldnames = field_list
        writer = csv.DictWriter(destinationsFile, fieldnames=fieldnames)
        writer.writeheader()
 
        # File closed
        destinationsFile.close()
 
        # File opened with appendFile()
        destinationsFile = fileObject.appendFile()
        fieldnames = field_list
        writer = csv.DictWriter(destinationsFile, fieldnames=fieldnames)
        for destination in destinations_list:
            if destination.getCountry() == dataList[0]:
                destination.setContact(dataList[1])
                destination.setEmergencyNumber(dataList[2])
            writer.writerow({field_list[0]: destination.getCountry(), field_list[1]: destination.getFlightTime(),
                            field_list[2]: destination.getContact(), field_list[3]: destination.getEmergencyNumber(), field_list[4]: destination.getDestId()})
       
        # File closed
        destinationsFile.close()

    def addLicense(self, dataList):

        # FileHandler DTO instance created
        fileObject = FileHandler(self.licensePath)
 
        # File opened with readFile()
        crewFile = fileObject.readFile()
        reader = csv.DictReader(crewFile)
        field_list = fileObject.findFieldNames()
        crew_list = []
        for row in reader:
            crew_list.append(StaffData(row[field_list[0]], row[field_list[1]], row[field_list[2]], row[field_list[3]], row[field_list[4]], row[field_list[5]], row[field_list[6]], row[field_list[7]], row[field_list[8]]))
       
        # File closed
        crewFile.close()
 
        # File opened with writeFile()
        crewFile = fileObject.writeFile()
        fieldnames = field_list
        writer = csv.DictWriter(crewFile, fieldnames=fieldnames)
        writer.writeheader()
 
        # File closed
        crewFile.close()
 
        # File opened with appendFile()
        crewFile = fileObject.appendFile()
        fieldnames = field_list
        writer = csv.DictWriter(crewFile, fieldnames=fieldnames)
        for employee in crew_list:
            if employee.getSSN() == dataList[0]:
                employee.setLicense(dataList[1])
            writer.writerow({field_list[0]: employee.getSSN(),field_list[1]: employee.getName(),field_list[2]: employee.getAddress(),
                            field_list[3]: employee.getCellPhone(),field_list[4]: employee.getPhoneNumber(),field_list[5]: employee.getEmail(),
                            field_list[6]: employee.getRole(),field_list[7]: employee.getRank(),field_list[8]: employee.getLicense()})
 
        # File closed
        crewFile.close()

