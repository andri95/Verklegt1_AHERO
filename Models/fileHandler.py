import csv

class FileHandler:

    def __init__(self, path):
        self.path = path
        #self.aircraftTypePath = 'AircraftType.csv'
        #self.crewPath = 'Crew.csv'
        #self.destinationsPath = 'Destinations.csv'
        #self.pastFlightsPath = 'PastFlights.csv'
        #self.upcomingFlightsPath = 'UpcomingFlights.csv'
        #self.upcomingVoyagesPath = 'UpcomingVoyages.csv'

    def readFile(self):
        with open (self.path, 'r') as returnFile:
            reader = csv.reader(returnFile)
            return reader


    