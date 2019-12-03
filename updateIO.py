from destinationData import DestinationData
import csv

class UpdateIO:

    def __init__(self):
        self.destPath = 'Destinations.csv'
        self.licensePath = 'Crew.csv'

    def updateDestIO(self, country, contact, emergencyNumber):

        csv_file = open(self.destPath, 'r')
        reader = csv.DictReader(csv_file)
        destinations_list = []

        for row in reader:
            destinations_list.append(DestinationData(row['country'], row['flightTime'], row['contact'], row['emergencyNumber']))

        for item in destinations_list:
            if item.getCountry() == country:
                item.setContact(contact)
                item.emergencyNumber(emergencyNumber)
            

test = UpdateIO()

test.updateDestIO('Thorshavn', 'Darth', '6666969')
