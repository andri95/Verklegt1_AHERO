#import sys
#sys.path.append('../Models/destinationData')
from Models.destinationData import DestinationData
#from .Models.destinationData import DestinationData
#from .Models.staffData import StaffData
#from .Models.fileHandler import FileHandler
import csv

class UpdateIO:

    def __init__(self):
        self.destPath = '../Data/Destinations.csv'
        self.licensePath = '../Data/Crew.csv'

    def updateDestIO(self, country, contact, emergencyNumber):

        #with open(self.destPath, 'r') as destinationsFile:
            #reader = csv.DictReader(destinationsFile)
            #destinations_list = []

            #for row in reader:
                #destinations_list.append(DestinationData(row['country'], row['flightTime'], row['contact'], row['emergencyNumber']))

        fileObject = FileHandler(self.destPath)
        reader = fileObject.readFile()
        destinations_list = []
        for row in reader:
            destinations_list.append(DestinationData(row['country'], row['flightTime'], row['contact'], row['emergencyNumber']))


        with open(self.destPath, 'w') as destinationsFile:
            fieldnames = ['country','flightTime','contact','emergencyNumber']
            writer = csv.DictWriter(destinationsFile, fieldnames=fieldnames)
            writer.writeheader()

        with open(self.destPath, 'a') as destinationsFile:
            fieldnames = ['country','flightTime','contact','emergencyNumber']
            writer = csv.DictWriter(destinationsFile, fieldnames=fieldnames)
            for destination in destinations_list:
                if destination.getCountry() == country:
                    destination.setContact(contact)
                    destination.setEmergencyNumber(emergencyNumber)
                writer.writerow({'country': destination.getCountry(), 'flightTime': destination.getFlightTime(), 
                                'contact': destination.getContact(), 'emergencyNumber': destination.getEmergencyNumber()})

    def addLicenseIO(self, SSN, newLicense):

        with open(self.licensePath, 'r') as crewFile:
            reader = csv.DictReader(crewFile)
            crew_list = []

            for row in reader:
                crew_list.append(StaffData(row['ssn'], row['name'], row['address'], row['cellPhone'], row['phoneNumber'], row['email'], row['role'], row['rank'], row['licence']))

        with open(self.licensePath, 'w') as crewFile:
            fieldnames = ['ssn','name','address','cellPhone','phoneNumber','email','role','rank','licence']
            writer = csv.DictWriter(crewFile, fieldnames=fieldnames)
            writer.writeheader()

        with open(self.licensePath, 'a') as crewFile:
            fieldnames = ['ssn','name','address','cellPhone','phoneNumber','email','role','rank','licence']
            writer = csv.DictWriter(crewFile, fieldnames=fieldnames)
            for employee in crew_list:
                if employee.getSSN() == SSN:
                    employee.setLicense(newLicense)
                writer.writerow({'ssn': employee.getSSN(),'name': employee.getName(),'address': employee.getAddress(),
                                'cellPhone': employee.getCellPhone(),'phoneNumber': employee.getPhoneNumber(),'email': employee.getEmail(),
                                'role': employee.getRole(),'rank': employee.getRank(),'licence': employee.getLicence()})


        
            

            

test = UpdateIO()

test.updateDestIO('Thorshavn', 'Darth', '7774444')

