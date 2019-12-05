import csv
from Models.destinationData import DestinationData
from Models.staffData import StaffData
from Models.fileHandler import FileHandler

class UpdateIO:
 
    def __init__(self):
        self.destinationPath = 'Data/Destinations.csv'
        self.licensePath = 'Data/Crew.csv'

    def updateDest(self, dataList):

        # FileHandler DTO instance created
        fileObject = FileHandler(self.destinationPath)

 
        # File opened with readFile()
        destinationsFile = fileObject.readFile()
        reader = csv.DictReader(destinationsFile)
        field_list = fileObject.findFieldNames()
        destinations_list = []
        for row in reader:
            destinations_list.append(DestinationData(row[field_list[0]], row[field_list[1]], row[field_list[2]], row[field_list[3]]))
 
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
                            field_list[2]: destination.getContact(), field_list[3]: destination.getEmergencyNumber()})
       
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
                            field_list[6]: employee.getRole(),field_list[7]: employee.getRank(),field_list[8]: employee.getLicence()})
 
        # File closed
        crewFile.close()

