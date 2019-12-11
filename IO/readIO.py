import csv
from Models.airplaneData import AirplaneData
from Models.staffData import StaffData
from Models.destinationData import DestinationData
from Models.voyageData import VoyageData
from Models.fileHandler import FileHandler

class ReadIO:
    def __init__(self):
        self.aircraftPath = "Data/AircraftType.csv"
        self.crewPath = "Data/Crew.csv"
        self.destinationPath = "Data/Destinations.csv"
        self.upcomingFlightsPath = "Data/UpcomingFlights.csv"
        self.upcomingVoyagesPath = "Data/UpcomingVoyages.csv"
        self.PastFlightsPath = "Data/PastFlights.csv"


    def getDestinations(self):
        fileObject = FileHandler(self.destinationPath)
        fileForRead = fileObject.readFile()
        reader = csv.DictReader(fileForRead)
        field_list = fileObject.findFieldNames()
        destination_list = []
        for row in reader:
            destination_list.append(
            DestinationData(row[field_list[0]], row[field_list[1]], row[field_list[2]], row[field_list[3]], row[field_list[4]]))

        return destination_list

    def getVoyages(self):
        fileObject = FileHandler(self.upcomingVoyagesPath)
        fileForRead = fileObject.readFile()
        reader = csv.DictReader(fileForRead)
        field_list = fileObject.findFieldNames()
        voyages_list = []
        for row in reader:
            voyages_list.append(
                VoyageData(row[field_list[0]], row[field_list[1]], row[field_list[2]], row[field_list[3]], row[field_list[4]],
                           row[field_list[5]], row[field_list[6]], row[field_list[7]], row[field_list[8]], row[field_list[9]]))

        return voyages_list




    def getStaff(self):
        fileObject = FileHandler(self.crewPath)
        fileForRead = fileObject.readFile()
        reader = csv.DictReader(fileForRead)
        field_list = fileObject.findFieldNames()
        crew_list = []
        for row in reader:
            crew_list.append(StaffData(row[field_list[0]], row[field_list[1]], row[field_list[2]], row[field_list[3]],
            row[field_list[4]], row[field_list[5]], row[field_list[6]], row[field_list[7]], row[field_list[8]]))

        return crew_list

    def getAirplanes(self):
        fileObject = FileHandler(self.aircraftPath)
        fileForRead = fileObject.readFile()
        reader = csv.DictReader(fileForRead)
        field_list = fileObject.findFieldNames()
        airplane_list = []
        for row in reader:
            airplane_list.append(AirplaneData(row[field_list[0]], row[field_list[1]], row[field_list[2]], row[field_list[3]]))

        return airplane_list


