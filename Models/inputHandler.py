from Models.airplaneData import AirplaneData
from Models.destinationData import DestinationData
from Models.flightData import FlightData
from Models.staffData import StaffData
from Models.voyageData import VoyageData

class InputHandler:

    def addNewAirplaneIH(self):
        planeID = input("Enter airplane ID: ")
        types = input("Enter Airplane type: ")
        model = input("Enter Model name: ")
        capacity = input("Enter Airplane Capacity")
        newAirplane = AirplaneData(planeID, types, model, capacity)
        return newAirplane

    def addNewDestinationIH(self):
        country = input('Enter country: ')
        flighttime = input('Enter flight time: ')
        contact = input('Enter contact: ')
        emergencynum = input('Enter emergency number: ')
        newDestination = DestinationData(country, flighttime, contact, emergencynum)
        return newDestination

    def addNewStaffIH(self):
        ssn = input('Enter social security number: ')
        name = input('Enter name: ')
        address = input('Enter address: ')
        cellPhone = input('Enter cell phone: ')
        phoneNumber = input('Enter phone number: ')
        email = input('Enter email: ')
        role = input('Enter role: ')
        rank = input('Enter rank: ')
        license_str = input('Enter license: ')
        newEmployee = StaffData(ssn, name, address, cellPhone, phoneNumber, email, role, rank, license_str)
        return newEmployee