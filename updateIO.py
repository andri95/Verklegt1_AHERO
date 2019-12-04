from destinationData import DestinationData
import csv

class UpdateIO:

    def __init__(self):
        self.destPath = 'Destinations.csv'
        self.licensePath = 'Crew.csv'

    def updateDestIO(self, country, contact, emergencyNumber):

        with open(self.destPath, 'w+') as destinationsFile:
            reader = csv.DictReader(destinationsFile)
            destinations_list = []

            for row in reader:
                destinations_list.append(DestinationData(row['country'], row['flightTime'], row['contact'], row['emergencyNumber']))

            fieldnames = ['country','flightTime','contact','emergencyNumber']
            writer = csv.DictWriter(destinationsFile, fieldnames=fieldnames)
            for destination in destinations_list:
                if destination.getCountry() == country:
                    destination.setContact(contact)
                    destination.emergencyNumber(emergencyNumber)
                writer.writerow({'country': destination.getCountry(), 'flightTime': destination.getFlightTime(),
                                'contact': destination.getContact(), 'emergencyNumber': destination.getEmergencyNumber()})


            

test = UpdateIO()

test.updateDestIO('Thorshavn', 'Darth', '6666969')
