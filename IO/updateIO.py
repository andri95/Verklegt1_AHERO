
from Models.destinationData import DestinationData
from Models.staffData import StaffData
from Models.fileHandler import FileHandler
import csv

class UpdateIO:

    def __init__(self):
        self.destPath = 'Data/Destinations.csv'
        self.licensePath = 'Data/Crew.csv'

    def updateDestIO(self, country, contact, emergencyNumber):

        # FileHandler DTO instance created
        fileObject = FileHandler(self.destPath)

        # File opened with readFile()
        destinationsFile = fileObject.readFile()
        reader = csv.DictReader(destinationsFile)
        destinations_list = []
        for row in reader:
            destinations_list.append(DestinationData(row['country'], row['flightTime'], row['contact'], row['emergencyNumber']))

        # File closed
        destinationsFile.close()

        # File opened with writeFile()
        destinationsFile = fileObject.writeFile()
        fieldnames = ['country','flightTime','contact','emergencyNumber']
        writer = csv.DictWriter(destinationsFile, fieldnames=fieldnames)
        writer.writeheader()

        # File closed
        destinationsFile.close()

        # File opened with appendFile()
        destinationsFile = fileObject.appendFile()
        fieldnames = ['country','flightTime','contact','emergencyNumber']
        writer = csv.DictWriter(destinationsFile, fieldnames=fieldnames)
        for destination in destinations_list:
            if destination.getCountry() == country:
                destination.setContact(contact)
                destination.setEmergencyNumber(emergencyNumber)
            writer.writerow({'country': destination.getCountry(), 'flightTime': destination.getFlightTime(), 
                            'contact': destination.getContact(), 'emergencyNumber': destination.getEmergencyNumber()})
        
        # File closed
        destinationsFile.close()
            

    def addLicenseIO(self, SSN, newLicense):

        # FileHandler DTO instance created
        fileObject = FileHandler(self.licensePath)

        # File opened with readFile()
        crewFile = fileObject.readFile()
        reader = csv.DictReader(crewFile)
        crew_list = []
        for row in reader:
            crew_list.append(StaffData(row['ssn'], row['name'], row['address'], row['cellPhone'], row['phoneNumber'], row['email'], row['role'], row['rank'], row['licence']))
        
        # File closed
        crewFile.close()

        # File opened with writeFile()
        crewFile = fileObject.writeFile()
        fieldnames = ['ssn','name','address','cellPhone','phoneNumber','email','role','rank','licence']
        writer = csv.DictWriter(crewFile, fieldnames=fieldnames)
        writer.writeheader()

        # File closed
        crewFile.close()

        # File opened with appendFile()
        crewFile = fileObject.appendFile()
        fieldnames = ['ssn','name','address','cellPhone','phoneNumber','email','role','rank','licence']
        writer = csv.DictWriter(crewFile, fieldnames=fieldnames)
        for employee in crew_list:
            if employee.getSSN() == SSN:
                employee.setLicense(newLicense)
            writer.writerow({'ssn': employee.getSSN(),'name': employee.getName(),'address': employee.getAddress(),
                            'cellPhone': employee.getCellPhone(),'phoneNumber': employee.getPhoneNumber(),'email': employee.getEmail(),
                            'role': employee.getRole(),'rank': employee.getRank(),'licence': employee.getLicence()})

        # File closed
        crewFile.close()


        
            

            


