import csv
from destinationData import DestinationData

class ReadIO():

    def __init__(self):
        self.destiPath = 'Destinations.csv'

    def getDestinations(self):
        with open(self.destiPath, 'r') as destFile:
            reader = csv.DictReader(destFile)
            dest_list = []
            for row in reader:
                dest_list.append(DestinationData(row['country'],row['flightTime'], row['contact'], row['emergencyNumber']))

        return dest_list


test = ReadIO()
test.getDestinations()




