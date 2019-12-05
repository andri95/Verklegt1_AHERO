import csv
from Models.airplaneData import AirplaneData
from Models.staffData import StaffData
from Models.destinationData import DestinationData
from Models.flightData import FlightData
from Models.voyageData import VoyageData
from Models.fileHandler import FileHandler

class ReadIO():
    def __init__(self):
        self.aircraftPath = "AircraftType.csv"
        self.crewPath = "Crew.csv"
        self.destinationPath = "DestinationData.csv"
        self.upcomingFlightsPath = "UpcomingFlights.csv"


    def getDestinations(self):
        with open(self.destinationPath, 'r') as destinationFile:
            reader = csv.DictReader(destinationFile)
            destination_list = []
            for row in reader:
                destination_list.append(
                    DestinationData(row['country'], row['flightTime'], row['contact'], row['emergencyNumber']))

        return destination_list

    def getVoyages(self):
        pass

    def getStaff(self):
        with open(self.crewPath, 'r') as crewFile:
            reader = csv.DictReader(crewFile)
            crew_list = []
            for row in reader:
                crew_list.append(StaffData(row['ssn'], row['name'], row['address'], row['cellPhone'],
                row['phoneNumber'], row['email'], row['role'], row['rank'], row['licence']))

        return crew_list

    def getAirplanes(self):
        with open(self.aircraftPath, 'r') as airplaneFile:
            reader = csv.DictReader(airplaneFile)
            airplane_list = []
            for row in reader:
                airplane_list.append(AirplaneData(row["planeTypeId"], row["planeType"], row["model"], row["capacity"]))

            return airplane_list

    def getFlights(self):
        with open(self.upcomingFlightsPath, 'r') as upcomingFlightsFile:
            reader = csv.DictReader(upcomingFlightsFile)
            flights_list = []
            for row in reader:
                flights_list.append(
                    FlightData(row['flightNumber'], row['departingFrom'], row['arrivingAt'], row['departure'],
                               row['arrival']))
        return flights_list

