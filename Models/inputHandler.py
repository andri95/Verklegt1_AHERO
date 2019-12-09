from Models.airplaneData import AirplaneData
from Models.destinationData import DestinationData
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

    def addNewFlightIH(self):
        flightNumber = input("Enter an ID for the flight ")
        departingFrom = input("Where will you be flying from: ")
        arrivalTime = input("When will you be flying: (Y/M/D, TT:TT:TT): ")
        departureTime = input("Where will you be arriving at: ")
        arrivingAt = input("When will you be arriving (Y/M/D, TT:TT:TT): ")
        aircraftId = input("Put di aircarft inn: ")
        newFlight = VoyageData(flightNumber, departingFrom, arrivingAt , departureTime, arrivalTime , aircraftId)
        return newFlight

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

    def updateDestinationIH(self):
        destToChange = input('Enter country you want to change: ')
        newContact = input('New contact name: ')
        newEmergencyNumber = input('New emergency number: ')
        dataList = [destToChange, newContact, newEmergencyNumber]
        return dataList
        
    def updateVoyageIH(self):
        staff_list = []
        staff_list.append(input("Enter a Captain"))
        staff_list.append(input("Enter a Co-Pilot"))
        staff_list.append(input("Enter a flight attendant: "))
        staff_list.append(input("Enter a flight attendant: "))
        return staff_list
